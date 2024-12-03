from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name="tasks")
    screenshot = models.ImageField(upload_to="screenshots/")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"
