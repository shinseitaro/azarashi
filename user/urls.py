from django.conf.urls import url
from django.urls import include, path

from .views import CustomConfirmEmailView

urlpatterns = [
    url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', CustomConfirmEmailView.as_view(),
        name='account_confirm_email'),

    # rest_auth.registration の urls を追加
    path('', include('rest_auth.registration.urls')),

]
