from __future__ import unicode_literals
from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in
from djoser.signals import user_registered
import receivers


class EngineConfig(AppConfig):
    name = 'engine'

    # runs once
    def ready(self):
        # register token authenticator function with login signal
        user_registered.connect(receivers.auth_token_callback)
