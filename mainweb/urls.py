from django.urls import path
from .import views

app_name = 'mainweb'
urlpatterns =[


path("", views.homeview, name='homepage'),
path('details/<str:pk_details>/', views.post_detail, name="details"),

path("reactions/", views.React, name='reactpage'),
path("biz/", views.BussinessView, name='bizpage'),

]