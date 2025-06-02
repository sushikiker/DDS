from django.contrib import admin
from .models import DDS_record, Status, Type, category, subcategory

from datetime import datetime, timedelta
from .models import DDS_record


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(category)
admin.site.register(subcategory)


class CreatedAtDateRangeFilter(admin.SimpleListFilter):
    title = ('Дата')
    parameter_name = 'created_range'

    def lookups(self, request, model_admin):
        return (
            ('today', ('Сегодня')),
            ('7days', ('Последние 7 дней')),
            ('30days',('Последние 30 дней')),
        )

    def queryset(self, request, queryset):
        value = self.value()
        now = datetime.now()
        if value == 'today':
            return queryset.filter(created_at__date=now.date())
        elif value == '7days':
            return queryset.filter(created_at__gte=now - timedelta(days=7))
        elif value == '30days':
            return queryset.filter(created_at__gte=now - timedelta(days=30))
        return queryset

@admin.register(DDS_record)
class DDSRecordAdmin(admin.ModelAdmin):
    list_filter = [
        CreatedAtDateRangeFilter,  # фильтр по дате
        'status',                  # фильтр по статусу
        'type',                    # фильтр по типу
        'category',                # фильтр по категории
        'subcategory',             # фильтр по подкатегории
    ]
    list_display = ['created_at', 'status', 'type', 'category', 'subcategory', 'summ']