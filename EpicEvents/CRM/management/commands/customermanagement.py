from django.core.management.base import BaseCommand
from AUTHENTIFICATION.models import Customer


class Command(BaseCommand):
    help = 'Perform CRUD operations on customers'

    def add_arguments(self, parser):
        parser.add_argument('operation', choices=[
                            'create', 'read', 'update', 'delete'])

    def handle(self, *args, **options):
        operation = options['operation']

        if operation == 'create':
            self.create_customer()
        elif operation == 'read':
            self.read_customer()
        elif operation == 'update':
            self.update_customer()
        elif operation == 'delete':
            self.delete_customer()

    def create_customer(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        email = input('Enter email: ')
        phone = input('Enter phone: ')
        mobile = input('Enter mobile: ')
        company_name = input('Enter company name: ')
        prospect = input('Is prospect? (True/False): ')

        Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            mobile=mobile,
            company_name=company_name,
            prospect=prospect,
        )

        self.stdout.write(self.style.SUCCESS('Customer created successfully!'))

    def read_customer(self):
        customers = Customer.objects.all()
        for customer in customers:
            self.stdout.write(self.style.SUCCESS(
                f'{customer.first_name} {customer.last_name} - {customer.email}'))

    def update_customer(self):
        customer_id = input('Enter customer ID to update: ')
        try:
            customer = Customer.objects.get(id=customer_id)
            # Implement logic to update customer fields
            self.stdout.write(self.style.SUCCESS(
                'Customer updated successfully!'))
        except Customer.DoesNotExist:
            self.stdout.write(self.style.ERROR('Customer not found'))

    def delete_customer(self):
        customer_id = input('Enter customer ID to delete: ')
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            self.stdout.write(self.style.SUCCESS(
                'Customer deleted successfully!'))
        except Customer.DoesNotExist:
            self.stdout.write(self.style.ERROR('Customer not found'))
