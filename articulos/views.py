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