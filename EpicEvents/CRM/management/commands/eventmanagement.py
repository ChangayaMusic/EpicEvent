from django.core.management.base import BaseCommand
from AUTHENTIFICATION.models import Event, Customer, Contract

class Command(BaseCommand):
    help = 'Perform CRUD operations on events'

    def add_arguments(self, parser):
        parser.add_argument('operation', choices=['create', 'read', 'update', 'delete'])

    def handle(self, *args, **options):
        operation = options['operation']

        if operation == 'create':
            self.create_event()
        elif operation == 'read':
            self.read_event()
        elif operation == 'update':
            self.update_event()
        elif operation == 'delete':
            self.delete_event()

    def create_event(self):
        customer_id = input('Enter customer ID: ')
        try:
            customer = Customer.objects.get(id=customer_id)
            contract_id = input('Enter contract ID: ')
            try:
                contract = Contract.objects.get(id=contract_id)
                # Implement logic to get other event details
                Event.objects.create(customer=customer, event_status=contract, attendees=0)  # Example fields, update
