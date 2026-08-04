"""dlt pipeline for ingesting NYC taxi data from a REST API."""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"


@dlt.source
def taxi_pipeline_source():
    """Create a dlt source for the NYC taxi REST API."""
    config: RESTAPIConfig = {
        "client": {
            "base_url": BASE_URL,
            "paginator": "auto",
        },
        "resource_defaults": {
            "endpoint": {
                "params": {
                    "size": 1000,
                },
            },
        },
        "resources": [
            {
                "name": "taxi_trips",
                "endpoint": {
                    "path": "",
                },
            }
        ],
    }

    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    dataset_name="main",
    refresh="drop_sources",
    progress="log",
)


if __name__ == "__main__":
    load_info = pipeline.run(taxi_pipeline_source())
    print(load_info)

    if load_info.loads_ids:
        print(f"\n✅ Pipeline réussi — {len(load_info.loads_ids)} package(s) chargé(s)")
        with pipeline.sql_client() as client:
            with client.execute_query("SELECT count(*) FROM taxi_trips") as cur:
                count = cur.fetchone()[0]
                print(f"📊 Lignes chargées dans taxi_trips : {count}")
    else:
        print("\n❌ Aucune donnée chargée")