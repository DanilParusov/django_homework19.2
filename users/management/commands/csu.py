from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='danil@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            verification_code='123',
            email_verify=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()

