from django.shortcuts import render, redirect
from .models import Videojuego

# READ: Mostrar el listado
def listar_juegos(request):
    juegos = Videojuego.objects.all()
    return render(request, 'app_videojuegos/listar_juegos.html', {
        'juegos': juegos
    }) 

# CREATE: Crear un nuevo videojuego
def crear_juego(request):
    if request.method == 'POST':
        # Capturamos los datos enviados desde el formulario HTML
        titulo = request.POST['titulo']
        plataforma = request.POST['plataforma']
        genero = request.POST['genero']
        precio = request.POST['precio']
        stock = request.POST['stock']

        # Creamos el registro en MySQL
        Videojuego.objects.create(
            titulo=titulo, 
            plataforma=plataforma,
            genero=genero,
            precio=precio,
            stock=stock
        )
        return redirect('listar_juegos')
    
    return render(request, 'app_videojuegos/crear_juego.html')

# UPDATE: Editar un videojuego
def editar_juego(request, id):
     juego = Videojuego.objects.get(id=id)
     
     if request.method == 'POST':
         # Actualizamos los datos
         juego.titulo = request.POST['titulo']
         juego.plataforma = request.POST['plataforma']
         juego.genero = request.POST['genero']
         juego.precio = request.POST['precio']
         juego.stock = request.POST['stock']

         juego.save()
         return redirect('listar_juegos')
         
     return render(request, 'app_videojuegos/editar_juego.html', {
         'juego': juego
     })

# DELETE: Eliminar un videojuego
def eliminar_juego(request, id):
    juego = Videojuego.objects.get(id=id)

    if request.method == 'POST':
        juego.delete()
        return redirect('listar_juegos')

    return render(request, 'app_videojuegos/eliminar_juego.html', {
        'juego': juego
    })