import django_filters
from . models import Film

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        fields = {'industry' : ['exact']}