from django.urls import path,include
from . import views
from inet.views import home,base,Grow_with_us,subgrowdetails, details_section_view

urlpatterns = [
    path('basic',base.basic),
    path('',details_section_view.fetch_category_items),
    path('SubGrow/<int:section>',Grow_with_us.SubGrow),
    path('SubGrowdetails/<int:sub_section>',subgrowdetails.SubGrowDetails)

]
