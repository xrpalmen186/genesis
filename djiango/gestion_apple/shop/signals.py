# shop/models.py  (o shop/signals.py si lo tienes así)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Si el usuario se acaba de crear, aseguramos que exista un perfil (get_or_create evita IntegrityError)
    if created:
        from .models import Profile  # importa aquí si estás en signals.py para evitar import circular
        Profile.objects.get_or_create(user=instance)
