from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status)
        
        return queryset

class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookStats(APIView):
    def get(self, request):
        books = Book.objects.all()

        count = 0
        rating = 0
        count_per_status = {}

        for book in books:
            count += 1
            book_status = book.status
            if book_status not in count_per_status:
                count_per_status[book_status] = 1
            else:
                count_per_status[book_status] += 1
            
            if book_status == 'finished':
                rating += book.rating
            
            if rating != 0:
                average_rating = round(rating / count_per_status['finished'], 2)
            else:
                average_rating = 0
            
        return Response({
            'count': count,
            'count_per_status': count_per_status,
            'average_rating': average_rating,
        }, status=status.HTTP_200_OK)