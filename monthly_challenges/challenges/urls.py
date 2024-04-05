from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("<int:month>",views.monthly_challenges_number),
    path("<str:month>", views.monthly_challenges,name="monthly_challenge")
]