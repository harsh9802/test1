from django.contrib import admin
from .models import llr_table,registration_table,complaint_table,Dl_table
# Register your models here.
admin.site.register(llr_table)
admin.site.register(registration_table)
admin.site.register(complaint_table)
admin.site.register(Dl_table)