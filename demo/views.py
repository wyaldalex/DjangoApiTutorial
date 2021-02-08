from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer , SmallBookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import  Response



class BookViewSet(viewsets.ModelViewSet):
    serializer_class = SmallBookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


