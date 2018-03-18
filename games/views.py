from django.shortcuts import render

# Create your views here.
def forced(request):
    return render(request, 'games/forced.html')

def wave(request):
    return render(request, 'games/wave.html')

def particle(request):
    return render(request, 'games/particle.html')
