from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):
    return render(request, "home.html")
def listadoEmpresa(request):   
    return render(request, 'listadoempresa.html', )
