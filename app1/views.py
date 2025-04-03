from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Book, Rental
from .serializers import BookSerializer, RentalSerializer
from .pagination import CustomPagination

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]  # Anyone can view books
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'isbn']
    ordering_fields = ['published_date', 'price']

class RentalViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        rentals = Rental.objects.filter(user=request.user)
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def create(self, request):
        if Rental.objects.filter(user=request.user, returned_at__isnull=True).exists():
            return Response({'error': 'You already rented a book'}, status=status.HTTP_400_BAD_REQUEST)
        
        book_id = request.data.get('book')
        book = get_object_or_404(Book, id=book_id, available=True)
        rental = Rental.objects.create(user=request.user, book=book)
        book.available = False
        book.save()
        return Response(RentalSerializer(rental).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        rental = get_object_or_404(Rental, id=pk, user=request.user, returned_at__isnull=True)
        rental.returned_at = timezone.now()
        rental.save()
        rental.book.available = True
        rental.book.save()
        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)