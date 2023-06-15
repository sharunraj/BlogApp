from django.urls import path
from pyblogapp import views

urlpatterns = [
    path('home', views.project_view, name='project_view'),
    path('newpost', views.newpost_view, name='newpost_view'),
    path('addpost',views.addpost_view,name='addpost_view'),
    path('delete/<int:pk>/', views.delete_project, name="delete_project"),
]