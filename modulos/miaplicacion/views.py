from django.shortcuts import render
from django.conf import settings

# Create your views here.
def vista1(request):
    return render(request,"formulario.html")

def url_recibe_responde(request):
    if request.method == "POST":
        # Se capturan las variables con los mismo nombres dados en los formularios de html
        asunto = request.POST["txtAsunto"]
        email = request.POST["txtEmail"]
        mensaje = request.POST["txtMensaje"]
        # Manejo
        mensaje = mensaje + " / Email: " + email
        # La idea es responder el mensaje automaticamente
        # Cargamos el correo q configuramos en settings.py
        # Esto no lo hice porque no quiero mandar un correo por ahora.
        # Para que luego se muestre una vista se carga una plantilla
        return render(request, "respuesta_formulario.html")
    else:
        return render(request,"formulario.html")
