from django.shortcuts import render
def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categories = ['code',  'design','marketing']
    contexto = {'name':name, 'categories':categories}
    return render(request, 'dinamico.html', contexto)