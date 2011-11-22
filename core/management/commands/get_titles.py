from django.core.management.base import BaseCommand, CommandError
from core.models import Video
from lxml.html import parse


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        for v in Video.objects.all():
            u = parse(v.source_url)
            print(u.find(".//title").text)
