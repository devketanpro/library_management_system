from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet,
    BorrowBookViewSet,
    BorrowRecordViewSet,
    ReturnBookViewSet,
)

router = DefaultRouter()
router.register(r"books", BookViewSet) # CRUD apis for books.
router.register(r"borrow-records", BorrowRecordViewSet) # CRUD apis for borrow records.
router.register(r"borrow-book", BorrowBookViewSet) # POST api to borrow a book.
router.register(r"return-book", ReturnBookViewSet) # POST api to return a book.

urlpatterns = [
    path("", include(router.urls)),
]
