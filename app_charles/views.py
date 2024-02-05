from django.shortcuts import render
from django.views import View
from .models import Libros
from .forms import BuscarLibroForm

# Create your views here.

class BuscarLibroView(View):
    template_name = 'buscar_libro.html'
    
    def get(self, request):
        # Lógica para manejar solicitudes GET
        form = BuscarLibroForm() #agregado al crear el formulario
       
        
        libros = Libros.objects.all() # Obtén todos los libros desde la base de datos
        return render(request,self.template_name, {'form': form, 'libros': libros})
    
    
    def post(self, request):
        # Lógica para manejar solicitudes POST
        # Puedes acceder a los datos del formulario utilizando request.POST
        form = BuscarLibroForm(request.POST)
        
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            libros = Libros.objects.filter(autor__icontains=termino_busqueda) | \
                     Libros.objects.filter(nombre__icontains=termino_busqueda)    # Filtra los libros por autor, icontains se usa para realizar una búsqueda insensible a mayúsculas y minúsculas.
            return render(request, self.template_name , {'form': form, 'libros': libros, 'termino_busqueda': termino_busqueda})
        
        else:
            return render(request, self.template_name, {'form': form})