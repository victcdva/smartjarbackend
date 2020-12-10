from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# https://qxf2.com/blog/database-migration-flask-migrate/

ma = Marshmallow()
db = SQLAlchemy()


class WeightData(db.Model):
    __tablename__ = "weightsdata"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(30))
    description = db.Column(db.String(40))
    created_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())


def __init__(self, value, description):
    self.value = value
    self.description = description


class WeightDataSchema(ma.Schema):
    id = fields.Integer(required=True)
    value = fields.String(required=True)
    description = fields.String(required=True)
    created_date = fields.DateTime()


class JarDevice(db.Model):
    __tablename__ = "jardevices"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    value = db.Column(db.Integer)
    weight_id = db.Column(db.Integer, db.ForeignKey(
        'weightsdata.id', ondelete='CASCADE'))
    weight = db.relationship(
        "WeightData", backref=db.backref("weightsdata", lazy='dynamic'))
    status = db.Column(db.Boolean(), server_default='1', default=True)
    created_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())


def __init__(self, name, value, weight_id):
    self.name = name
    self.value = value
    self.weight_id = weight_id


class JarDeviceSchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    value = fields.Integer(required=True)
    weight_id = fields.Integer(required=True)
    status = fields.Boolean()
    created_date = fields.DateTime()
