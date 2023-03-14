from django.db import models


# Create your models here.
class Task(models.Model):

    STATUS = [
        ("not started yet", "not started yet"),
        ("in progres...", "in progress"),
        ("pending", "pending"),
        ("done", "done"),
    ]

    CATEGORY = [
        ("new", "unassigned"),
        ("urgent and important", "urgent and important"),
        ("not urgent and important", "urgent and not important"),
        ("urgent but not important", "urgent but not important"),
        ("not urgent and not important", "not urgent and not important"),
    ]

    ID = models.AutoField(primary_key=True)
    user = models.TextField
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True)

    def __str__(self) -> str:
        return f"{self.title} {self.category} {self.status}."

