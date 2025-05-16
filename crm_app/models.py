from django.contrib.auth.models import AbstractUser
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    ROLE_CHOICES = (
        ('admin', 'Админ'),
        ('manager', 'Менеджер'),
        ('analyst', 'Аналитик'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager')

    def __str__(self):
        return f"{self.username} ({self.role})" 
    

class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Deal(models.Model):
    STAGES = [
        ('lead', 'Лид'),
        ('contacted', 'Контакт установлен'),
        ('proposal', 'Предложение'),
        ('won', 'Выиграно'),
        ('lost', 'Проиграно'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=20, choices=STAGES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
 

