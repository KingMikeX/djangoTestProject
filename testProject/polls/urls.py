from django.urls import path
from . import views

# Beschreibe hier die Url Call's über die der Client die die Views ansprechen kann

urlpatterns = [
    path("", views.index, name="index"),
]