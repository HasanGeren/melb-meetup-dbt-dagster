from dagster import define_asset_job, AssetSelection, AssetKey
from .assets.dbt_assets import dbt_assets

# Get all asset keys except 'refresh_stg_app_events'
dbt_asset_keys = [asset_key for dbt_asset in dbt_assets for asset_key in dbt_asset.keys if asset_key != AssetKey("refresh_stg_app_events")]

run_dbt_models = define_asset_job(
    "run_dbt_models",
    selection=AssetSelection.keys(*dbt_asset_keys)
)

hybrid_stream_update = define_asset_job(
    "hybrid_stream_update",
    selection=AssetSelection.keys("refresh_stg_app_events") | AssetSelection.keys("int_user_activity").downstream()
)
