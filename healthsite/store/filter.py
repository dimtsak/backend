import django_filters
from django_filters import RangeFilter
from .models import *

class PriceFilter(django_filters.FilterSet):
    range = RangeFilter(field_name='price')
    class Meta:
        model = Product
        fields = ['price']
