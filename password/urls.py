from django.urls import path
from . import views
urlpatterns = [
	path("", views.create,name="create"),
	path("list", views.list,name="list"),
	path("list/<int:id>",views.solo,name="solo"),
]