from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Participants


def index(request):
    participants_list = Participants.objects.order_by('dob')
    context = {'participants_list': participants_list}
    return render(request, 'organizer/index.html', context)


def detail(request, participants_id):
    participants = get_object_or_404(Participants, pk=participants_id)
    return render(request, 'organizer/details_participants.html', {'participants': participants})


def participants(request, participants_id):
    response = "Der Status des Teilnehmers %s ist:"
    return HttpResponse(response % participants_id)
