from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, ProfileListAPI, UserListAPI, CreateProfileAPI

from rest_framework.routers import DefaultRouter
from knox import views as knox_views

router = DefaultRouter()
router.register('userlist', UserListAPI, 'userlist')
router.register('profilelist', ProfileListAPI, 'userlist')

urlpatterns = [
    path('api/auth/', include('knox.urls')), 
    path('api/auth/', include(router.urls)), # userlist - viewset
    path('api/auth/register/', RegisterAPI.as_view()),
    path('api/auth/profile/create', CreateProfileAPI.as_view()),
    path('api/auth/users/', UserAPI.as_view()),
    path('api/auth/login/', LoginAPI.as_view()),
    #로그아웃 - 토큰을 사라지게 한다. 
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name = 'knox_logout')
]