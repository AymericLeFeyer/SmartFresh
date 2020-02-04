from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

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


class SearchView(ListView):
    model = Container
    template_name = 'SmartFreshApp/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Container.objects.filter(numContainer__contains=query)
            result = postresult
        else:
            result = None
        return result
