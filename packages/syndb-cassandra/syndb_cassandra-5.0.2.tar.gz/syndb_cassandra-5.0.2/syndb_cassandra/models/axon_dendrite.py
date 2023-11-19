from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from syndb_constants.table import SyndbTable, syndb_table_to_table_name

from syndb_cassandra.utils.misc import get_class_names


class Axon(Model):
    __table_name__ = syndb_table_to_table_name[SyndbTable.AXON]

    dataset_id = columns.UUID(primary_key=True)
    cid = columns.UUID(primary_key=True)

    # Placement for model-specific clustering keys =====================================================================

    terminal_count = columns.Integer()
    mitochondria_count = columns.Integer()
    total_mitochondria_volume = columns.Double()

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

    parent_id = columns.UUID()
    parent_enum = columns.Integer()

    neuron_id = columns.UUID()


class PreSynapticTerminal(Model):
    __table_name__ = syndb_table_to_table_name[SyndbTable.PRE_SYNAPTIC_TERMINAL]

    dataset_id = columns.UUID(primary_key=True)
    cid = columns.UUID(primary_key=True)

    # Placement for model-specific clustering keys =====================================================================

    vesicle_count = columns.Integer()
    total_vesicle_volume = columns.Double()

    mitochondria_count = columns.Integer()
    total_mitochondria_volume = columns.Double()

    forms_synapse_with = columns.UUID()

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

    parent_id = columns.UUID()
    parent_enum = columns.Integer()

    neuron_id = columns.UUID()


class DendriticSpine(Model):
    __table_name__ = syndb_table_to_table_name[SyndbTable.DENDRITIC_SPINE]

    dataset_id = columns.UUID(primary_key=True)
    cid = columns.UUID(primary_key=True)

    # Placement for model-specific clustering keys =====================================================================

    forms_synapse_with = columns.UUID()

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

    parent_id = columns.UUID()
    parent_enum = columns.Integer()

    neuron_id = columns.UUID()


class Dendrite(Model):
    __table_name__ = syndb_table_to_table_name[SyndbTable.DENDRITE]

    dataset_id = columns.UUID(primary_key=True)
    cid = columns.UUID(primary_key=True)

    # Placement for model-specific clustering keys =====================================================================

    dendritic_spine_count = columns.Integer()

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

    parent_id = columns.UUID()
    parent_enum = columns.Integer()

    neuron_id = columns.UUID()


dendrite_axon_models = (
    Axon,
    PreSynapticTerminal,
    DendriticSpine,
    Dendrite,
)
dendrite_axon_model_names = get_class_names(dendrite_axon_models)
