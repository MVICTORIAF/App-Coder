from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .forms import AlumnoForm, ProfesorForm, CursoForm

def inicio(request):
    return render(request, "App/index.html")

def alumnos(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos')  # Cambia 'alumnos' por el nombre de la URL correspondiente
    else:
        form = AlumnoForm()
    return render(request, "App/alumno.html", {'form': form})

def profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor')  
    else:
        form = ProfesorForm()
    return render(request, "App/profesor.html", {'form': form})

def curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso') 
    else:
        form = CursoForm()
    return render(request, "App/cursos.html", {'form': form})

