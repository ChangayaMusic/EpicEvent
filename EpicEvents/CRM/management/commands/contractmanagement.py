from django.core.management.base import BaseCommand
from AUTHENTIFICATION.models import Contract, Customer

class Command(BaseCommand):
    help = 'Perform CRUD operations on contracts'

    def add_arguments(self, parser):
        parser.add_argument('operation', choices=['create', 'read', 'update', 'delete'])

    def handle(self, *args, **options):
        operation = options['operation']

        if operation == 'create':
            self.create_contract()
        elif operation == 'read':
            self.read_contract()
        elif operation == 'update':
            self.update_contract()
        elif operation == 'delete':
            self.delete_contract()

    def create_contract(self):
        customer_id = input('Enter customer ID: ')
        try:
            customer = Customer.objects.get(id=customer_id)
            # Implement logic to get other contract details
            Contract.objects.create(customer=customer, status=False)  # Example fields, update as needed
            self.stdout.write(self.style.SUCCESS('Contract created successfully!'))
        except Customer.DoesNotExist:
            self.stdout.write(self.style.ERROR('Customer not found'))

    def read_contract(self):
        contracts = Contract.objects.all()
        for contract in contracts:
            self.stdout.write(self.style.SUCCESS(f'Contract {contract.id} for {contract.customer} - Status: {contract.status}'))

    def update_contract(self):
        contract_id = input('Enter contract ID to update: ')
        try:
            contract = Contract.objects.get(id=contract_id)
            # Implement logic to update contract fields
            self.stdout.write(self.style.SUCCESS('Contract updated successfully!'))
        except Contract.DoesNotExist:
            self.stdout.write(self.style.ERROR('Contract not found'))

    def delete_contract(self):
        contract_id = input('Enter contract ID to delete: ')
        try:
            contract = Contract.objects.get(id=contract_id)
            contract.delete()
            self.stdout.write(self.style.SUCCESS('Contract deleted successfully!'))
        except Contract.DoesNotExist:
            self.stdout.write(self.style.ERROR('Contract not found'))