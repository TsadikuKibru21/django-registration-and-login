from . import views

from django.urls import path

urlpatterns = [
 
    path('',views.aa,name='aa'),
    path('',views.Dean,name='Dean'),
    path('',views.Vice,name='Vice'),
    path('',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('add_item/',views.add_item,name='add_item'),
    #path('delete_item/<int:myid>/',views.delete_item,name='delete_item'),
    # path('edit_item/<int:myid>/',views.edit_item,name='edit_item'),
    # path('update_item/<int:myid>/',views.update_item,name='update_item'),
   
]