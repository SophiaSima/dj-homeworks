# python manage.py import_books
import json
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                new_book = Book.objects.create(
                    name=item['fields']['name'],
                    author=item['fields']['author'],
                    pub_date=item['fields']['pub_date']
                )