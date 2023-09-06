from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Irfan Firmansyah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)