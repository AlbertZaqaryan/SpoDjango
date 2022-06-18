from django.urls import path
from .views import  HomepageListView, contact

urlpatterns = [
   path('', HomepageListView.as_view(), name='index'),
   path('contact/', contact, name='contact')
]