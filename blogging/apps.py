"""
blogging apps
"""

from django.apps import AppConfig


class BloggingConfig(AppConfig):
    """
    blogging config
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "blogging"
