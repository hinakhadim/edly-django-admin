"""
edly_django_admin Django application initialization.
"""

import importlib.util
from pathlib import Path

from django.apps import AppConfig
from django.conf import settings

from edx_django_utils.plugins.constants import PluginURLs 
from openedx.core.djangoapps.plugins.constants import ProjectType

app_label_edly = 'edly_django_admin.apps.EdlyDjangoAdminConfig'

class EdlyDjangoAdminConfig(AppConfig):
    """
    Configuration for the edly_django_admin Django application.
    """

    name = 'edly_django_admin'

    plugin_app = {
        PluginURLs.CONFIG: {
             ProjectType.LMS: {
                 PluginURLs.NAMESPACE: 'edly',
                 PluginURLs.REGEX: r'^api/edly/',
                 PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
    }

    def ready(self):
        self.prioritize_app()

    def prioritize_app(self):
        app_label = 'edly_django_admin.apps.EdlyDjangoAdminConfig'
        if app_label in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS.remove(app_label)
            settings.INSTALLED_APPS.insert(0, app_label)

            edly_django_admin_spec = importlib.util.find_spec("edly_django_admin")
            if edly_django_admin_spec and edly_django_admin_spec.origin:
                edly_django_admin_path = Path(edly_django_admin_spec.origin).parent / 'templates'
            
                DIRS = settings.TEMPLATES[0]['DIRS']
                DIRS = [edly_django_admin_path] + DIRS
                settings.TEMPLATES[0]['DIRS'] = DIRS
                print("------updated-----",settings.TEMPLATES[0])
