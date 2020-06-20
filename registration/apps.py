from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'registration'

    # Using signals in our app
    def ready(self):
        import registration.signals
