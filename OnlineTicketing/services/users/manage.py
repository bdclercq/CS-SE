import unittest

from flask.cli import FlaskGroup

from project import create_app, db  # new
from project.api.models import User  # new

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
    db.session.add(User(email="hermanmu@gmail.com", password="michael", cc="BE643200640052002"))
    db.session.add(User(email="michael@mherman.org", password="herman", cc="BE643200640054004"))
    db.session.add(User(email="bdclercq@hotmail.com", password="test", cc="BE643400640056002"))
    db.session.add(User(email="admin@admin.com", password="admin", cc="BE640000000000000"))
    db.session.commit()


if __name__ == '__main__':
    cli()
