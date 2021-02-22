from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url('account/',include('django.contrib.auth.urls')),
    url('', views.index, name='index'),
    url('accounts/register/', views.signup, name='signup'),
    url('accounts/customregister/', views.customSignup, name='customsignup'),
    url('logout/', auth_views.LogoutView.as_view(), {"next_page": '/'}),
    url('customusers/',views.customuserList.as_view()),
    url('users/',views.usersList.as_view()),
    url('api/register/', views.registration_view, name='register'),
    url('api/login/', obtain_auth_token, name='apilogin'),
    



 

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)