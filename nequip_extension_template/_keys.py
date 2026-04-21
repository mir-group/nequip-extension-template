from typing import Final

# == IMPORTANT ==
# Import directly from the key registry to avoid importing the full `nequip.data` package during module import
# This keeps package dependency closure smaller for `nequip-package` and avoids pulling optional runtime integrations.
from nequip.data._key_registry import register_fields

# define the custom keys required for the extension package
DEV_FACING_GRAPH_FIELD_KEY: Final[str] = "user_facing_graph_field_name"
DEV_FACING_NODE_FIELD_KEY: Final[str] = "user_facing_node_field_name"

# register fields so that NequIP's data processing utilities can process the new keys
register_fields(
    graph_fields=[DEV_FACING_GRAPH_FIELD_KEY],
    node_fields=[DEV_FACING_NODE_FIELD_KEY],
)
