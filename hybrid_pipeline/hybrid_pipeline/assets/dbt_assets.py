from dagster_dbt import load_assets_from_dbt_project
from dagster import AssetSelection, define_asset_job

DBT_PROJECT_PATH = "/Users/hasangeren/Documents/melbourne-meetup"
DBT_PROFILES_PATH = "/Users/hasangeren/Documents/melbourne-meetup"

pipeline_1_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH,
    profiles_dir=DBT_PROFILES_PATH,
    select="pipeline_1",
    key_prefix=["pipeline_1"]
)

pipeline_2_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH,
    profiles_dir=DBT_PROFILES_PATH,
    select="pipeline_2",
    key_prefix=["pipeline_2"]
)

pipeline_1_job = define_asset_job(
    "pipeline_1_job",
    selection=AssetSelection.keys(*[key for asset in pipeline_1_assets for key in asset.keys])
)

pipeline_2_job = define_asset_job(
    "pipeline_2_job",
    selection=AssetSelection.keys(*[key for asset in pipeline_2_assets for key in asset.keys])
)

all_assets = [*pipeline_1_assets, *pipeline_2_assets]
all_jobs = [pipeline_1_job, pipeline_2_job]
