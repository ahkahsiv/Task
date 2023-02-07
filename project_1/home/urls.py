from django.urls import path
from . import views

urlpatterns = [
    path('',views.form),
    path('add/',views.add),
    path('csv/',views.write_csv),
    path('text/',views.write_text),
    path('pdf/',views.write_pdf),
    path('new/',views.new),


]
