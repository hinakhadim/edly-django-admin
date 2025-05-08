
import logging
import requests
from openedx_filters import PipelineStep
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import NotRegistered

logger = logging.getLogger(__name__)


class GlobalAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add classes to all fields
        for field in self.fields.values():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing} edly-theme'


class GlobalAdmin(admin.ModelAdmin):
    form = GlobalAdminForm


class AdminThemePipeline(PipelineStep):
    def run_filter(self, model, admin_class):
        return [model, admin_class]

class CustomAdminThemePipeline(PipelineStep):
    def run_filter(self, model, admin_class):

        class FinalAdmin(admin_class, GlobalAdmin):
            pass
        return [model, FinalAdmin]
