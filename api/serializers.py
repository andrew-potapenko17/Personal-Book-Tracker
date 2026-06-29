from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        status = data.get('status', getattr(self.instance, 'status', None))
        rating = data.get('rating', getattr(self.instance, 'rating', None))

        if rating is not None and status != 'finished':
            raise serializers.ValidationError({
                'rating': 'Rating is only allowed when status is finished.'
            })

        return data