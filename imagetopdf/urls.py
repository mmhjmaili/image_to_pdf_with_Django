from django.urls import path
from . import views

app_name= 'imagetopdf'

urlpatterns = [
    path('convert/', views.convert_image_to_pdf, name='convert_image_to_pdf'),
]
