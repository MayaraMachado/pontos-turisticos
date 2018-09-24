from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateField(auto_now_add=True)
    aprovado = models.BooleanField(default = True)

    def __str__(self):
        return self.user.username