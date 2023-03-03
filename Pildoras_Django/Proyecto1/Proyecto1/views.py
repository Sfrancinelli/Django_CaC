from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Every function created in the views file it's a view for our web.
def saludo(request):

    name = "Juan"

    last_name = "Diaz"

    date_now = datetime.datetime.now().strftime("%d/%m/%Y")

    doc_externo = open("C:/Users/Esteban/Desktop/SF/CaC_Django/Pildoras_Django/Proyecto1/Proyecto1/html/index.html")

    template = Template(doc_externo.read())

    doc_externo.close()

    context = Context({"name" : name, "last_name" : last_name, "date_now" : date_now})

    documento = template.render(context)

    return HttpResponse(documento)

def goodbye(request):

    return HttpResponse("Goodbye!")

def show_date(request):

    fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")

    documento = """
    <html>
        <body>
            <h1>
                La fecha actual es %s
            </h1>
        </body>
    </html>""" % fecha_actual

    # documento = f"""
    # <html>
    #     <body>
    #         <h1>
    #             La fecha actual es {fecha_actual}
    #         </h1>
    #     </body>
    # </html>"""

    # Any of this posibilities will work fine.

    return HttpResponse(documento)

def age_calculator(request, year, age):

    year_now = datetime.datetime.now().strftime("%Y") # 2023

    age_to_add = int(year) - int(year_now)

    future_age = int(age) + age_to_add

    # document = f"""
    # <html>
    #     <body>
    #         <h1>
    #             You will be {future_age} old on {year}
    #         </h1>
    #     </body>
    # </html>"""


    # This couyld be done with positional arguments

    document = """
    <html>
        <body>
            <h1>
                You will be %s old on %s
            </h1>
        </body>
    </html>""" %(future_age, year)

    return HttpResponse(document)

    

    