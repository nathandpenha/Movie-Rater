from django.contrib import admin
from .models import Book, BookNumber
# Register your models here.


#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title','description']
    list_display = ['title','description','price']
    list_filter = ['is_published','published']
    search_fields = ['title','description']

admin.site.register(BookNumber)