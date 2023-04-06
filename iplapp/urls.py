
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
    path('delete_team/<id>',views.delete_team,name="delete_team"),
    path('model_add_team/',views.model_add_team,name="model_add_team"),
    path('normal_add_team/',views.normal_add_team,name="normal_add_team"),
    path('',views.register_user,name="register_user"),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('email_check/',views.forgot_password_email_check,name="forgot_password_email_check"),
    path('verify_otp/',views.verify_otp,name="verify_otp"),
    path('change_password/<pk>',views.change_password,name="change_password"),
    # class based urls
    path('cbv_hello/',views.HelloCBV.as_view(),name="cbv_hello"),
    path('cbv_register_team/',views.RegisterTeamCBV.as_view(),name="cbv_register_team"),
    path('cbv_list_team/',views.ListTeamCBV.as_view(),name="cbv_list_team"),
    path('cbv_update_team/<pk>',views.UpdateTeamCBV.as_view(),name="cbv_update_team"),
    path('cbv_detail_team/<pk>',views.DetailTeamCBV.as_view(),name="cbv_detail_team"),

    # rest-framework urls
    path('hello_api/',views.hello_api),
]
