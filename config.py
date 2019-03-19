import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_DATABASE_URI ="postgres://postgres:apple321@35.182.246.214:5432/garage_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False