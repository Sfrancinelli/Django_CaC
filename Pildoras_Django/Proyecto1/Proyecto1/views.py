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
    