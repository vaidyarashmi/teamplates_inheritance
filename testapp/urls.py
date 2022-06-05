from django.urls import path,include
from testapp import views
urlpatterns = [
    path('blue_print', views.blue_print,name='blue_print'),
    path('home', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    
]
