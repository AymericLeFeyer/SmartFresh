from django.http import HttpResponse
from .models import Container


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def container(request, container_id):
    try:
        c = Container.objects.get(numLot=container_id)
        output = str(c.numLot) + ' ' + str(c.numContainer)
    except Exception:
        output = "No container with numLot = " + str(container_id)
    
    return HttpResponse(output)

def allContainers(request):
    try:
        containerList = Container.objects.order_by('numLot')
        output = '\n'.join([str(c) for c in containerList])
    except Exception as e:
        output = e
    
    return HttpResponse(output)