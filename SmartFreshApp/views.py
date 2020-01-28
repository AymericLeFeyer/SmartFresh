from django.http import HttpResponse
from django.template import loader
from .models import Container

def container(request, container_id):
    try:
        c = Container.objects.get(numLot=container_id)
        template = loader.get_template('SmartFreshApp/detailsContainer.html')
        context = {
            'c': c,
        }
        output = template.render(context, request)
    except Exception:
        output = "No container with numLot = " + str(container_id)
    
    return HttpResponse(output)

def allContainers(request):
    try:
        containerList = Container.objects.order_by('numLot')
        template = loader.get_template('SmartFreshApp/index.html')
        context = {
            'containerList': containerList,
        }
        output = template.render(context, request)
    except Exception as e:
        output = e
    
    return HttpResponse(output)