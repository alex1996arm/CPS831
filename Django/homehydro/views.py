from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('./templates/index.html')
    context = {
        'graph': graph,
    }
    return HttpResponse(template.render(context,request))
