from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings


# Create your views here.
class GoogleLoginView(SocialLoginView):
    """
    View that allows users to login using Google OAuth2.0
    """

    authentication_classes = (
        []
    )  # disable authentication, make sure to override `allowed origins` in settings.py in production!
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.FRONTEND_URL  # frontend application url
    client_class = OAuth2Client
