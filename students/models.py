from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    registration_number = models.CharField(max_length=20, unique=True, verbose_name="Numéro d'inscription")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Numéro de téléphone")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Genre")
    address = models.TextField(verbose_name="Adresse")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
