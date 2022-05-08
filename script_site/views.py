from django.shortcuts import render
from . import forms
from . import functions

def index (request):
    # including prints to understand the flow of information
    print(f'Este é o request: {request}')
    context = {}
    context['form'] = forms.BooleanForm()
    context['test'] = 'TESTING AGAIN'
    if request.GET:
        for values in request.GET:
            print(f"value = {values} : {request.GET[values]}")
        context['boolean'] = functions.booleanmaker(request.GET["tech1"], request.GET["tech2"], request.GET["job"],
                                                    request.GET["language"], request.GET["level"])


    return render(request, 'index.html', context)


# Create your views here.
