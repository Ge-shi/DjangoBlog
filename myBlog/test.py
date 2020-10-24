from django.contrib.auth.models import User
user = User.objects.filter(is_superuser = True)
print(user)