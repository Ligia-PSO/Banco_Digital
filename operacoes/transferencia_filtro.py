from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter
import django_filters
from operacoes.models import transferencia

# class TransferenciaFilter(FilterSet):
#     data = django_filters.DateTimeFilter(
#         method='filter_guest_level', field_name='guest_level')
#     # de_data = DateTimeFilter(method='data',
#                                             #  lookup_expr='gte')
#     # ate_data = DateTimeFilter(field_name='data',
#     #                                        lookup_expr='lte')
#     class Meta:
#         model = transferencia
#         fields = (
#             'conta',
#             'de_data',
#             # 'ate_data',
#             )