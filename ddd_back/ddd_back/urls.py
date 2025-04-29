"""
URL configuration for ddd_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.api.rest.authentication_rest_controller import AuthenticationRestController
from apps.api.rest.country_rest_controller import CountryRestController
from apps.api.rest.song_rest_controller import SongRestController
from apps.api.rest.user_rest_controller import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', obtain_auth_token, name='api_token_auth'),
    path('api/auth/logout/', AuthenticationRestController.as_view({'delete': 'delete'}), name='delete'),
    path('api/auth/groups', AuthenticationRestController.as_view({'get': 'get_user_groups'}), name='get_user_groups'),
    
    path('api/countries/', CountryRestController.as_view({'get': 'get'})),
    path('api/countries/names', CountryRestController.as_view({'get': 'get_names'})),
    path('api/countries/<str:country>/songs/', CountryRestController.as_view({'get': 'get_songs'}), name='get_songs'),
    
    path('api/songs/generate-playlist', SongRestController.as_view({'post': 'generate_playlist'}), name='generate_playlist'),

    path('api/users/', UserViewSet.as_view({'get': 'list'}), name='user_list'),
    path('api/users/<int:pk>/', UserViewSet.as_view({'delete': 'destroy'}), name='user_detail'),
]
