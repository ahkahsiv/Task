from django.urls import path
from . import views

urlpatterns = [
    path('',views.form),
    path('write/',views.write),
    path('add_vish/',views.add_vish)
]
