from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World from Django!")

# Create your views here.
