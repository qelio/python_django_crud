import random
from faker import Faker
from django.db import transaction
from .models import Author

fake = Faker()


def gentestdata():
    try:
        with transaction.atomic():
            # user = User()
            # user.username = 'user1'
            # user.set_password('pass1')
            # user.is_staff = True
            # user.is_active = True
            # user.is_superuser = True
            # user.save()
            authors = [Author.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=30, maximum_age=80),
                nationality=fake.country(),
                biography=fake.text(max_nb_chars=200)
            ) for _ in range(1000)]

            print("OK gentestdata()")
    except Exception as e:
        print(f"*** ERROR gentestdata(): {e} ***")

import os

if __name__ == "__main__":

    gentestdata()
