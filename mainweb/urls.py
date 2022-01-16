from django.urls import path
from .import views

app_name = 'mainweb'
urlpatterns =[


path("", views.homeview, name='homepage'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),

path("reactions/", views.React, name='reactpage'),
path("biz/", views.BussinessView, name='bizpage'),

]