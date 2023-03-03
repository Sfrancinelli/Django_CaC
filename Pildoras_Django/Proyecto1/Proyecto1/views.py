from django.http import HttpResponse

# Every function created in the views file it's a view for our web.
def saludo(request):

    documento = "<html><body><h1>Hola Mundo!</h1></body></html>"

    return HttpResponse(documento)

def goodbye(request):

    return HttpResponse("Goodbye!")