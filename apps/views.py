from django.shortcuts import render

# Create your views here.
def index(request):
    ass = request.user.id
    print(ass)
    return render(request, 'apps/index.html')