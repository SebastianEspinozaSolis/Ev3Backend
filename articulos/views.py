from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required
from reseñas.models import Reseña
@login_required
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')
    return render(request, 'articulos/lista_publicaciones.html', {'publicaciones': publicaciones})

@login_required
def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    # Verificar si el usuario ya dejó una reseña
    usuario_reseño = Reseña.objects.filter(usuario=request.user, publicacion=publicacion).exists() if request.user.is_authenticated else False

    return render(request, 'articulos/detalle_publicacion.html', {
        'publicacion': publicacion,
        'usuario_reseño': usuario_reseño,
    })

@login_required
def crear_publicacion(request):
    if request.user.perfil.rol in ['vendedor', 'administrador']:
        if request.method == 'POST':
            form = PublicacionForm(request.POST, request.FILES)
            if form.is_valid():
                publicacion = form.save(commit=False)
                publicacion.vendedor = request.user
                publicacion.save()
                return redirect('articulos:detalle_publicacion', pk=publicacion.pk)
        else:
            form = PublicacionForm()
        return render(request, 'articulos/crear_publicacion.html', {'form': form})
    else:
        return redirect('articulos:lista_publicaciones')

@login_required
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.user == publicacion.vendedor:
        if request.method == 'POST':
            form = PublicacionForm(request.POST, instance=publicacion)
            if form.is_valid():
                form.save()
                return redirect('articulos:detalle_publicacion', pk=publicacion.pk)
        else:
            form = PublicacionForm(instance=publicacion)
        return render(request, 'articulos/editar_publicacion.html', {'form': form, 'publicacion': publicacion})
    else:
        return redirect('articulos:lista_publicaciones')

@login_required
def mis_articulos(request):
    # Filtra las publicaciones solo para el vendedor autenticado
    publicaciones = Publicacion.objects.filter(vendedor=request.user)

    return render(request, 'articulos/mis_articulos.html', {'publicaciones': publicaciones})
    
from .serializers import PublicacionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#get ver, post crear, put creo que es actualizar, delete borrar
@api_view(['GET','POST'])
def publicaciones_api(request):
    if request.method=="GET":#Respuesta para mostrar todos los registros
        publicaciones=Publicacion.objects.all()
        serializer=PublicacionSerializer(publicaciones,many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":#Al agregar solicitud es con POST
        serializer=PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
#para detalles y editar o eliminar una especifica
@api_view(['GET','PUT','DELETE'])
def publicaciones_api_detalle(request,pk):
    try:
        publicacion=Publicacion.objects.get(pk=pk)
    except Publicacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":# Viene por la info
        serializer=PublicacionSerializer(publicacion)
        return Response(serializer.data)
    elif request.method=="PUT":# Lo actualiza
        serializer=PublicacionSerializer(publicacion,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":# lo elimina
        publicacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)