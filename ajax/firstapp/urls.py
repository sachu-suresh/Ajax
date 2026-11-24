from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('add_items', views.add_items,name="add_items"),
    path('get_items', views.get_items,name="get_items"),
    path('edit_item', views.edit_item,name="edit_item"),
    path('update_item', views.update_item,name="update_item"),
    path('delete_item', views.delete_item,name="delete_item"),
    

    
    
    

]