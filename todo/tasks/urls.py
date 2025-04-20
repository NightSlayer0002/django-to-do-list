from django.urls import path
from . import views

urlpatterns = [      #a list
	path('', views.index, name="list"),     #will trigger the HttpResponse in views     
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),

]
