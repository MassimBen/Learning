import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from dlt.helpers.marimo import render, load_package_viewer,pipeline_selector

    return (mo,)


@app.cell
def _():
    import duckdb
    import dlt

    conn = duckdb.connect("D:/Learning/Learning-progress/Learning/dlt-learning/taxi_pipeline.duckdb")
    return (conn,)


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM taxi_pipeline.main.taxi_trips limit 10;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT max(trip_dropoff_date_time) as max_time FROM taxi_pipeline.main.taxi_trips;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""

        SELECT min(trip_pickup_date_time) as min_date, max(trip_pickup_date_time) as max_date FROM taxi_pipeline.main.taxi_trips;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT payment_type, count(*) *100 / sum(count(*)) over() as pourcentage FROM taxi_pipeline.main.taxi_trips group by payment_type;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT sum(total_amt) as nb_tip FROM taxi_pipeline.main.taxi_trips;
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
