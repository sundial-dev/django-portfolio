from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def project_list(request):
    #print(request)
    #return HttpResponse("hello")
    return render(request,'projects/index.html')