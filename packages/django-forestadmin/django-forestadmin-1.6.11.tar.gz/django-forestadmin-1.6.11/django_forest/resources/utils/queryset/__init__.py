from .filters import FiltersMixin
from .limit_fields import LimitFieldsMixin
from .pagination import PaginationMixin
from .scope import ScopeMixin
from .search import SearchMixin
from .segment import SegmentMixin
from django_forest.resources.utils.decorators import DecoratorsMixin


class QuerysetMixin(
    PaginationMixin, FiltersMixin, SearchMixin, ScopeMixin, DecoratorsMixin, LimitFieldsMixin, SegmentMixin
):
    def filter_queryset(self, queryset, Model, params, request):
        # Notice: first apply scope
        scope_filters = self.get_scope(request, Model)
        if scope_filters is not None:
            queryset = queryset.filter(scope_filters)

        # Notice: then apply filters and search
        PARAMS = {
            'filters': self.get_filters,
            'search': self.get_search
        }
        for name, method in PARAMS.items():
            if name in params and params[name]:
                queryset = queryset.filter(method(params, Model))
        return queryset

    def enhance_queryset(self, queryset, Model, params, request, apply_pagination=True):
        # scopes + filter + search
        queryset = self.filter_queryset(queryset, Model, params, request)

        # sort
        if 'sort' in params:
            queryset = queryset.order_by(params['sort'].replace('.', '__'))

        # segment
        queryset = self.handle_segment(params, Model, queryset)

        # limit fields
        queryset = self.handle_limit_fields(params, Model, queryset)

        # pagination
        if apply_pagination:
            queryset = self.get_pagination(params, queryset)

        return queryset
