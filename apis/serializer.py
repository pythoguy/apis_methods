from rest_framework import serializers
from apis.models import *

class dataserlizer(serializers.ModelSerializer):
    class Meta:
        model = database
        fields = '__all__'
