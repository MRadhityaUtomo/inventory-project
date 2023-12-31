from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Registration form imports
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

# Login function imports 
from django.contrib.auth import authenticate, login

# Logout function imports
from django.contrib.auth import logout

# Restrict access
from django.contrib.auth.decorators import login_required

# last login cookie deetector mm
import datetime

from django.http import JsonResponse
import json

@login_required(login_url='/login')
def show_main(request):
    item = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'description': 'The ultimate wizard in terms of attack and defense. come and enter your wares traveler, for they will be your memoirs, reminders, keepsakes, of your adventure',
        'items' : item,
        'count' : item.count,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)



# Register function

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)



# Login function

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)



# logout function
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def add_Item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_Item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def add_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def dec_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        if item.amount > 0:
            item.amount -= 1
            item.save()
        if item.amount == 0:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_item(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main')) 


def edit_item(request, id):
    # Get item berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)


# Fetch API
@csrf_exempt
def get_item_json(request):
    obj_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', obj_item))


@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        omen = request.POST.get("omen")
        space = request.POST.get("space")
        description = request.POST.get("description")

        user = request.user

        new_item = Item(name=name, amount=amount, omen=omen, space=space, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        Item.objects.get(pk=id).delete()
        return HttpResponse(b"DELETED", status = 201)
    return HttpResponseNotFound()

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            omen = int(data["omen"]),
            space = int(data["space"]),
            description = data["description"],
            amount = int(data["amount"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
