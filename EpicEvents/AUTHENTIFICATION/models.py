from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from EpicEvents.CRM.models import Departement


class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, verbose_name="Identifiant unique de l'utilisateur")

    MANAGEMENT = 1
    SUPPORT = 2
    SALES = 3

    USER_ROLE = (
        (MANAGEMENT, "management"),
        (SUPPORT, "support"),
        (SALES, "sales"),
    )

    role = models.PositiveIntegerField(
        choices=USER_ROLE, verbose_name="Role", blank=True, null=True
    )

    affiliation_departement = models.ForeignKey(
        Departement, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=255)
    email = models.EmailField(
        unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nom: {self.name} | Role: {self.get_role_display()} | Department: {self.affiliation_departement}"

class JwtToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"JWT Token for {self.user.username}"