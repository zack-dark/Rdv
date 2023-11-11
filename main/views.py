from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Client,Rendezvous,Consultation
from .filters import ClientFilter
from django.core.paginator import Paginator
from .forms import LoginForm
from django.contrib.auth import authenticate ,login

def index(request):
    return render(request, 'pages/index.html')


def client(request):
    context = {}
    filtered_client = ClientFilter(
        request.GET,
        queryset=Client.objects.all()
    )

    context['filtered_client'] = filtered_client

    paginated_filtered_client = Paginator(filtered_client.qs, 3)
    page_number = request.GET.get('page')
    client_page_obj = paginated_filtered_client.get_page(page_number)

    context ['client_page_obj'] = client_page_obj

    return render(request, 'pages/client.html',context=context)

# def doctor(request):
#     medecins = Medecin.objects.all()
#     context = {
#         'medecins': medecins,
#
#     }
#     return render(request, 'pages/doctor.html',context)

def rendezvous(request):
    clients = Client.objects.all()
    # medecins = Medecin.objects.all()
    rendez = Rendezvous.objects.all()
    context = {
        'clients': clients,
        # 'medecins': medecins,
        'rendez': rendez,

    }
    return render(request, 'pages/rendezvous.html',context)

def consultation(request):
    rendez = Rendezvous.objects.all()
    consultation = Consultation.objects.all()

    context = {
        'rendez': rendez,
        'consultation': consultation,

    }

    return render(request, 'pages/consultation.html',context)



def add_client(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        dateN = request.POST['dateN']
        clients= Client(nom=nom, prenom=prenom, email=email, dateN=dateN)
        clients.save()
        clients = Client.objects.all()
        context = {
            'clients': clients,

        }
    else:
        pass
    return render(request, 'pages/client.html',context)
def delete_client(request,myid):
    clients = Client.objects.get(id = myid)
    clients.delete()
    return redirect(client)

def edit_client(request,myid):
    clients = Client.objects.get(id=myid)
    sel_client = Client.objects.all()
    context = {
        'clients': clients,
        'sel_client':  sel_client,
    }
    return render(request, 'pages/editclient.html',context)


def update_client(request,myid):
    clients = Client.objects.get(id=myid)
    clients.nom = request.POST['nom']
    clients.prenom = request.POST['prenom']
    clients.email = request.POST['email']
    clients.dateN = request.POST['dateN']
    clients.save()
    return redirect(client)



# def add_doctor(request):
#     if request.method == "POST":
#         nom = request.POST['nom']
#         prenom = request.POST['prenom']
#         specialite = request.POST['specialite']
#         medecins= Medecin(nom=nom, prenom=prenom, specialite=specialite)
#         medecins.save()
#         medecins = Medecin.objects.all()
#         context = {
#             'medecins': medecins,
#
#         }
#     else:
#         pass
#     return render(request, 'pages/doctor.html',context)
#
# def delete_doctor(request,myid):
#     medecins = Medecin.objects.get(id = myid)
#     medecins.delete()
#     return redirect(doctor)



def add_rendezvous(request):
    if request.method == "POST":
        date = request.POST['date']
        rendezvous = request.POST['rendezvous']
        nomclient_id = request.POST['nomclient_id']
        # nomdoctor_id = request.POST['nomdoctor_id']
        rendez= Rendezvous(date=date, rendezvous=rendezvous, nomclient_id=nomclient_id)
        rendez.save()
        rendez = Rendezvous.objects.all()
        clients = Client.objects.all()
        # medecins = Medecin.objects.all()
        context = {
            'rendez': rendez,
            'clients': clients,
            # 'medecins': medecins,

        }
    else:
        pass
    return render(request, 'pages/rendezvous.html',context)


# def delete_doctor(request,myid):
#     rendez = Rendezvous.objects.get(id = myid)
#     rendez.delete()
#     return redirect(rendezvous)






def add_consultation(request):
    if request.method == "POST":
        description = request.POST['description']
        traitement = request.POST['traitement']
        type = request.POST['type']
        idrendezvous_id = request.POST['idrendezvous_id']
        consultation= Consultation(description=description, traitement=traitement, type=type, idrendezvous_id=idrendezvous_id)
        consultation.save()
        consultation = Consultation.objects.all()
        rendez = Rendezvous.objects.all()
        context = {
            'consultation': consultation,
            'rendez': rendez,

        }
    else:
        pass
    return render(request, 'pages/consultation.html',context)



def delete_consultation(request,myid):
    consultation = Consultation.objects.get(id = myid)
    consultation.delete()
    return redirect(consultation)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request)
