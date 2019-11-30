from django.contrib import admin
from restapp.models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ("name", "eid")
    list_filter = ("name", )
    search_fields = ("name", "eid", "data")


admin.site.register(Data, DataAdmin)

