from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Transit

# Create your views here.

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
    t = Transit(
        license_plate=request.POST['license_plate'],
        car_brand=request.POST['car_brand'],
        car_model=request.POST['car_model'],
        location=request.POST['location'],
        transit_date=timezone.now()
    )
    t.save()

    return HttpResponseRedirect(reverse('index'))
