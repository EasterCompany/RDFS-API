from core.library import (
  move,
  exists,
  rename,
  rmtree,
  getsize,
  dirname,
  console,
  basename,
  splitext,
)


class Compressor:

  def __init__(self, uuid:str, user_path:str, absolute_file_path:str) -> None:
    ''' initialize the compressor for the designated file and set the compression type '''
    self.uuid = uuid
    self.user_path = user_path
    self.dir = dirname(absolute_file_path)
    self.path = absolute_file_path
    self.name, self.ext = splitext(basename(self.path))
    self.compressed_ext = None
    self.compressed_size = None

  def compress(self) -> str|None:
    ''' maps the file extension to a designated compression type and compress the file '''
    match self.ext:

      case '.jpg' | '.jpeg':
        console.input(f'jpegoptim -s --all-progressive --dest={self.path} {self.path}', cwd=self.dir)
        return self.lrzip()

      case '.png' | '.bmp' | '.gif' | '.pnm' | '.tiff':
        console.input(f'optipng -o7 -out {self.path} {self.path}', cwd=self.dir)
        return self.lrzip()

    if self.ext != '.lrz' and exists(self.dir):
      return self.lrzip()
    else:
      return self.finalize('lrz')

  def finalize(self, compression_type) -> None:
    ''' renames, moves, deletes the original file '''
    tmp_file = f'{self.path}.{compression_type}'
    renamed_file = f'{self.uuid}.{compression_type}'
    rename(tmp_file, renamed_file)
    move(renamed_file, self.user_path)
    rmtree(self.dir)
    self.compressed_ext = f'.{compression_type}'
    self.compressed_size = getsize(f'{self.user_path}/{self.uuid}{self.compressed_ext}')

  def bzip(self) -> None:
    ''' bzip a file and set the alias '''
    console.input(f'tar -cjvf {self.name}{self.ext}.tar.bz2 {self.path}', cwd=self.dir)
    self.finalize('tar.bz2')

  def lrzip(self) -> None:
    ''' lrzip a file and set the alias '''
    console.input(f'lrzip -Q -U -z {self.path}', cwd=self.dir)
    self.finalize('lrz')
