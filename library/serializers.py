from rest_framework import serializers
from .models import Book, BorrowRecord


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = "__all__"


class BorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ("book", "borrower")

    def validate_book(self, value):
        """Validation for book while borrowing.
        """
        if not value.quantity:
            raise serializers.ValidationError("Book is not available.")
        return value


class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ("book", "borrower")


class BorrowBookResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()

