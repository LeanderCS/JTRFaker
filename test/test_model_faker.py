from datetime import datetime, date

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ModelFaker import ModelFaker


"""
Test the ModelFaker class
"""

iapp = Flask(__name__)
iapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
iapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(iapp)


class MyModel(db.Model):
    """
    A simple SQLAlchemy model for testing the ModelFaker class
    """

    id = db.Column(db.Integer, primary_key=True)
    string_field = db.Column(db.String(80), nullable=False)
    short_string_field = db.Column(db.String(5), nullable=False)
    long_string_field = db.Column(db.String(255), nullable=False)
    nullable_field = db.Column(db.String(80), nullable=True)
    boolean_field = db.Column(db.Boolean, nullable=False)
    default_field = db.Column(db.String(80), nullable=False, default="test123")
    integer_field = db.Column(db.Integer, nullable=False)
    max_min_integer_field = db.Column(db.Integer, nullable=False, info={"min": 100, "max": 101})
    date_field = db.Column(db.Date, nullable=False)
    datetime_field = db.Column(db.DateTime, nullable=False)
    json_field = db.Column(db.Text, nullable=False, doc='["string", "integer"]')


@pytest.fixture
def app() -> Flask:
    """
    Fixture to create a test Flask app with an in-memory database and remove
    it after the test.
    """

    with iapp.app_context():
        db.create_all()

        yield iapp

        db.drop_all()


@pytest.fixture
def client(app) -> Flask:
    """
    Fixture to create a test client for the Flask app.
    """

    return app.test_client()


@pytest.fixture
def fake_data(app) -> ModelFaker:
    """
    Fixture to create fake data for the MyModel model.
    """

    modelFaker = ModelFaker(MyModel)

    return modelFaker


def test_create_fake_data(fake_data) -> None:
    """
    Test if the ModelFaker is able to create fake data and validate each field.
    """

    fake_data.create(amount=5)

    fakeEntries = MyModel.query.all()
    assert len(fakeEntries) == 5


def test_nullable_field(fake_data) -> None:
    """
    Test if the nullable fields are handled correctly by ModelFaker.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert entry.nullable_field is None


def test_default_value(fake_data) -> None:
    """
    Test if the default value is correctly set (for price).
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert entry.default_field == "test123"


def test_string_field(fake_data) -> None:
    """
    Test if the string field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert isinstance(entry.string_field, str)


def test_integer_field(fake_data) -> None:
    """
    Test if the integer field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert isinstance(entry.integer_field, int)


def test_max_min_integer_field(fake_data) -> None:
    """
    Test if the integer field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert isinstance(entry.max_min_integer_field, int)
    assert entry.max_min_integer_field >= 100
    assert entry.max_min_integer_field <= 101


def test_bool_field(fake_data) -> None:
    """
    Test if the bool field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert isinstance(entry.boolean_field, bool)


def test_date_field(fake_data) -> None:
    """
    Test if the date field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert isinstance(entry.date_field, date)


def test_datetime_field(fake_data) -> None:
    """
    Test if the datetime field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert isinstance(entry.datetime_field, datetime)


def test_json_field(fake_data) -> None:
    """
    Test if the json field is handled correctly.
    """

    fake_data.create()

    entry = MyModel.query.first()

    assert entry.json_field is not None
    assert isinstance(entry.json_field, str)

    jsonData = eval(entry.json_field)
    assert isinstance(jsonData, list)
    assert len(jsonData) == 2

    assert isinstance(jsonData[0], str)
    assert isinstance(jsonData[1], int)
