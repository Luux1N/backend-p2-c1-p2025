from django.http import HttpResponse

def inicio(request):
    nombre = "Benshita"
    return HttpResponse(f"¡Bienvenido a mi primera APP Django, {nombre}")