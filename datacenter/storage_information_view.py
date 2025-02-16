from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.view_utilities import format_duration


def storage_information_view(request):
    in_storage_now = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in in_storage_now:
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration()),
        }
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
