from django.shortcuts import render

# Create your views here.
def forced(request):
    return render(request, 'games/forced.html')
