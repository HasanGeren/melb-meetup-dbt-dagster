from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets.dbt_assets import dbt_assets
from .assets.refresh_mv import refresh_stg_app_events
from .jobs import run_dbt_models, hybrid_stream_update

defs = Definitions(
    assets=[refresh_stg_app_events, *dbt_assets],
    jobs=[run_dbt_models, hybrid_stream_update],
    resources={
        "dbt": DbtCliResource(
            project_dir="/Users/hasangeren/Documents/melbourne-meetup",
            profiles_dir="/Users/hasangeren/Documents/melbourne-meetup",
        ),
    },
)
