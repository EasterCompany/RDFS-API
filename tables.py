# Overlord library
from core.library import models, uuid, JsonResponse, api, console


class RDFSModel(models.Model):
  uuid = models.CharField(
    null=False,
    blank=False,
    unique=True,
    default=uuid,
    max_length=36,
    primary_key=True
  )
