from __future__ import unicode_literals
from django.apps import AppConfig


class EngineConfig(AppConfig):
    name = 'engine'

    def ready(self):
        import engine.receivers
