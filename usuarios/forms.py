from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class FormularioRegistroUsuarioTM(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'direccion', 'telefono', 'run']
