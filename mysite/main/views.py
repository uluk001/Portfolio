from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

from main.models import Contact, My_skill, skill

# Create your views here.
def home(request):
    data = skill.objects.all()
    data2 = My_skill.objects.all()
    return render(request, 'index.html', {'data':data, 'data2':data2})


def main(request):
    return render(request, 'main.html')

def sendMessage(request):
    if request.method == 'POST':
        send_message = Contact()
        send_message.name = request.POST.get("name")
        send_message.message = request.POST.get("message")
        send_message.email = request.POST.get("email")
        send_message.save()
        return HttpResponseRedirect('/')

