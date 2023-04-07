from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from .forms import PatientCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User, TemperatureData, RespirationData, PulseData, HumidityData, SPO2Data, NIBPData
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import time

# Create your views here.
def mainPage(request):
    return render(request, 'base/home.html')

def patient(request, pk):
    patient = User.objects.get(pk=pk)
    data = {
        'Temperature' : '-',
        'Respiration' : '-',
        'Pulse' : '-',
        'Humidity' : '-',
        'SPO2' : '-',
        'NIBPD' : '-',
    }
    
    if patient.temperaturedata_set.all():
        temps = patient.temperaturedata_set.all()
        data['Temperature'] = temps.latest('created')
    if patient.respirationdata_set.all():
        resps = patient.respirationdata_set.all()
        data['Respiration'] = resps.latest('created')
    if patient.pulsedata_set.all():
        pulses = patient.pulsedata_set.all()
        data['Pulse'] = pulses.latest('created')
    if patient.humiditydata_set.all():
        hums = patient.humiditydata_set.all()
        data['Humidity'] = hums.latest('created')
    if patient.spo2data_set.all():
        spo2s = patient.spo2data_set.all()
        data['SPO2'] = spo2s.latest('created')
    if patient.nibpdata_set.all():
        nibpds = patient.nibpdata_set.all()
        data['NIBPD'] = nibpds.latest('created')
    
    
    # context = {'pk': int(pk),'templ' : templ, 'respl' : respl,'pulsel' : pulsel,'huml' : huml,'spo2l' : spo2l,'nibpdl' : nibpdl }
    context = {'pk': int(pk), 'data' : data, 'patient' : patient }
    return render(request, 'base/patient.html', context)

def staff(request):
    patients = User.objects.all()
    data = {}
    for patient in patients:
        if patient.email == "staff@gmail.com":
            continue
        data[patient.username] = {}
        if patient.temperaturedata_set.all():
            data[patient.username]["Temperature"] = patient.temperaturedata_set.all().latest('created')
        else:
            data[patient.username]["Temperature"] = "No data"
        if patient.respirationdata_set.all():
            data[patient.username]["Respiration"] = patient.respirationdata_set.all().latest('created')
        else:
            data[patient.username]["Respiration"] = "No data"
        if patient.pulsedata_set.all():
            data[patient.username]["Pulse"] = patient.pulsedata_set.all().latest('created')
        else:
            data[patient.username]["Pulse"] = "No data"
        if patient.humiditydata_set.all():
            data[patient.username]["Humidity"] = patient.humiditydata_set.all().latest('created')
        else:
            data[patient.username]["Humidity"] = "No data"
        if patient.spo2data_set.all():
            data[patient.username]["SPO2"] = patient.spo2data_set.all().latest('created')
        else:
            data[patient.username]["SPO2"] = "No data"
        if patient.nibpdata_set.all():
            data[patient.username]["NIBP"] = patient.nibpdata_set.all().latest('created')
        else:
            data[patient.username]["NIBP"] = "No data"

    context = {"patients" : patients, "data" : data}
    return render(request, 'base/staff.html', context)

def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=username)
        except:
            messages.error(request, "User does not exist!")

        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'patient':
                return redirect('patient',user.id)
            else:
                return redirect('staff')
        else:
            messages.error(request, "Username or password does not exist!")

    context = {'page' : page, }
    return render(request, 'base/login_register.html', context)

def registerPatient(request):
    page = 'register'
    if request.method == "POST":
        form = PatientCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)#false to get the user object
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('patient',user.id)
        else:
            messages.error(request, form.errors)
    form = PatientCreationForm()
    context = {'page':page, 'form':form}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('main')

# def ajaxResponse(request):
#     data={"result" : "1,2,3,4,5,56,7"}
#     print("hello")
#     return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None, *arg, **kwarg):
        pk = kwarg["pk"]
        patient = User.objects.get(id=pk)
        temperatures = patient.temperaturedata_set.all().order_by('-created')[:20]
        respiration = patient.respirationdata_set.all().order_by('-created')[:20]
        pulse = patient.pulsedata_set.all().order_by('-created')[:20]
        humidity = patient.humiditydata_set.all().order_by('-created')[:20]
        spo2 = patient.spo2data_set.all().order_by('-created')[:20]
        nibpd = patient.nibpdata_set.all().order_by('-created')[:20]
        #users = User.objects.all().count()
        data = {}
        dat = []
        labels = []
        for temp in temperatures:
            dat.append(temp.value)
            time = str(temp.created).split(":")[:2]
            time = ":".join(time)
            labels.append(time)
        data["temperature"] = dat
        data["tlabels"] = labels
        dat = []
        labels = []
        for temp in respiration:
            dat.append(temp.value)
            time = str(temp.created).split(":")[:2]
            time = ":".join(time)
            labels.append(time)
        data["respiration"] = dat
        data["rlabels"] = labels
        dat = []
        labels = []
        for temp in pulse:
            dat.append(temp.value)
            time = str(temp.created).split(":")[:2]
            time = ":".join(time)
            labels.append(time)
        data["pulse"] = dat
        data["plabels"] = labels
        dat = []
        labels = []
        for temp in humidity:
            dat.append(temp.value)
            time = str(temp.created).split(":")[:2]
            time = ":".join(time)
            labels.append(time)
        data["humidity"] = dat
        data["hlabels"] = labels
        dat = []
        labels = []
        for temp in spo2:
            dat.append(temp.value)
            time = str(temp.created).split(":")[:2]
            time = ":".join(time)
            labels.append(time)
        data["spo2"] = dat
        data["slabels"] = labels
        dat = []
        labels = []
        for temp in nibpd:
            dat.append(temp.value)
            time = str(temp.created).split(":")[:2]
            time = ":".join(time)
            labels.append(time)
        data["nibpd"] = dat
        data["nlabels"] = labels
        return Response(data)
