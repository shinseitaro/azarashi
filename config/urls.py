# from django.contrib import admin
from django.contrib.gis import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from user.views import GithubLoginView, TwitterLoginView, FetchTokenView
from rest_framework_jwt.views import obtain_jwt_token
from user import urls as user_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('v1.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include(user_url)),
    path('rest-auth/github/', GithubLoginView.as_view(), name='github_login'),
    path('rest-auth/twitter/', TwitterLoginView.as_view(), name='twitter_login'),
    path('api-token-auth/', obtain_jwt_token),
    path('token/', FetchTokenView.as_view(), name='token'),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
