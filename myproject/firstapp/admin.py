from django.contrib import admin
from .models import User
from .models import Events

class EventsAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'event_price', 'stock')
# Register your models here.


admin.site.register(User)
admin.site.register(Events, EventsAdmin)



