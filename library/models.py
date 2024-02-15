from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.id}. {self.title} - {self.author}"


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.borrower.email} - {self.book.title}"
