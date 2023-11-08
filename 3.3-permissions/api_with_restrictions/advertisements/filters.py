from django_filters import rest_framework as filters

from advertisements.models import Advertisement

STATUS_CHOICES = (
    ('OPEN', 'OPEN'),
    ('CLOSED', 'CLOSED'),
)


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(choices=STATUS_CHOICES)
    creator = filters.DjangoFilterBackend()

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at']
