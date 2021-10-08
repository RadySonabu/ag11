import os
import re
from textwrap import dedent
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):

    help = "Create serializers and views"
    # Gets the name of the app

    def add_arguments(self, parser):
        parser.add_argument("app", type=str, nargs="+",
                            help="Get the app name")

    def handle(self, *args, **kwargs):
        app_name = kwargs["app"][0]
        # new_project_name = kwargs['new'][0]

        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))
        )
        path = base_dir + "\\apps" + "\\" + app_name
        admin_path = path + "\\admin.py"
        file = open(admin_path, "w") 
        file.write("from django.contrib import admin\n") 
        file.write("from django import forms\n") 
        
        app = apps.get_app_config(app_name).get_models()
        model_names = [apps.get_model(
            app_name, str(m._meta.object_name)) for m in app]
        model_fields = [m._meta.get_fields() for m in model_names]

        models = []
        for m in model_names:
            models.append(m.__name__)
        
        comma_separated_models = ','.join(i for i in models)
        file.write(f'from .models import {comma_separated_models} \n\n')
        """
        class OrganizationStaffAdminForm(forms.ModelForm):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['user'].queryset = User.objects.filter(role=2)

        class OrganizationStaffScheduleInline(admin.TabularInline):
            model = OrganizationStaffSchedule
            extra = 0
        class OrganizationStaffAdmin(admin.ModelAdmin):
            form = OrganizationStaffAdminForm
            inlines = [
                OrganizationStaffScheduleInline,
            ]
            list_display = ('user', 'doctor_type')
        """
        for m in model_names:
            fields = []
            for field in m._meta.concrete_fields:

                field_model = field.model.__name__
                model = m.__name__

                if model == field_model:
                    # if field.name != 'id':
                    fields.append(field.name)
            file.write(f'class {model}Admin(admin.ModelAdmin):\n\tlist_display={fields}\n')     
            # file.write(f"\n\t\tfields='__all__'")
            file.write(f'admin.site.register({m.__name__}, {model}Admin)\n')        