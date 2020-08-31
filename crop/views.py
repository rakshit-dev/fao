from django.shortcuts import render
# from rest_framework import viewsets
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from crop.utils import url, headers
import requests
import json

import logging as logger


class CropAPIView(APIView):
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    def get(self, request, area, element, item, year):
        logger.info("Getting list of crops")
        try:
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
            return Response(data["data"], status=200)
        except Exception as ex:
            logger.error(ex)
        return Response(data=json.dumps({"error": "Something went wrong"}), status=500)
