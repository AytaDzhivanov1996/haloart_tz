import django_filters
from django_filters import OrderingFilter

from shopping_list.models import Item

class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    quantity = django_filters.NumberFilter()
    quantity__gt = django_filters.NumberFilter(field_name='quantity', lookup_expr='gt')
    quantity__lt = django_filters.NumberFilter(field_name='quantity', lookup_expr='lt')

    o = OrderingFilter(
        fields=(
            ('quantity', 'quantity'),
            ('name', 'name')
        )
    )

    class Meta:
        model = Item
        fields = ['quantity']