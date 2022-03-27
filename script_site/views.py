from django.shortcuts import render

def index (request):
    print(f'Este é o request: {request}')
    return render(request, 'index.html')


# Create your views here.
