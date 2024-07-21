from rest_framework import serializers
from ..models import Jogs
from ..choices import DIFFICULTY_CHOICES


class DifficultyChoiceFieldSerializer(serializers.Field):
    def to_representation(self, obj):
        return dict(DIFFICULTY_CHOICES)[obj]
    
    def to_internal_value(self, data):
        return data
    
class JogsSerializer(serializers.ModelSerializer):
    difficulty = DifficultyChoiceFieldSerializer()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Jogs
        fields = (
            'id',
            'place',
            'distance',
            'duration',
            'date',
            'difficulty',
        )

    def date(self, obj):
        return obj.date.strftime('%Y-%m-%d %H:%M:%S')