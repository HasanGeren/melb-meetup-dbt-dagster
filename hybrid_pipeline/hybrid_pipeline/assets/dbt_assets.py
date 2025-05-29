from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_DIR = "/Users/hasangeren/Documents/melbourne-meetup"
DBT_PROFILES_DIR = "/Users/hasangeren/Documents/melbourne-meetup"

# Load ALL dbt assets
dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_PROFILES_DIR,
)
