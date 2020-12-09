from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

#https://qxf2.com/blog/database-migration-flask-migrate/

ma = Marshmallow()
db = SQLAlchemy()