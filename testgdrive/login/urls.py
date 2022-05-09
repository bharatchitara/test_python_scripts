from django import urls
from django.urls import include, path, re_path
from login import views
 
urlpatterns = [
    path("test",views.test),
    re_path(r'test_user2/',views.test_user2),
    
    
]
