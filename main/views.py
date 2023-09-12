from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Radhitya Utomo',
        'class': 'PBP D',
        'description': 'The ultimate wizard in terms of attack and defense',
        'attack': 2500,
        'defense': 2100,
        'amount': 64,

    }

    return render(request, "main.html", context)
