from django.urls import path
from django.conf import settings
from network.views import CreateTopologyView, TopologyView

urlpatterns = [
    path("topology_create/", CreateTopologyView.as_view(), name="create_topology"),
    path("topologies/", TopologyView.as_view(), name="topologies"),
]


