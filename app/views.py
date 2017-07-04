from django.shortcuts import render

def index(request) :
    # hardcoded for now
    user = {'name': 'Jenny', 'id': 1}
    context = {'user': user}
    return render(request, 'app/index.html', context)
