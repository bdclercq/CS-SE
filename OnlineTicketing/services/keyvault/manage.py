import unittest

from flask.cli import FlaskGroup

from project import create_app, db  # new
from project.api.models import Keyvault  # new
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import requests

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
