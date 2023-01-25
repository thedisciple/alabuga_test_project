from django.contrib import admin
from .models import lords, soldiers, slaves_of_lords, slaves_of_soldiers

# Register your models here.
admin.site.register(lords)
admin.site.register(soldiers)
admin.site.register(slaves_of_lords)
admin.site.register(slaves_of_soldiers)