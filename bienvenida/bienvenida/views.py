from django.http import HttpResponse

def inicio(request):
    nombre = "Luxinn"
    return HttpResponse(f"¡Bienvenido a mi primera APP Django, {nombre}")