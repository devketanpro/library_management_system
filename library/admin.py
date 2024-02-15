from django.contrib import admin
from .models import Book, BorrowRecord


class BorrowRecordInline(admin.TabularInline):
    """Inline to show borrow records for a book."""
    extra = 0
    model = BorrowRecord
    readonly_fields = ["book", "borrower", "borrow_date", "return_date"]
    show_change_link = True


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "quantity"]
    list_display_links = ["id", "title", "author", "quantity"]
    search_fields = ["id", "title", "author"]
    inlines = [BorrowRecordInline]


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "borrower", "borrow_date", "return_date"]
    list_display_links = ["id", "book", "borrower", "borrow_date", "return_date"]
    search_fields = [
        "id",
        "book__title",
        "book__author",
        "borrower__email",
        "borrower__username",
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
