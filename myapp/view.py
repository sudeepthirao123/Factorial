from django.shortcuts import render

def number_view(request):
    number = 25
    return render(request, 'index.html', {'number': number})
