from django.contrib import admin
from django.urls import path
from LMS import views
from .views import user_logout
urlpatterns = [
    path('', views.Welcome, name='Welcome'),

    path('about', views.about, name='about'),


    path('contact', views.contact, name='contact'),

    path('signin', views.signin, name='signin'),
    
    path('signup', views.signup, name='signup'),
    
    path('logout', user_logout, name='logout'),
   
 path('book_list', views.book_list, name='books'),
]

