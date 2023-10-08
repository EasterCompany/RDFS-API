from core.library import Path, dirname, realpath, api
from web.settings import MEDIA_ROOT


class _API(api.UniversalAPI):

  NAME = Path(dirname(realpath(__file__))).parts[-1]

  def __init__(self) -> None:
    super().__init__()

  def upload_dir(self, user) -> None:
    return Path(MEDIA_ROOT) / f"{user.data.uuid}/rdfs"


API = _API()
