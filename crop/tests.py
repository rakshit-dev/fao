from django.test import TestCase
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .utils import headers
import requests

#TODO: Make this url configurable 
url = "http://fenixservices.fao.org/faostat/api/v1/en/data/QC"


class cropDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        self.url = self.url = reverse("crops:crops", args=[3, 2510, 515, 1961])

    def test_pet_object_bundle(self):
        """
        Test to verify Pet object bundle
        """
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 200)
