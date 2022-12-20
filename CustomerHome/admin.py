from django.contrib import admin

# Register your models here.
from .models import Customer
from .team import teams
from .contact import Contact


class Team(admin.ModelAdmin):
    list_display = ['name','designation','twitter','facebook','linkedin']



admin.site.register(Customer)
admin.site.register(teams,Team)
admin.site.register(Contact)
