import click
from wbo.main import wbo
import lxml
import pandas as pd
from datetime import datetime as dt
import os
import plotly.graph_objects as go
import plotly
import tempfile
from time import sleep

@click.group()
def cli():
    """
    WBO
    Get box office mojo's worldwide box office data.
    Plot the data.
    Usage:
    Type "wbo get-data" or "wbo display-plot" in the command line. These will run the two commands with their default values.
    You can also specify the earliest year and the latest year like this:
    "wbo get-data -min=2005 -max=2020" 

    by Adnan Hoq
    """


@cli.command()
@click.option('-min', '--min_year', default = 2019,
    help = 'Earliest year of data you want', type=int)
@click.option('-max', '--max_year', default = 2021,
    help = 'Latest year of data you want', type=int)
def get_data(min_year, max_year):
    """
    Get the Data as csv.
    """
    dk = wbo()
    dm=dk.collect_bom(min_year=min_year,max_year=max_year)
    print("Saving the data as a csv file in your Download folder!")        
    sleep(3)
    dm.to_csv(os.path.expanduser(f'~/Downloads/worldwide_box_office({min_year}-{max_year}).csv'),index=False)




@cli.command()
@click.option('-min', '--min_year', default = 2019,
    help = 'Earliest year of data you want')
@click.option('-max', '--max_year', default = 2021,
    help = 'Latest year of data you want')
def display_plot(min_year, max_year):
    """
    Display the data in a scatter plot.
    """
    dk = wbo()
    dm=dk.collect_bom(min_year=min_year,max_year=max_year)
    dm2=dk.get_top_movies()
    dk.plot_gross_scatter()


if __name__ == '__main__':
    cli()


    