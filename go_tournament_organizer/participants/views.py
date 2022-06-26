from django.shortcuts import render

from django.http import HttpResponse

from .models import Participant


def index(request):
    participants_ordered_by_strength = Participant.objects.order_by('strength_number')
    output = '\n '.join([p.name + " " + str(p.strength_number) + p.strength_type for p in participants_ordered_by_strength])
    return HttpResponse(output)

def detail(request, participant_id):
    return HttpResponse("This is participant %s." % participant_id)
