from django.db import models


# Create your models here.
class Category(models.Choices):
    CATEGORY = [
        ("NEW", "unassigned"),
        ("URGENT_AND_IMPORTANT", "urgent and important"),
        ("URGENT_AND_NOT_IMPORTANT", "urgent and not important"),
        ("URGENT_BUT_NOT_IMPORTANT", "urgent but not important"),
        ("NOT_URGENT_AND_NOT_IMPORTANT", "not urgent and not important"),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self):
        return self.category


class Status(models.Model):
    STATUS = models.Choises[
        ("NOT_STARTED_YET", "not started yet"),
        ("IN_PROGRESS", "in progress"),
        ("PENDING", "pending"),
        ("DONE", "done"),
    ]

    status = models.CharField(max_length=50, choices=STATUS, default="NOT_STARTED_YET")

    def __str__(self):
        return self.status


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
