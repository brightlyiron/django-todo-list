from django.db import models


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField()
