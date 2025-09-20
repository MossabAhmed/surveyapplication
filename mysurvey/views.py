from django.shortcuts import render

# Create your views here.
def MySurvey(request):
    return render(request, 'mysurvey/MySurvey.html')