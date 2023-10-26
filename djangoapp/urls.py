from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addeducation',views.addeducation,name='addeducation'), 
    path('alluser',views.alluser,name='alluser'), 
    path('editData/<int:id>',views.editData,name='editData'),
    path('updateData/<int:id>/',views.updateData,name='updateData'),
]