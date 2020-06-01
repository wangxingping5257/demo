# coding: utf-8

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, ModelSerializer
from client import models
from rest_framework.exceptions import ValidationError


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = models.ClientScore
        fields = ['client_name', 'client_score']

    def validate_client_score(self, client_score):
        if int(client_score) < 1 or int(client_score) > 10000000:
            raise ValidationError("client_score只支持1~10000000")
        return client_score

    def save(self, **kwargs):
        validated_data = dict(self.validated_data)
        client_name = validated_data.pop("client_name")
        models.ClientScore.objects.update_or_create(state=1, client_name=client_name, defaults=validated_data)

