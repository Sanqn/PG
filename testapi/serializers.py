from rest_framework import serializers
from .models import NewPerson


class NewPersonHeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewPerson
        fields = ('id', 'first_name', 'last_name', 'email', 'work_experience')
        lookup_field = 'first_name'
        extra_kwargs = {
            'url': {'lookup_field': 'first_name'}
        }