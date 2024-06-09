from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo"
        ,max_length=100, null=False, blank=False
    )  # n pode ter mais de 100 letras valor n pode estar em branco
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField( verbose_name="Data de entrega",null=False, blank=False)
    finished_at = models.DateField(null=True)
