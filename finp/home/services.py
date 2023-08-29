from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login


class UserService(AbstractUser):


    @staticmethod
    def user_authentication(request, user, password):
        user = authenticate(request, username=user, password=password)

        if user:
            login(request, user)

            return True
        
        else:
            return False