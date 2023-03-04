from django.db import migrations
from django.contrib.auth.models import User


def create_admin(apps, schema_editor):
    # Crée un nouvel utilisateur avec l'adresse e-mail et le mot de passe spécifiés
    User.objects.create_user('admin', None, '&zND4!96pA*dHR%9r86z')


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
