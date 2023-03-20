
from django.urls import path
from . import views
urlpatterns = [
    path('hello',views.hello_world),
    path('first_page',views.first_html),
    path('first_form',views.first_form),
    path('add_team',views.add_team,name="add_team"),
    path('list_team',views.list_team,name="list_team"),
    path('single_team/<id>',views.single_team,name="single_team"),
    path('update_team/<id>',views.update_team,name="update_team"),
    path('delete_team/<id>',views.delete_team,name="delete_team")
]
