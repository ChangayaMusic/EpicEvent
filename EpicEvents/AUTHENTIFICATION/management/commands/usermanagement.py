from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Perform CRUD operations on users'

    def add_arguments(self, parser):
        parser.add_argument('operation', choices=[
                            'create', 'read', 'update', 'delete'])

    def handle(self, *args, **options):
        operation = options['operation']

        if operation == 'create':
            self.create_user()
        elif operation == 'read':
            self.read_user()
        elif operation == 'update':
            self.update_user()
        elif operation == 'delete':
            self.delete_user()

    def create_user(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        email = input('Enter email: ')

        User.objects.create_user(
            username=username, password=password, email=email)
        self.stdout.write(self.style.SUCCESS('User created successfully!'))

    def read_user(self):
        username = input('Enter username: ')
        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS(
                f'User found: {user.username}, {user.email}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found'))

    def update_user(self):
        username = input('Enter username to update: ')
        try:
            user = User.objects.get(username=username)
            new_email = input('Enter new email: ')
            user.email = new_email
            user.save()
            self.stdout.write(self.style.SUCCESS(
                f'User updated successfully!'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found'))

    def delete_user(self):
        username = input('Enter username to delete: ')
        try:
            user = User.objects.get(username=username)
            user.delete()
            self.stdout.write(self.style.SUCCESS(
                f'User deleted successfully!'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found'))
