#!/usr/bin/env python
"""
CLI
"""
import os
import click
from databricks import sql

@click.group()
def cli():
    """
    Salary cli
    """

@cli.command()
def get_average_salary():
    """Get average salary"""

    print("Getting the avarage salary: ")
    with sql.connect(
        server_hostname=os.environ["DATABRICKS_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    ) as conn:

        with conn.cursor() as cursor:
            statement = (
                "SELECT AVG(SalaryUSD) FROM default.ds_salaries_csv"
            )
            cursor.execute(statement)
            result1 = cursor.fetchall()

            print(result1[0]["avg(SalaryUSD)"], "USD/Year")

@cli.command()
def get_max_salary():
    """Get the highest salary"""
    with sql.connect(
        server_hostname=os.environ["DATABRICKS_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    ) as conn:

        with conn.cursor() as cursor:
            statement = (
                "SELECT MAX(SalaryUSD) FROM default.ds_salaries_csv"
            )
            cursor.execute(statement)
            result1 = cursor.fetchall()

            print(result1[0]["max(SalaryUSD)"], "USD/Year")

@cli.command()
def get_min_salary():
    """Get the lowest salary"""
    with sql.connect(
        server_hostname=os.environ["DATABRICKS_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    ) as conn:

        with conn.cursor() as cursor:
            statement = (
                "SELECT MIN(SalaryUSD) FROM default.ds_salaries_csv"
            )
            cursor.execute(statement)
            result1 = cursor.fetchall()

            print(result1[0]["min(SalaryUSD)"], "USD/Year")

@cli.command()
@click.option("--year", default=2020, help="Year to get salary data for [2020-2022]")
def get_salary(year):
    """Get salary"""
    if year < 2020 or year > 2022:
        print("Year must be between 2020 and 2022")
        return

    print("Getting salary data for year: ", year)
    with sql.connect(
        server_hostname=os.environ["DATABRICKS_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    ) as conn:

        with conn.cursor() as cursor:
            statement = (
                "SELECT AVG(SalaryUSD) FROM default.ds_salaries_csv WHERE year = "
                + str(year)
            )
            cursor.execute(statement)
            result1 = cursor.fetchall()

            print(result1[0]["avg(SalaryUSD)"], "USD/Year")

if __name__ == "__main__":
    cli()