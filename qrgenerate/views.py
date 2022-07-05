import imp
from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import Qrcode
from rest_framework.authentication import BasicAuthentication
from .serializer import Qrserilizer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def qr_code(request):
    if request.method ==  'GET':
        prod = Qrcode.objects.all()
        serilizer = Qrserilizer(prod,many = True)
        return Response(serilizer.data,status = status.HTTP_200_OK)

    if request.method == 'POST':
        serilizer = Qrserilizer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)

    
