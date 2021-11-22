from django.core.files import File
from network.draw_network_graph import draw_topology
from datetime import datetime
from apterek_blog.settings import BASE_DIR
from network.network_parser import unique_network_map, create_network_map
from network.models import TopologyImages, ImageModel
import shutil


# create svg file with devices topology, and with function "add_topology_to_database" and add it to database
def create_topology_pict(filenames: list, user) -> None:
    date = datetime.now()
    identification_mark = f"{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}"
    path_topology_save = f"{BASE_DIR}/media/network_topology/{user.id}/{identification_mark}"
    draw_topology(unique_network_map(create_network_map(filenames)), f"{path_topology_save}/topology")
    add_topology_to_database(path_topology_save, user)


# save a file with topology in a database, and remove from webserver
def add_topology_to_database(path: str, user) -> None:
    f = open(f"{path}/topology.svg")
    image = ImageModel()
    image.topology_image.save("topology.svg", File(f))
    last_image = ImageModel.objects.all().last()
    TopologyImages.objects.create(username=user, image=last_image)
    shutil.rmtree(f"{BASE_DIR}/media/network_topology/{user.id}")
