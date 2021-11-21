from django.urls import reverse_lazy
from network.services import create_topology_pict
from django.views.generic import TemplateView, FormView
from network.forms import FileForm
from network.models import TopologyImages


class CreateTopologyView(FormView):
    template_name = "network/network_create_topology.html"
    form_class = FileForm
    success_url = reverse_lazy("topologies")

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist("filename")
        if form.is_valid():
            create_topology_pict(files, request.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class TopologyView(TemplateView):
    template_name = "network/network_topology.html"

    def get_context_data(self, **kwargs):
        topologies = TopologyImages.objects.all().filter(username=self.request.user.id).first()
        print(topologies, type(topologies))
        return {"topologies": topologies}
