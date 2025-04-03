from rest_framework import serializers
from.models import Book ,Rental

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Rental
        fields = ['id', 'user', 'book', 'book_title', 'rented_at', 'returned_at']