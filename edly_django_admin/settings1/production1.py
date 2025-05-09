from django.conf import settings
from edx_django_utils.plugins.constants import (
     PluginURLs, PluginSettings
)
 
app_label_edly = 'edly_django_admin.apps:EdlyDjangoAdminConfig'


def plugin_settings(settings):
    if app_label_edly in settings.INSTALLED_APPS:
        # settings.INSTALLED_APPS.remove(app_label_edly)
        settings.INSTALLED_APPS.insert(0, app_label_edly)
        print("------Done----", settings.INSTALLED_APPS[:5])


# ./manage.py lms collectstatic