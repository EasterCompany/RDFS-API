from core.library import Path, dirname, realpath, api, mkdirs
from web.settings import BASE_DIR


class _API(api.UniversalAPI):

  NAME = Path(dirname(realpath(__file__))).parts[-1]

  UPLOAD_DIR = Path(BASE_DIR) / "static/shared/rdfs"

  def __init__(self) -> None:
    super().__init__()
    mkdirs(self.UPLOAD_DIR, exist_ok=True)


API = _API()
