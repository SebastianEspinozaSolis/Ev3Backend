# en views.py de la app reseñas

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reseña
from .forms import ReseñaForm
from articulos.models import Publicacion

@login_required
def crear_reseña(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    
    # Verificar si el usuario ya dejó una reseña
    if Reseña.objects.filter(usuario=request.user, publicacion=publicacion).exists():
        return redirect('articulos:detalle_publicacion', pk=pk)
    
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.usuario = request.user
            reseña.publicacion = publicacion
            reseña.save()
            return redirect('articulos:detalle_publicacion', pk=publicacion.pk)
    else:
        form = ReseñaForm()

    return render(request, 'reseñas/crear_reseña.html', {'form': form, 'publicacion': publicacion})
@login_required
def mis_reseñas(request):
    # Filtrar las reseñas que el usuario autenticado ha dejado
    reseñas_usuario = Reseña.objects.filter(usuario=request.user)

    return render(request, 'reseñas/mis_reseñas.html', {
        'reseñas': reseñas_usuario
    })
@login_required
def editar_reseña(request, pk):
    # Obtener la reseña que corresponde a ese ID
    reseña = get_object_or_404(Reseña, pk=pk, usuario=request.user)

    # Si el formulario fue enviado
    if request.method == 'POST':
        form = ReseñaForm(request.POST, instance=reseña)
        if form.is_valid():
            form.save()
            # Redirigir a "Mis Reseñas" después de guardar
            return redirect('reseñas:mis_reseñas')
    else:
        # Si no se ha enviado el formulario, mostrarlo con los datos actuales de la reseña
        form = ReseñaForm(instance=reseña)

    return render(request, 'reseñas/editar_reseña.html', {
        'form': form,
        'reseña': reseña
    })
  
from .serializers import ReseñaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#get ver, post crear, put creo que es actualizar, delete borrar
@api_view(['GET','POST'])
def reseñas_api(request):
    if request.method=="GET":#Respuesta para mostrar todos los registros
        reseñas=Reseña.objects.all()
        serializer=ReseñaSerializer(reseñas,many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":#Al agregar solicitud es con POST
        serializer=ReseñaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
#para detalles y editar o eliminar una especifica
@api_view(['GET','PUT','DELETE'])
def reseñas_api_detalle(request,pk):
    try:
        reseña=Reseña.objects.get(pk=pk)
    except Reseña.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":# Viene por la info
        serializer=ReseñaSerializer(reseña)
        return Response(serializer.data)
    elif request.method=="PUT":# Lo actualiza
        serializer=ReseñaSerializer(reseña,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":# lo elimina
        reseña.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)