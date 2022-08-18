from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import get_object_or_404

from .utils import salty_code_hasher

User = get_user_model()


class ConfirmationCodeBackend(ModelBackend):
    def authenticate(self, request, username=None, confirmation_code=None):
        user = get_object_or_404(User, username=username)
        if not user.code.value == salty_code_hasher(confirmation_code):
            raise AttributeError('Code mismatch')
        return user
