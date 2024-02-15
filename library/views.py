from .models import Book, BorrowRecord
from .serializers import (
    BookSerializer,
    BorrowBookResponseSerializer,
    BorrowBookSerializer,
    BorrowRecordSerializer,
    ReturnBookSerializer,
)
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for books.
    Only can be accessed by staff user.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "author"]


class BorrowRecordViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for book borrow records.
    Only can be accessed by staff user.
    """

    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "book__title",
        "book__author",
        "borrower__username",
        "borrower__email",
    ]


class BorrowBookViewSet(viewsets.ViewSet):
    """
    View with functionality to borrow a book.
    Only can be accessed by staff user.
    Accepts only POST method.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = BorrowRecord.objects.none()

    @swagger_auto_schema(
        request_body=BorrowBookSerializer, responses={200: BorrowBookResponseSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = BorrowBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data["book"]
        BorrowRecord.objects.create(
            book=book,
            borrower=serializer.validated_data["borrower"],
            borrow_date=datetime.now().date(),
        )
        book.quantity -= 1
        book.save()

        return Response({"success": True}, status=status.HTTP_200_OK)


class ReturnBookViewSet(viewsets.ViewSet):
    """
    View with functionality to return a book.
    Only can be accessed by staff user.
    Accepts only POST method.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = BorrowRecord.objects.none()

    @swagger_auto_schema(
        request_body=ReturnBookSerializer, responses={200: BorrowBookResponseSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = ReturnBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data["book"]
        record = BorrowRecord.objects.filter(
            book=book,
            borrower=serializer.validated_data["borrower"],
            return_date__isnull=True,
        ).first()
        if not record:
            return Response(
                "The book is not borrowed by this user.",
                status=status.HTTP_404_NOT_FOUND,
            )
        record.return_date = datetime.now().date()
        book.quantity += 1
        record.save()
        book.save()

        return Response({"success": True}, status=status.HTTP_200_OK)
