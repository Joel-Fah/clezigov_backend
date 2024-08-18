from django.contrib.auth.hashers import check_password

from authentication.models import CustomUser


def authenticate(email=None, password=None):
    try:
        # Get the corresponding user.
        user = CustomUser.objects.get(email=email)
        #  If password, matches just return the user. Otherwise, return None.
        if check_password(password, user.email):
            return user
        return None
    except CustomUser.DoesNotExist:
        # No user was found.
        return None
