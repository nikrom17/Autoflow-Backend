import click
from flask.cli import with_appcontext

from .extensions import db
from .models import Lead, Opportunity, OpportunityInfo, FunnelStep
from .initialize_data import initialize_data

@click.command(name="create_tables")
@with_appcontext
def create_tables():
    db.create_all()
    
@click.command(name="drop_and_create_tables")
@with_appcontext
def drop_and_create_tables():
    db.drop_all()
    db.create_all()

@click.command(name="init_data")
@with_appcontext
def init_data():
    initialize_data()