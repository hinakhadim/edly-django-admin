"""
edly_django_admin Django application initialization.
"""

from django.apps import AppConfig
from django.conf import settings
from edx_django_utils.plugins.constants import (
     PluginURLs, 
 )
 
from openedx.core.djangoapps.plugins.constants import ProjectType

app_label_edly = 'edly_django_admin.apps:EdlyDjangoAdminConfig'

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
        # 'settings_config': {
        #     'lms.djangoapp': {
        #         'production': { 'relative_path': 'settings.production' },
        #     }
        # },
    }

    def ready(self):
        self.prioritize_app()

    def prioritize_app(self):
        # 'edly_django_admin.apps.EdlyDjangoAdminConfig'
        app_label = 'edly_django_admin.apps.EdlyDjangoAdminConfig'
        # print("app-label -----> ", app_label, settings.INSTALLED_APPS)
        if app_label in settings.INSTALLED_APPS:
            # settings.INSTALLED_APPS.remove(app_label)
            settings.INSTALLED_APPS.insert(0, app_label)
            print("------Done----", settings.INSTALLED_APPS[:5])
