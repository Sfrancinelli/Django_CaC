from django.http import HttpResponse

# Every function created in the views file it's a view for our web.
def saludo(request):

    return HttpResponse("Hola mundo!")

def goodbye(request):

    return HttpResponse("Goodbye!")