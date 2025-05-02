
# create_superuser.py
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="htech").exists():
    User.objects.create_superuser("htech", "htech", "azertyuiop")
