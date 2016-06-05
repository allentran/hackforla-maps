from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def basemap(request):
    return render_to_response('maps/test.html', {}, RequestContext(request))