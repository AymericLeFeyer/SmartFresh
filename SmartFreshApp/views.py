from django.http import HttpResponse
from django.template import loader

from .models import Container, Score


def container(request, container_id):
    try:
        c = Container.objects.get(numLot=container_id)
        s = Score.objects.filter(numLot=c.numLot)
        template = loader.get_template('SmartFreshApp/detailsContainer.html')
        context = {
            'c': c,
            's': s,
        }
        output = template.render(context, request)
    except Exception:
        output = "No container with numLot = " + str(container_id)

    return HttpResponse(output)


def containerByName(request, container_name):
    try:
        c = Container.objects.get(numContainer=container_name)
        s = Score.objects.get(numLot=c.numLot)
        template = loader.get_template('SmartFreshApp/detailsContainer.html')
        context = {
            'c': c,
            's': s,
        }
        output = template.render(context, request)
    except Exception:
        output = "No container with numContainer = " + str(container_name)

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


def homepage(request):
    template = loader.get_template('SmartFreshApp/homepage.html')
    return HttpResponse(template.render({}, request))


def research(request):
    if request.method == 'GET':
        form = request.GET['form']
        if form == '':
            containers = Container.objects.all()
        else:
            containers = Container.objects.filter(numContainer__contains=form)
    else:
        containers = Container.objects.all()
    template = loader.get_template('SmartFreshApp/index.html')
    context = {
        'containerList': containers,
    }
    return HttpResponse(template.render(context, request))
