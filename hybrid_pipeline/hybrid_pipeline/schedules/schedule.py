from dagster import define_asset_job, AssetSelection, ScheduleDefinition

# Define pipeline_2 job: staging (MV), intermediate (incremental), marts (view)
pipeline_2_scheduled_job = define_asset_job(
    name="pipeline_2_scheduled_job",
    selection=AssetSelection.keys(
        ("pipeline_2", "int_user_activity_p2"),
        ("pipeline_2", "marts_user_metrics_p2"),
    )
)

# Run job every 2 minutes
pipeline_2_schedule = ScheduleDefinition(
    job=pipeline_2_scheduled_job,
    cron_schedule="*/2 * * * *",
    name="pipeline_2_schedule",
)
