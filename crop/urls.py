from django.urls import path
from crop import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('<str:area>/<int:element>/<int:item>/<int:year>',views.CropAPIView.as_view()),
]
