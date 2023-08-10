import os
import django
import importlib
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "premier_league_analysis.settings")
django.setup()

# from appname.models import YourModel
from django.apps import apps
from premier_league_analysis.settings import USER_APPS

def import_class(module_name, class_name):
    try:
        module = importlib.import_module(module_name)
        imported_class = getattr(module, class_name)
        return imported_class
    except (ImportError, AttributeError):
        return None

def import_and_print_models(app_name):
    try:
        app = apps.get_app_config(app_name)
    except LookupError:
        print(f"App '{app_name}' not found.")
        return
    
    for model in app.get_models():
        model_name = model.__name__
        template = f"from {app_name}.models import {model_name}"
        globals()[model_name] = import_class(app_name+'.models',model_name) 
    
        

app_name_to_import = USER_APPS
for app in app_name_to_import :
    import_and_print_models(app)
