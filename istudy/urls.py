from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('account/',include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('accounts/register/', views.signup, name='signup'),
    path('accounts/customregister/', views.customSignup, name='customsignup'),
    path('logout/', auth_views.LogoutView.as_view(), {"next_page": '/'}),
    path('customusers/',views.customuserList.as_view()),
    path('users/',views.usersList.as_view()),
    path('api/register/', views.registration_view, name='register'),
    # path('api/customregister/', views.custom_registration_view, name='register'),
    path('api/login/', obtain_auth_token, name='login'),



 

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)