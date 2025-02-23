from django.contrib import admin
from .models import Airport,Flight,Passengers

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassengersAdmin(admin.ModelAdmin):
    filter_Horizontal=("flights",)    


admin.site.register(Airport)
admin.site.register(Flight , FlightAdmin)
admin.site.register(Passengers , PassengersAdmin)