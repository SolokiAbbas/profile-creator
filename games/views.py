from django.shortcuts import render

# Create your views here.
def forced(request):
    return render(request, 'games/forced.html')

def collision(request):
    return render(request, 'games/collision.html')

def fireball(request):
    return render(request, 'games/fireball.html')
