from rest_framework import viewsets, renderers

import django_filters

from fruitex.api.views import ChildModelViewSetMixin
from delivery.models import *
from delivery.api.serializers import *

# Filters
class DeliveryBucketFilter(django_filters.FilterSet):
  after = django_filters.DateTimeFilter(name="end", lookup_type='gt')
  before = django_filters.DateTimeFilter(name="start", lookup_type='lt')
  class Meta:
    model = DeliveryBucket
    fields = ['assignee__username', 'assignee__id', 'after', 'before']


# Views
class DeliveryBucketViewSet(viewsets.ReadOnlyModelViewSet):
  renderer_classes = (
    renderers.JSONRenderer,
    renderers.JSONPRenderer,
    renderers.BrowsableAPIRenderer)
  model = DeliveryBucket
  serializer_class = DeliveryBucketSerializer
  filter_class = DeliveryBucketFilter
  ordering = ['-start']

class DeliveryBucketOrderViewSet(ChildModelViewSetMixin, viewsets.ReadOnlyModelViewSet):
  renderer_classes = (
    renderers.JSONRenderer,
    renderers.JSONPRenderer,
    renderers.BrowsableAPIRenderer)
  model = DeliveryBucketOrder
  parent_model = DeliveryBucket
  serializer_class = DeliveryBucketOrderSerializer
