from django.shortcuts import render

def index(request) :
    # hardcoded for now
    user = {'name': 'Jenny', 'id': 1}
    context = {'user': user}
    return render(request, 'app/index.html', context)

def submit(request, user_id):
    # user = userExists()
    ids = request.POST['cusips']
    idList = ids.split()
    print('this is the POST from the request', idList)
    return render(request, 'app/success.html')
