
from django.urls import path
from myapp import views
urlpatterns = [
    path('home', views.project_view,name='project_view'),
    path('login', views.login_view,name='login_view'),
    path('adddetails',views.adddetails_view,name='adddetails_view'),
    path('viewdetails',views.viewdetails,name='viewdetails'),
    path('<int:pk>/',views.getsinglestudents,name='getsinglestudents'),

]
