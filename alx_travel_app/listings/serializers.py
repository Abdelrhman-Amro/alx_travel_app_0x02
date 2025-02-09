from rest_framework import serializers

from .models import Booking, Listing, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["name", "description", "location", "price_per_night", "host"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["start_date", "end_date", "total_price", "status", "guest", "listing"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["rating", "comment", "created_at", "listing", "user"]
