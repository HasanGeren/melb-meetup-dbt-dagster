## Melbourne Data Engineering Meetup Demo

This repository was created for the Melbourne Data Engineering Meetup. It demonstrates how dbt's materialized views and incremental models can be integrated with Dagster to handle hybrid data pipelines.

---

## Project Structure

- `models/` - Contains dbt models, organized by pipeline.
- `event_simulator/` - Python scripts to simulate event data for the demo.
- `hybrid_pipeline/` - Dagster project integrating dbt models, assets, and schedules for hybrid orchestration.
  - `assets/` - Dagster asset definitions.
  - `schedules/` - Dagster schedule definitions.
  - `hybrid_pipeline_tests/` - Tests for Dagster assets and pipelines.
- `dbt_project.yml` - dbt project configuration.
- `profiles.yml` - dbt profiles for connection settings.


