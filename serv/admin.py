from django.contrib import admin
from .models import DDS_record, Status, Type, category, subcategory

admin.site.register(DDS_record)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(category)
admin.site.register(subcategory)

