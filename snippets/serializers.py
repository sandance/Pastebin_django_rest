__author__ = 'nazmul'
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """
    Model Serializer is nothing magical , they are simply shortcut for creating serializer class
    """
    class Meta:
        model = Snippet
        fields = ('id' , 'title', 'code', 'linenos', 'language', 'style')


