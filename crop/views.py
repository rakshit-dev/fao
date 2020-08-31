from django.shortcuts import render
# from rest_framework import viewsets
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from crop.utils import url, headers
import requests
import json

# Create your views here.


class CropAPIView(APIView):
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    def get(self, request, area, element, item, year):
        params = {
            "area": area,
            "area_cs": "fao",
            "element": element,
            "item": item,
            "item_cs": "fao",
            "year": year,
            "show_codes": True,
            "show_unit": True,
            "show_flags": True,
            "null_values": False,
            "output_type": "objects"
        }
        response = requests.get(url, params=params, headers=headers)
        data = json.loads(response._content)
        return Response(data["data"])
