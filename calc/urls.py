from django.urls import path
from .views import Calc

app_name = "calc"
urlpatterns = [
	path('', Calc, name='calc'),
]

