from core.library import models, uuid, time

FILE_TYPES = {
  'generic': 'Generic',
  'pictures': 'Pictures',
  'videos': 'Videos',
  'audio': 'Audio',
  'games': 'Games',
  'tv & movies': 'TV & Movies',
  'documents': 'Documents'
}


class RDFSModel(models.Model):
  uuid = models.CharField(
    null=False,
    blank=False,
    unique=True,
    default=uuid,
    max_length=36,
    primary_key=True
  )
  name = models.TextField(
    null=False,
    blank=False
  )
  ext = models.TextField(
    null=True,
    blank=True
  )
  mime_type = models.TextField(
    null=True,
    blank=True,
    default="text/html"
  )
  size = models.IntegerField(
    null=False,
    blank=False,
    default=0
  )
  compressed_size = models.IntegerField(
    null=False,
    blank=False,
    default=0
  )
  last_modified = models.DateTimeField(
    null=False,
    blank=False,
    default=time.now
  )
  uploaded_by = models.CharField(
    null=False,
    blank=False,
    max_length=36,
  )
  date_uploaded = models.DateTimeField(
    null=False,
    blank=False,
    default=time.now
  )
  file_type = models.TextField(
    null=False,
    blank=False,
    default=FILE_TYPES['generic']
  )

  def __str__(self) -> str:
    return f"{self.name}{self.ext}"

  def source_path(self) -> str:
    return f"/static/shared/{self.uploaded_by}/rdfs/{self.uuid}/{self}"
