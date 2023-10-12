from core.library import console, exists, mkdirs, rename


class Decompressor:

  def __init__(self, file_record, user_dir) -> None:
    ''' initialize the decompressor for the designated file '''
    self.file = file_record
    self.dir = user_dir
    self.hot_dir = f"{self.dir}/hot/{self.file.uuid}"
    self.path = f"{self.dir}/{self.file.compressed_file_name()}"
    self.hot_path = f"{self.hot_dir}/{self.file}"
    if not exists(self.hot_dir):
      mkdirs(self.hot_dir, exist_ok=True)

  def decompress(self) -> None:
    ''' decompress a file using a method based on the compression type '''
    match self.file.compressed_ext:
      case '.lrz':
        return self.lrzip()

  def lrzip(self) -> None:
    ''' decompress a lrzip file to the hot directory '''
    console.input(f'lrzip -d {self.path} -O {self.hot_dir}', cwd=self.dir, show_output=True)
    rename(f"{self.hot_dir}/{self.file.uuid}", self.hot_path)
