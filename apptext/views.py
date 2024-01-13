from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse,request
import datetime
from .models import patient
from django.views import View

# Create your views here.
def index(request):
    info = {}
    try :
        if request.method=="POST":
            name=request.POST.get("name")
            age=request.POST.get("age")
            mobile=request.POST.get("mobile")
            address=request.POST.get("address")
            medicine=request.POST.get("medicine")
            DATE = datetime.datetime.now()
            date = DATE.strftime("%x")
            time = DATE.strftime("%X")

            if name != None:
                x=patient(name=name , age=age , mobile=mobile , address=address , medicine=medicine , date=date , time=time)
                x.save()
                stext = name + " Data Added Successfully ..."
                info = {"successText" : stext}
    except :
        etext=f"Fill the Details Properly | {name} Data not Save ..."
        info = {"errorText" : etext}

    return render(request, "index.html" ,info)

def data(request):
    patientData = patient.objects.all()
    content = {
        "patient" : patientData
    }
    return render(request , "data.html" , content)



def search(request):
    data = {}
    if request.method == "POST":
        serachPat = request.POST.get("search")
        if serachPat != None:
            findPat = patient.objects.filter(name__icontains = serachPat)
        data = {
            "searchPatient" : findPat ,
            "patName" : serachPat
                }
    return render(request,"search.html",data)




def delete(request,id):
    deleteData = patient.objects.get(id=id)
    deleteData.delete()
    return redirect("/data")