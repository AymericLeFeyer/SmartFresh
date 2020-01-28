from django.http import HttpResponse
from django.template import loader
from tablib import Dataset
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

def containerByName(request, container_name):
    try:
        c = Container.objects.get(numContainer=container_name)
        template = loader.get_template('SmartFreshApp/detailsContainer.html')
        context = {
            'c': c,
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

def simple_upload(request):
    if request.method == 'POST':
        template = loader.get_template('SmartFreshApp/simple_upload.html')

        container_resource = Container()
        dataset = Dataset()
        new_container = request.FILES['myfile']

        imported_data = dataset.load(new_container.read())
        result = container_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            container_resource.import_data(dataset, dry_run=False)
        
    return template.render(request)
