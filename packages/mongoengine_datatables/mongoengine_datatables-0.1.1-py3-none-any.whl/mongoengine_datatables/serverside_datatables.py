'''DataTables server-side for Flask-MongoEngine'''
import json
import re

from bson import ObjectId, json_util
from mongoengine.fields import (BooleanField, DecimalField,
                                EmbeddedDocumentField,
                                EmbeddedDocumentListField, FloatField,
                                IntField, ListField, LongField, ObjectIdField,
                                ReferenceField, SequenceField)
from mongoengine.queryset.visitor import Q, QCombination


class DataTables(object):
    def __init__(self, model, request_args, embed_search={}, q_obj=[],
                 custom_filter={}, exclude_lst=[]):
        '''
        :param model: The MongoEngine model
        :param request_args: Passed as Flask request.values.get('args')
        :param embed_search: For specific search in EmbeddedDocumentField
        :param q_obj: Additional search results in reference collection
        :param custom_filter: Additional filter
        :param exclude_lst: For performance exclude(*fields)
        '''

        self.model = model
        self.request_args = request_args
        self.columns = self.request_args.get('columns')
        self.search_string = self.request_args.get('search', {}).get('value')
        self.embed_search = embed_search
        self.q_obj = q_obj
        self.custom_filter = custom_filter
        self.exclude_lst = exclude_lst

        _num_types = {IntField, BooleanField, DecimalField, FloatField,
                      LongField, SequenceField}
        _embed_types = {EmbeddedDocumentField, EmbeddedDocumentListField}

        self.field_type_dict = {}
        for k, v in model._fields.items():
            if type(v) in _num_types:
                self.field_type_dict[k] = 'number'
            elif type(v) in {ReferenceField}:
                self.field_type_dict[k] = 'reference'
            elif type(v) in {ObjectIdField}:
                self.field_type_dict[k] = 'objectID'
            elif type(v) in {ListField}:
                self.field_type_dict[k] = 'list'
            elif type(v) in _embed_types:
                self.field_type_dict[k] = 'embed'
            else:
                self.field_type_dict[k] = 'other'

    @property
    def total_records(self):
        if self.custom_filter:
            return str(self.model.objects(**self.custom_filter).count())
        return str(self.model.objects().count())

    @property
    def search_terms(self):
        return str(self.request_args.get("search")["value"]).split()

    @property
    def requested_columns(self):
        return [column["data"] for column in self.request_args.get("columns")]

    @property
    def draw(self):
        return self.request_args.get("draw")

    @property
    def start(self):
        return self.request_args.get("start")

    @property
    def limit(self):
        _length = self.request_args.get("length")
        if _length == -1:
            return None
        return _length

    @property
    def order_dir(self):
        ''' Return '' for 'asc' or '-' for 'desc' '''
        _dir = self.request_args.get("order")[0]["dir"]
        _MONGO_ORDER = {'asc': '', 'desc': '-'}
        return _MONGO_ORDER[_dir]

    @property
    def order_column(self):
        '''
        DataTables provides the index of the order column,
        but Mongo .sort wants its name.
        '''
        _order_col = self.request_args.get("order")[0]["column"]
        return self.requested_columns[_order_col]

    @property
    def dt_column_search(self):
        '''
        Adds support for datatables own column search functionality.
        documented here: https://datatables.net/examples/api/multi_filter.html
        '''

        _cols = []
        for column in self.request_args.get('columns'):
            _val = column['search']['value']
            _regex = column['search']['regex']
            _data = column['data']
            if _val == '':
                continue
            if not _regex:
                _cols.append(dict(column=_data, value=_val, regex=False))
            else:
                _d = {_data: re.compile(_val, re.IGNORECASE)}
                self.custom_filter.update(**_d)

        return _cols

    def query_by_col_type(self, _q, col):
        '''Build a query depending on the field type'''

        if self.field_type_dict.get(col) == 'number':
            # Fix OverflowError: MongoDB can only handle up to 8-byte ints
            # import sys;len(str(sys.maxsize)) ans: 19
            if _q.isdigit() and len(_q) < 19:
                return [Q(**{col: _q})]
            return []

        if self.field_type_dict.get(col) == 'objectID':
            if not ObjectId.is_valid(_q):
                return []

        if self.field_type_dict.get(col) == 'embed':
            if not self.embed_search:
                return []
            _em = []
            for field in self.embed_search.get(col)['fields']:
                _emb = f'{col}__{field}__icontains'
                _em.append(Q(**{_emb: _q}))
            return _em

        return [Q(**{col + '__icontains': _q})]

    @property
    def get_search_query(self):
        '''Create search request'''
        queries = []
        _column_names = [d['data'] for d in self.columns if d['data']
                         in self.field_type_dict.keys() and d['searchable']]
        # global search for all columns
        if self.search_string:
            for col in _column_names:
                _q = self.search_string
                _obj = self.query_by_col_type(_q, col)
                queries += _obj

        # search by specific columns
        _own_col_q = []
        for column_search in self.dt_column_search:
            col = column_search['column']
            term = column_search['value']
            _obj = self.query_by_col_type(term, col)
            _own_col_q += _obj

        if self.q_obj:
            queries.append(self.q_obj)

        _search_query = QCombination(QCombination.OR, queries)
        if _own_col_q:
            _own_col_q = QCombination(QCombination.AND, _own_col_q)
            _search_query = (_search_query & _own_col_q)

        if self.custom_filter:
            _search_query = (_search_query & Q(**self.custom_filter))

        return _search_query

    def results(self):
        _res = self.model.objects(self.get_search_query)
        _order_by = f'{self.order_dir}{self.order_column}'
        _results = _res.exclude(*self.exclude_lst).order_by(_order_by).skip(
            self.start).limit(self.limit).as_pymongo()

        # Use aggregate is very slow

        # Fix 'ObjectId' is not JSON serializable
        data = json.loads(json_util.dumps(_results))
        return dict(data=data, count=_res.count())

    def get_rows(self):
        _res = self.results()
        rec_totals = self.total_records if self.search_string \
            else _res.get('count')
        return {'recordsTotal': rec_totals,
                'recordsFiltered': _res.get('count'),
                'draw': int(str(self.draw)),
                'data': _res.get('data')}
