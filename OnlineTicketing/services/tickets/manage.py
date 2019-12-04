import unittest
import datetime

from flask.cli import FlaskGroup

from project import create_app, db  # new
from project.api.models import Ticket  # new

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    """Seeds the database."""
    db.session.add(Ticket(period_from=datetime.datetime(2020, 7, 20), period_to=datetime.datetime(2020, 7, 22)))
    db.session.add(Ticket(period_from=datetime.datetime(2020, 8, 2), period_to=datetime.datetime(2020, 8, 4)))
    db.session.commit()


if __name__ == '__main__':
    cli()
