from rest_framework import serializers
from demo.models import Demo

class DemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demo
        fields = "__all__"