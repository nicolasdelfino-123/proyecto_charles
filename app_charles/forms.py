from django import forms





# formulario busqueda
class BuscarLibroForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, required=False, label='Buscar por Autor o Título del libro')
  
  
  
  
