from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('blogs/',views.blogs, name='blogs'),
    path('contact/',views.contact, name='contact'),
    path('contact1/',views.contact1, name='contact1'),
    
   
]