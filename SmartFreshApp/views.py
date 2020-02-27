from django.http import HttpResponse, FileResponse
from django.template import loader
from reportlab.pdfgen import canvas
import io

from .models import Container, Score, LotBloque


def container(request, container_id):
    try:
        c = Container.objects.get(id=container_id)
        s = Score.objects.filter(numLot=c.id)
        b = LotBloque.objects.filter(numLot=c.id)
        template = loader.get_template('SmartFreshApp/detailsContainer.html')
        context = {
            'c': c,
            's': s,
            'b': b,
        }
        output = template.render(context, request)
    except Exception:
        output = "No container with numLot = " + str(container_id)

    return HttpResponse(output)


def containerByName(request, container_name):
    try:
        c = Container.objects.get(numContainer=container_name)
        s = Score.objects.get(numLot=c.id)
        b = LotBloque.objects.filter(numLot=c.id)
        template = loader.get_template('SmartFreshApp/detailsContainer.html')
        context = {
            'c': c,
            's': s,
            'b': b,
        }
        output = template.render(context, request)
    except Exception:
        output = "No container with numContainer = " + str(container_name)

    return HttpResponse(output)


def allContainers(request):
    try:
        containerListPrevious = Container.objects.all().order_by('id')
        # containerList = sorted(containerListPrevious, key=lambda c: c.withoutChar())
        containerList = containerListPrevious.order_by('id')
        template = loader.get_template('SmartFreshApp/index.html')
        context = {
            'containerList': containerList,
            'backPossible': False,
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
        option = request.GET['typeRadio']
        backPossible = False
        value = ''
        checked = 0
        if form == '':
            containers = Container.objects.all()
            backPossible = False
        else:
            if option == 'option1':
                containers = Container.objects.filter(numContainer__contains=form)
                backPossible = True
                checked = 1
            elif option == 'option2':
                containers = Container.objects.filter(id=form)
                backPossible = True
                checked = 2
            value = form
    else:
        containers = Container.objects.all()
        backPossible = False

    template = loader.get_template('SmartFreshApp/index.html')
    context = {
        'containerList': containers,
        'backPossible': backPossible,
        'checked': checked,
        'value': value,
    }
    return HttpResponse(template.render(context, request))


def create_pdf(request, container_id):
    if request.method == 'GET':
        if 'infos' in request.GET:
            info = request.GET['infos']
        else:
            info = False
        if 'score' in request.GET:
            score = request.GET['score']
        else:
            score = False
        if 'bloque' in request.GET:
            bloque = request.GET['bloque']
        else:
            bloque = False

        # If nothing is checked, imagine that everything is needed
        if not info and not score and not bloque:
            info = True
            score = True
            bloque = True

        c = Container.objects.get(id=container_id)
        if score:
            s = Score.objects.filter(numLot=c.id)
        if bloque:
            b = LotBloque.objects.filter(numLot=c.id)

        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        y = 810
        ecartLigne = 15
        alineaBase = 30
        alineaTitre = 50

        if c.isF:
            fr = "oui"
        else:
            fr = "non"

        if c.isBloque:
            bl = "oui"
        else:
            bl = "non"

        if info:
            p.drawString(alineaTitre, y, "INFORMATIONS DU CONTAINER")
            y -= ecartLigne
            p.drawString(alineaBase, y, 'Numéro du container :' + c.numContainer + ' | Lot : ' + str(c.id))
            y -= ecartLigne
            if c.commentaires:
                p.drawString(alineaBase, y, c.commentaires)
                y -= ecartLigne
            p.drawString(alineaBase, y, 'Francité : ' + fr + ' | Lot Bloqué : ' + bl)
            y -= ecartLigne

            y -= ecartLigne
        if score:
            p.drawString(alineaTitre, y, "SCORES")
            y -= ecartLigne
            for scores in s:
                p.drawString(alineaBase, y, 'Produit : '+scores.produit+' | Quantité : '+str(scores.qteAnnonce)+' | Marque : '+scores.marque)
                y -= ecartLigne
            y -= ecartLigne

        if bloque:
            p.drawString(alineaTitre, y, "LOTS BLOQUES")
            y -= ecartLigne
            for bloques in b:
                p.drawString(alineaBase, y, 'Catégorie : '+bloques.categorie+' | Quantité : '+str(bloques.quantite)+' | Contremarque : '+bloques.contremarque)
                y -= ecartLigne
            y -= ecartLigne


        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='ticket-'+str(c.numContainer)+'.pdf')
