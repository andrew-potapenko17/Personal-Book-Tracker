from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookView, basename='book')

urlpatterns = [
    path('books/<int:pk>/', views.SingleBookView.as_view(), name='single_book'),
    path('books/stats/', views.BookStats.as_view(), name='stats')
] + router.urls