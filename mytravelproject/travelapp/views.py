from django.http import HttpResponse
from django.shortcuts import render


from . models import place
from . models import team
# Create your views here.
def demo(request):
     obj=place.objects.all()
     newobj=team.objects.all()


     return render(request,"index.html",{'result':obj,'res':newobj})


# def about(request):
#      return render(request,"about.html")
# def contact(request):
#      return HttpResponse("i am contact")
