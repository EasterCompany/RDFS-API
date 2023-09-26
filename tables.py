from core.library import models, uuid, time

DIRECTORIES = {
  'generic': ('GENERIC', 'Generic'),
  'pictures': ('PICTURES', 'Pictures'),
  'videos': ('VIDEOS', 'Videos'),
  'audio': ('AUDIO', 'Audio'),
  'games': ('GAMES', 'Games'),
  'tv & movies': ('TV & MOVIES', 'TV & Movies'),
  'documents': ('DOCUMENTS', 'Documents')
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
  name = models.CharField(
    null=False,
    blank=False,
    default=uuid,
    max_length=128
  )
  ext = models.CharField(
    null=True,
    blank=True,
    max_length=36,
  )
  size = models.IntegerField(
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
  date_upload = models.DateTimeField(
    null=False,
    blank=False,
    default=time.now
  )
  directory = models.CharField(
    null=False,
    blank=False,
    default=DIRECTORIES['generic'],
    choices=(DIRECTORIES[dir] for dir in DIRECTORIES),
    max_length=36
  )

  def __str__(self) -> str:
    return f"{self.name}.{self.ext}"

  def __dict__(self) -> dict:
    return {
      "uuid": self.uuid,
      "name": f"{self.name}.{self.ext}",
      "alias": self.name,
      "ext": self.ext,
      "type": self.directory,
      "uploaded_by": self.uploaded_by
    }
