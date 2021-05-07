from django.shortcuts import render

# Create your views here.
def jeongho_home(request):
    return render(request, template_name = 'jeongho/jeongho_home.html')