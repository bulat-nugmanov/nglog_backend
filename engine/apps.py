from __future__ import unicode_literals
from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in
import receivers


class EngineConfig(AppConfig):
    name = 'engine'

    # runs once
    def ready(self):
        # register token authenticator function with login signal
        user_logged_in.connect(receivers.auth_token_callback,
                               dispatch_uid='aoeighaergalegraei09u3ot')
