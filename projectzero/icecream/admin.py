from django.contrib import admin
from .models import Icecream

class IcecreamAdmin(admin.ModelAdmin):
    list_display = ('pk','name','avatar','desc','price','rating')

admin.site.register(Icecream, IcecreamAdmin)
