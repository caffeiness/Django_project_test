from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'user'

urlpatterns = {
    path('home/',views.HomeView.as_view(),name='home'),
}