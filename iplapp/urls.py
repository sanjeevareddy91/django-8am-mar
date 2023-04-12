
from django.urls import path,re_path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MINIIPL API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
    path('team_name_api/',views.team_name_api),
    path('team_name_api/<id>/',views.team_update_delete_api),
    path('team_name_api_serializer/',views.team_name_api_serializer),
    path('team_name_api_serializer/<id>/',views.team_update_delete_api_serializer),
    path('team_name_cls_api/',views.TeamNameAPIView.as_view()),
    path('team_name_cls_detail_api/<id>/',views.TeamNameDetailAPIView.as_view()),
    path('team_name_create_list_api/',views.TeamNameCreateListAPIView.as_view()),
    path('team_name_list_api/',views.TeamNameListAPIView.as_view()),
    path('team_name_retrieve_api/<pk>/',views.TeamNameRetrieveAPIView.as_view()),
    path('team_name_retrieve_update_destroy/<pk>/',views.TeamNameRetrieveUpdateDestroyAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
