
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from allauth.utils import email_address_exists
from allauth.account.utils import setup_user_email
from allauth.account import app_settings as allauth_settings

# Get the User model
UserModel = get_user_model()

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'email', 'name')
        read_only_fields = ('email', )

