import os
from core.library import console, remove, rmtree


class Compressor:

  def __init__(self, file_dir:str, absolute_file_path:str, mime_type:str) -> None:
    self.dir = file_dir
    self.path = absolute_file_path
    self.name, self.ext = os.path.splitext(os.path.basename(self.path))
    self.size = os.path.getsize(self.path)
    self.mime_type = mime_type
    self.compression_type = self.compression_type()
    self.compressed_alias = None
    self.compressed_size = None

  def compression_type(self) -> str|None:
    if self.ext == '.jpg' or self.ext == '.jpeg' or self.mime_type == 'image/jpg' or self.mime_type == 'image/jpeg':
      return 'jpg'
    elif self.ext == '.png' or self.mime_type == 'image/png' or\
      self.ext == '.bmp' or self.mime_type == 'image/bmp' or\
      self.ext == '.gif' or self.mime_type == 'image/gif' or\
      self.ext == '.pnm' or self.mime_type == 'image/pnm' or\
      self.ext == '.tiff' or self.mime_type == 'image/tiff':
      return 'png'
    elif self.ext != '.lrz':
      return 'lrz'
    return None

  def set_alias(self, compression_type, remove_original=True) -> None:
    self.compressed_alias = f'{self.name}{self.ext}.{compression_type}'
    if remove_original:
      remove(self.path)

  def bzip(self, remove_original=True) -> None:
    console.input(f'tar -cjvf {self.dir}.tar.bz2 {self.dir}')
    if remove_original:
      rmtree(self.dir)

  def compress(self) -> int:
    match self.compression_type:
      case 'jpg':
        console.input(f'jpegoptim -s --all-progressive --dest={self.path} {self.path}', cwd=self.dir)
      case 'png':
        console.input(f'optipng -o7 -out {self.path} {self.path}', cwd=self.dir)
    console.input(f'lrzip -z {self.path}', cwd=self.dir)
    self.set_alias('lrz')
    self.compressed_size = os.path.getsize(f'{self.dir}/{self.compressed_alias}')
    return {
      'dir': self.dir,
      'path': self.path,
      'name': self.name,
      'ext': self.ext,
      'size': self.size,
      'mime_type': self.mime_type,
      'compressed_alias': self.compressed_alias,
      'compressed_size': self.compressed_size
    }
