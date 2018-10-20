from django.contrib import admin
from .models import Bid
from .models import Choice

# Register your models here.


#admin.site.register(Bid)
admin.site.register(Choice)


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'phone', 'date')
    list_filter = ('lastname', 'date')

# Register the admin class with the associated model


#admin.site.register(Bid, BidAdmin)






