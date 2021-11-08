"""
polling apps
"""

from django.apps import AppConfig


class PollingConfig(AppConfig):
    """
    polling Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polling'
