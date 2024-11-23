from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UniversityApp.accounts'

    def ready(self):                                # when the app is READY
        import UniversityApp.accounts.signals       # import signals
