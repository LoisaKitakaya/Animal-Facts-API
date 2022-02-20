from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'docs/index.html')

def docs(request):

    return render(request, 'docs/docs.html')