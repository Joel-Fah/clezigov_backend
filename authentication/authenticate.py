from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        # Allow authentication with both email and username
        try:
            user = UserModel.objects.get(email=username)  # Try to get the user by email
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(username=username)  # Try to get the user by username
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
