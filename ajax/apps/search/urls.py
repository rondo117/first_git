from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),  
    url(r'^add$', views.add),  
    url(r'^fetch$', views.fetch),  
    url(r'^fetch$', views.fetch),  
    url(r'^search$', views.search),  
    url(r'^filter$', views.filter),  
]                            
