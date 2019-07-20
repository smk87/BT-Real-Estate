from django.contrib import admin

# Register your models here.
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')  # Additional display fields

    list_display_links = ('id', 'title')  # Add clickable option
    list_filter = ('realtor',)  # Add filter option
    list_editable = ('is_published',)  # Add editable option
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode')  # Add searchfield option
    list_per_page = 25  # Maximum data per page


admin.site.register(Listing, ListingAdmin)  # Add this model to Admin page
