import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dds_servis.settings")
django.setup()

from serv.init_data import load_initial_data
load_initial_data()