from django.shortcuts import render
from .models import Survey

# Create your views here.
def Index(request):
    context = Survey.objects.order_by('-last_updated')[:4]
    return render(request, 'index.html', {'surveys': context})

def CreateSurvey(request):
    pass

def CallTheModal(request):
    return render(request, 'partials/Modalfile.html')

def CreateFile(request):
    filename = request.POST.get('filename')
    context = {'filename': filename}
    return render(request, 'partials/subFile.html',context)

