from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'VaniTheSwaRi KaVaLi','s':'hai python'}
    return render(request,'usdf.html',d)