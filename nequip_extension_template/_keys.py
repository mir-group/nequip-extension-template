from nequip.data import register_fields
from typing import Final

# define the custom keys required for the extension package
DEV_FACING_GRAPH_FIELD_KEY: Final[str] = "user_facing_graph_field_name"
DEV_FACING_NODE_FIELD_KEY: Final[str] = "user_facing_node_field_name"

# register fields so that NequIP's data processing utilities can process the new keys
register_fields(
    graph_fields=[DEV_FACING_NODE_FIELD_KEY],
    node_fields=[DEV_FACING_GRAPH_FIELD_KEY],
)
