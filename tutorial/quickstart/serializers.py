from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import FederalState


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FederalStateSerializer(serializers.ModelSerializer):
    # ModelSerializer determines the set of fields and has default create() and update() methods
    class Meta:
        model = FederalState
        fields = ['id', 'letter_code', 'spec_yield']

# long from above (does the same)
# class FederalStateSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # letter_code = serializers.CharField(required=False, allow_blank=True, max_length=2)
    # spec_yield = serializers.IntegerField()

    # def create(self, validated_data):
    #     # creates new FederalState instance from validated data
    #     return FederalState.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # updates the given instance with the validated data
    #     instance.letter_code = validated_data.get('letter_code', instance.title)
    #     instance.spec_yield = validated_data.get('spec_yield', instance.spec_yield)
    #     instance.save()
    #     return instance
