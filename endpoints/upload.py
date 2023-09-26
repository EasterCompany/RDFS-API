from core.library import api


def upload(req, *args, **kwargs):
  try:
    return api.success()
  except Exception as error:
    return api.error(error)
