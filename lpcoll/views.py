from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from .models import Transit


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'transits'

    def get_queryset(self):
        """Return the last five published questions."""
        return Transit.objects.order_by('-transit_date')[:5]


class TransitsView(generic.ListView):
    template_name = 'transits.html'
    context_object_name = 'transits'

    def get_queryset(self):
        """Return the last five published questions."""
        return Transit.objects.order_by('-transit_date')


def addTransit(request):
    Transit.add(
        license_plate=request.POST['license_plate'],
        car_brand=request.POST['license_plate'],
        car_model=request.POST['car_model'],
        location=request.POST['location'])

    return HttpResponseRedirect(reverse('transits'))
