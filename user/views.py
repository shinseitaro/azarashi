from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from django.conf import settings
from allauth.account.views import ConfirmEmailView
from rest_auth.registration.serializers import VerifyEmailSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
from allauth.account.models import EmailConfirmationHMAC
from django.utils.translation import ugettext_lazy as _
from django.http import Http404, HttpResponseRedirect
import urllib.parse


class GithubLoginView(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.GITHUB_CALLBACK_URL
    client_class = OAuth2Client

# このqiitaのまとめが素晴らしい。https://qiita.com/fumuumuf/items/e39eb99524c4b234b019
# 基本的にはallauth.account.views.ConfirmEmailViewを継承したViewをカスタムで作る。
class CustomConfirmEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def get_optional_params(self, confirmation: EmailConfirmationHMAC):
        return {}

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=kwargs)
        try:
            serializer.is_valid(raise_exception=True)
            self.kwargs['key'] = serializer.validated_data['key']
            confirmation = self.get_object()
            confirmation.confirm(self.request)
            params = {'detail': _('ok'), 'status': status.HTTP_200_OK}
            params.update(self.get_optional_params(confirmation))

        except ValidationError as e:
            params = {'detail': _('Invalid input.'), 'status': e.status_code}
        except Http404:
            params = {'detail': _('Invalid input.'), 'status': status.HTTP_404_NOT_FOUND}

        # Front サーバーへリダイレクト.
        url = 'http://localhost:3000/complete_sign_up'
        # クエリパラメータに認証結果を付与
        url = '{}?{}'.format(url, urllib.parse.urlencode(params))
        return HttpResponseRedirect(redirect_to=url)
