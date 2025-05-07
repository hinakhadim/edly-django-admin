"""
edly_django_admin Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
     PluginURLs
 )
 
from openedx.core.djangoapps.plugins.constants import ProjectType


class EdlyDjangoAdminConfig(AppConfig):
    """
    Configuration for the edly_django_admin Django application.
    """

    name = 'edly_django_admin'

    plugin_app = {
         PluginURLs.CONFIG: {
             ProjectType.LMS: {
                 PluginURLs.NAMESPACE: 'user_custom',
                 PluginURLs.REGEX: r'^api/user_custom/',
                 PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }
