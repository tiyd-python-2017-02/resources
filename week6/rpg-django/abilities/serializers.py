from rest_framework import serializers
from .models import Ability, Task


class AbilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ability
        fields = ('url', 'name', 'damage', 'icon', 'rarity')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'description')
