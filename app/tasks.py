from celery import shared_task
from django.core.management import call_command

@shared_task
def fetch_navica_data_task():
    call_command('fetch_navica_data_from_api')