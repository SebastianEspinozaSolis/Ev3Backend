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
