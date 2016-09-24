from __future__ import unicode_literals
from mongoengine import *

# http://docs.mongoengine.org/guide/defining-documents.html#dealing-with-deletion-of-referred-documents

ADDRESS_LEN = 100
NAME_LEN = 25
COMMENT_LEN = 200


class Comment(Document):
    text = StringField(max_length=COMMENT_LEN)
    # user = ReferenceField('User')  # TODO


class Log(Document):
    user = ReferenceField('User')
    comments = ListField(ReferenceField(Comment))
    checkin = DateTimeField(required=True)
    checkout = DateTimeField(required=True)  # TODO figure out timing


class Contact(Document):
    name = StringField(max_length=NAME_LEN, required=True)
    organization = StringField(max_length=NAME_LEN)
    address = StringField(max_length=ADDRESS_LEN)
    number = StringField(max_length=15, required=True)
    email = EmailField()


class Unit(Document):
    serial = StringField(max_length=25, unique=True, required=True)
    name = StringField(max_length=NAME_LEN)
    logs = ListField(ReferenceField(Log))
    # site = ReferenceField(Site, required=True)
    contacts = ListField(ReferenceField(Contact))
    # TODO schematics (optional)
    # TODO photos (optional)
    # TODO add indexing and QuerySet ordering for efficiency:
    # meta = {}


class Site(Document):
    name = StringField(max_length=25, unique=True, required=True)
    address = StringField(max_length=ADDRESS_LEN)
    units = ListField(ReferenceField(Unit))
    # TODO loc = GeoPointField()
