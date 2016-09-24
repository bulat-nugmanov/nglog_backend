from __future__ import unicode_literals
from mongoengine import *


class Unit(Document):
    serial = StringField(max_length=25)
    name = StringField(max_length=50)
    # logbook
    # site
    # contacts
    # schematics (optional)
    # photos (optional)


class Site(Document):
    # name
    # address
    # lat lon
    # units
    # overview???
    """"""


class Logbook(Document):
    """"""
    # unit
    # logs


class Log(Document):
    """"""


class Comment(Document):
    text = StringField(max_length=150)
    # log
    # check in?
    # user


class Contact(Document):
    """"""
    # name
    # number
    # email
    #

