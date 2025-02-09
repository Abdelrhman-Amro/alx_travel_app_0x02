from django.contrib import admin

from .models import Booking, Listing, Review


class ListingAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "host")
    search_fields = ("name", "host__username", "location")
    list_filter = ("host__username", "location")


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "listing",
        "guest",
        "start_date",
        "end_date",
        "total_price",
        "status",
    )
    search_fields = ("guest__username", "listing__name")
    list_filter = ("status",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "rating", "comment")
    search_fields = ("user__username", "listing__name")
    list_filter = ("rating",)


admin.site.register(Listing, ListingAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
