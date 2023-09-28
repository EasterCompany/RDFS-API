from core.library import Path, dirname, realpath, api, mkdirs
from web.settings import BASE_DIR


class _API(api.UniversalAPI):

  NAME = Path(dirname(realpath(__file__))).parts[-1]

  def __init__(self) -> None:
    super().__init__()

  def upload_dir(self, user) -> None:
    return Path(BASE_DIR) / f"static/shared/{user.data.uuid}/rdfs"


API = _API()
