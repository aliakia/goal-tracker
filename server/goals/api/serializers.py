from rest_framework import serializers
from ..models import Person
from ..choices import GENDER_CHOICES

class GenderChoiceFieldSerializer(serializers.Field):
    def to_representation(self, obj):
        return dict(GENDER_CHOICES)[obj]
    
    def to_internal_value(self, data):
        return data

class PersonSerializers(serializers.ModelSerializer):
    gender = GenderChoiceFieldSerializer()
    created = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'gender',
            'age',
            'favorite_num',
            'created'
        )

    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')