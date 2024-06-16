from django.shortcuts import render

def number_view(request):
    number = 24
    return render(request, 'index.html', {'number': number})
