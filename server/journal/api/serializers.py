from rest_framework import serializers
from ..models import Journal

class JournalSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Journal
        fields = (
            'id',
            'title',
            'date',
            'mood',
            'entry',
        )

    def date(self, obj):
        return obj.date.strftime('%Y-%m-%d %H:%M:%S')