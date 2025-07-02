from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets.dbt_assets import all_assets, all_jobs
from .schedules.schedule import pipeline_2_scheduled_job, pipeline_2_schedule


defs = Definitions(
    assets=all_assets,
    jobs=all_jobs+ [pipeline_2_scheduled_job],
    schedules=[pipeline_2_schedule],
    resources={
        "dbt": DbtCliResource(
            project_dir="/Users/hasangeren/Documents/melbourne-meetup",
            profiles_dir="/Users/hasangeren/Documents/melbourne-meetup",
        ),
    },
)