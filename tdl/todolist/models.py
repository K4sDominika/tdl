from django.db import models

# Create your models here.
class Category(models.Model):
    pass


class Status(models.Model):
    pass


class Task(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.TextField
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    status = models.ForeignKey(
        "Status", on_delete=models.CASCADE)








