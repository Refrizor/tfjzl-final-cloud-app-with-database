from __future__ import annotations

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from onlinecourse.models import Instructor


class Command(BaseCommand):
    help = "Dev seeder: creates dev user, admin user, and instructor."

    def handle(self, *args, **options):
        User = get_user_model()

        # ---- Dev user (you) ----
        dev_user, dev_created = User.objects.get_or_create(
            username="dev",
            defaults={
                "email": "dev@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if dev_created:
            dev_user.set_password("123")
            dev_user.save()
            self.stdout.write(self.style.SUCCESS("Created dev user"))
        else:
            self.stdout.write("Dev user already exists")

        # ---- Admin superuser ----
        admin_user, admin_created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if admin_created:
            admin_user.set_password("admin12345")
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Created admin superuser"))
        else:
            self.stdout.write("Admin user already exists")

        # ---- Instructor tied to admin ----
        instructor, instructor_created = Instructor.objects.get_or_create(
            user=admin_user,
            defaults={
                "full_time": True,
                "total_learners": 35,
            },
        )
        if instructor_created:
            self.stdout.write(self.style.SUCCESS("Created instructor for admin"))
        else:
            self.stdout.write("Instructor already exists for admin")
