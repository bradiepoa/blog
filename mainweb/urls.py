from django.urls import path
from .import views

app_name = 'mainweb'
urlpatterns =[


path("", views.homeview, name='homepage'),
path('details/<str:pk_details>/', views.post_detail, name="details"),

path("reactions/", views.React, name='reactpage'),
path("biz/", views.BussinessView, name='bizpage'),
path("sports/", views.sportview, name='sportpage'),
path("politics/", views.politicsview, name='politicspage'),
path("education/", views.educationview, name="educationpage"),
path("business/", views.businessview, name="businesspage"),
path("science/", views.scienceview, name="sciencepage"),
path("health/", views.healthview, name="healthpage"),

]
