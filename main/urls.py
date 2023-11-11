from django.urls import path
from . import views


urlpatterns = [
    path('index.html',views.index,name='index'),
    path('add_client',views.add_client,name='add_client'),
    path('client.html',views.client,name='client'),
    path('delete_client/<int:myid>/',views.delete_client,name='delete_client'),
    path('editclient/<int:myid>/',views.edit_client,name='edit_client'),
    path('update_client/<int:myid>/',views.update_client,name='update_client'),
    # path('doctor.html', views.doctor, name='doctor'),
    # path('add_doctor',views.add_doctor,name='add_doctor'),
    # path('delete_doctor/<int:myid>/',views.delete_doctor,name='delete_doctor'),
    path('rendezvous.html', views.rendezvous, name='rendezvous'),
    path('add_rendezvous', views.add_rendezvous, name='add_rendezvous'),
    # path('delete_doctor/<int:myid>/', views.delete_doctor, name='delete_doctor'),

    path('consultation.html', views.consultation, name='consultation'),

    path('add_consultation',views.add_consultation,name='add_consultation'),

    path('delete_consultation/<int:myid>/', views.delete_consultation, name='delete_consultation'),



]