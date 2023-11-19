import pkgutil

from cassandra.cqlengine import ValidationError, columns
from cassandra.cqlengine.models import Model
from orjson import orjson
from syndb_constants.table import SyndbTable, syndb_table_to_table_name

neuron_data = orjson.loads(pkgutil.get_data("syndb_cassandra", "assets/neuron_types.json"))


class Neuron(Model):
    __table_name__ = syndb_table_to_table_name[SyndbTable.NEURON]

    dataset_id = columns.UUID(primary_key=True)
    cid = columns.UUID(primary_key=True)

    # Placement for model-specific clustering keys =====================================================================

    polarity = columns.Ascii(max_length=35)
    neuron_type = columns.Ascii(max_length=35)
    direction = columns.Ascii(max_length=35)

    # ==================================================================================================================

    voxel_volume = columns.Double()
    voxel_radius = columns.Double()

    mesh_path = columns.Text()
    mesh_volume = columns.Double()
    mesh_surface_area = columns.Double()
    mesh_area_volume_ratio = columns.Double()
    mesh_sphericity = columns.Double()

    centroid_z = columns.Double()
    centroid_x = columns.Double()
    centroid_y = columns.Double()

    neuron_id = columns.UUID()

    def validate(self):
        super().validate()
        if self.polarity and self.polarity not in neuron_data["polarity"]:
            msg = f"{self.polarity} is not a valid polarity, make sure that the characters are lowercase"
            raise ValidationError(msg)

        if self.neuron_type and self.neuron_type not in neuron_data["type"]:
            msg = f"{self.neuron_type} is not a valid neuron type, make sure that the characters are lowercase"
            raise ValidationError(msg)

        if self.direction and self.direction not in neuron_data["direction"]:
            msg = f"{self.direction} is not a valid direction, make sure that the characters are lowercase"
            raise ValidationError(msg)
