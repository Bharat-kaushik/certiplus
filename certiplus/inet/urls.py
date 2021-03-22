from django.urls import path,include
from . import views
from inet.views import home,base

urlpatterns = [
    path('basic',base.basic),
    path('',home.Home),

]
