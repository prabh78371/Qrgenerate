from click import style
from .models import Qrcode
from rest_framework import serializers

class Qrserilizer(serializers.ModelSerializer):
    class Meta:
        model = Qrcode
        fields = '__all__'