from django.db import models

# Create your models here.
class ConnectionType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Connection(models.Model):
    connection_type = models.ForeignKey(ConnectionType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Task(models.Model):
    connection_type = models.ForeignKey(ConnectionType, on_delete=models.CASCADE)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
