from django.urls import path
from facebook import views

#facebook in my app name

urlpatterns = [
path('about/',views.about,name='aboutlink')

]