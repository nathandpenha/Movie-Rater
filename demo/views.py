from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# class Another(View):
#
#     book = Book.objects.get(id=1)
#     output = f"We have {book.title} with Book ID {book.id} <br>"
#
#     # for book in books:
#     #
#     #     output += f"We have {book.title} with Book ID {book.id} <br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)

#
#
# def first(request):
#     #return HttpResponse('First message from views')
#     books = Book.objects.all()
#     return render(request,'first_temp.html',{'books':books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)