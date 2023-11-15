from datetime import timedelta

from celery import shared_task

from django.utils import timezone

from drifters.models import Wormhole


@shared_task
def garbage_collection():
    for wormhole in Wormhole.objects.filter(created_at__lte=timezone.now() - timedelta(hours=16)):
        wormhole.set_archived()

    for wormhole in Wormhole.objects.filter(lifetime=Wormhole.Lifetime.EOL,
                                            eol_changed_at__lte=timezone.now() - timedelta(hours=4)):
        wormhole.set_archived()

    for wormhole in Wormhole.objects.filter(lifetime__in=[Wormhole.Lifetime.DECAY, Wormhole.Lifetime.FRESH],
                                            created_at__lte=timezone.now() - timedelta(hours=12)):
        wormhole.set_eol()
