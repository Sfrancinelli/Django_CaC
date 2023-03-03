from django.http import HttpResponse
import datetime

# Every function created in the views file it's a view for our web.
def saludo(request):

    documento = """
    <html>
        <body>
            <h1>
                Hola Mundo!
            </h1>
        </body>
    </html>"""

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

    

    