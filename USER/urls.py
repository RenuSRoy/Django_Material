from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('Next/',views.Next,name="Next"),
    path('Third_Page/',views.Third_Page,name="Third_Page")
]
