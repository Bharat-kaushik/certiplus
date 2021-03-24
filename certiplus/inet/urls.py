from django.urls import path,include
from . import views
from inet.views import home,base,Grow_with_us

urlpatterns = [
    path('basic',base.basic),
    path('',home.Home),
    path('SubGrow/<int:section>', Grow_with_us.SubGrow)

]
