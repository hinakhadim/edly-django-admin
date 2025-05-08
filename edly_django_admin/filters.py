from openedx_filters.tooling import OpenEdxPublicFilter

from django import forms
from django.contrib import admin


class DjangoUserAdminThemeFilter(OpenEdxPublicFilter):
    

    filter_type = "org.edly.theme.v1"

    @classmethod
    def run_filter(cls, model, admin_class):
        result = super().run_pipeline(model, admin_class)
        return result