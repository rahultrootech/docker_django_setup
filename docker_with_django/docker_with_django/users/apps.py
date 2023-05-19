from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "docker_with_django.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import docker_with_django.users.signals  # noqa: F401
        except ImportError:
            pass
