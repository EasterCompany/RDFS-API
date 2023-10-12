from core.library import (
  move,
  exists,
  rename,
  remove,
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
    if self.ext.startswith('.'):
      self.ext_type = self.ext[1:]
    else:
      self.ext_type = self.ext

  def compress(self) -> str|None:
    ''' maps the file extension to a designated compression type and compress the file '''
    match self.ext_type:

      case 'jpg'|'jpeg':
        console.input(f'jpegoptim -s --all-progressive --dest={self.path} {self.path}', cwd=self.dir)
        return self.lrzip()

      case 'png'|'bmp'|'gif'|'pnm'|'tiff':
        console.input(f'optipng -o7 -out {self.path} {self.path}', cwd=self.dir)
        return self.lrzip()

      case '3dostr'|'3g2'|'3gp'|'4xm'|'a64'|'aa'|'aac'|'aax'|'ac3'|'ace'|'acm'|'act'|'adf'|'adp'|'ads'|'adts'|\
        'adx'|'aea'|'afc'|'aiff'|'aix'|'alaw'|'alias_pix'|'alp'|'alsa'|'amr'|'amrnb'|'amrwb'|'amv'|'anm'|'apc'|'ape'\
        'apm'|'apng'|'aptx'|'aptx_hd'|'aqtitle'|'argo_asf'|'argo_brp'|'argo_cvg'|'asf'|'asf_o'|'asf_stream'|'ass'|\
        'ast'|'au'|'av1'|'avi'|'avif'|'avm2'|'avr'|'avs'|'avs2'|'avs3'|'bethsoftvid'|'bfi'|'bfstm'|'bin'|'bink'|\
        'binka'|'bit'|'bitpacked'|'bmp_pipe'|'bmv'|'boa'|'brender_pix'|'brstm'|'c93'|'caca'|'caf'|'cavsvideo'|'cdg'|\
        'cdxl'|'chromaprint'|'cine'|'codec2'|'codec2raw'|'concat'|'crc'|'cri_pipe'|'dash'|'data'|'daud'|'dcstr'|\
        'dds_pipe'|'derf'|'dfa'|'dfpwm'|'dhav'|'dirac'|'dnxhd'|'dpx_pipe'|'dsf'|'dsicin'|'dss'|'dts'|'dtshd'|'dv'|\
        'dvbsub'|'dvbtxt'|'dvd'|'dxa'|'ea'|'ea_cdata'|'eac3'|'epaf'|'exr_pipe'|'f32be'|'f32le'|'f4v'|'f64be'|'f64le'|\
        'fbdev'|'ffmetadata'|'fifo'|'fifo_test'|'film_cpk'|'filmstrip'|'fits'|'flac'|'flic'|'flv'|'framecrc'|\
        'framehash'|'framemd5'|'frm'|'fsb'|'fwse'|'g722'|'g723_1'|'g726'|'g726le'|'g729'|'gdv'|'gem_pipe'|'genh'|'gif'|\
        'gif_pipe'|'gsm'|'gxf'|'h261'|'h263'|'h264'|'hash'|'hca'|'hcom'|'hds'|'hevc'|'hls'|'hnm'|'ico'|'idcin'|'idf'|\
        'iec61883'|'iff'|'ifv'|'ilbc'|'image2'|'image2pipe'|'imf'|'ingenient'|'ipmovie'|'ipod'|'ipu'|'ircam'|'ismv'|\
        'iss'|'iv8'|'ivf'|'ivr'|'j2k_pipe'|'jack'|'jacosub'|'jpeg_pipe'|'jpegls_pipe'|'jpegxl_pipe'|'jv'|'kmsgrab'|\
        'kux'|'kvag'|'latm'|'lavfi'|'libcdio'|'libdc1394'|'libgme'|'libopenmpt'|'live_flv'|'lmlm4'|'loas'|'lrc'|\
        'luodat'|'lvf'|'lxf'|'m4v'|'matroska'|'mca'|'mcc'|'md5'|'mgsts'|'microdvd'|'mjpeg'|'mjpeg_2000'|\
        'mkvtimestamp_v2'|'mlp'|'mlv'|'mm'|'mmf'|'mods'|'moflex'|'mov'|'m4a'|'3gp'|'3g2'|'mj2'|'mp2'|'mp3'|'mp4'|'mpc'|\
        'mpc8'|'mpeg'|'mpeg1video'|'mpeg2video'|'mpegts'|'mpegtsraw'|'mpegvideo'|'mpjpeg'|'mpl2'|'mpsub'|'msf'|\
        'msnwctcp'|'msp'|'mtaf'|'mtv'|'mulaw'|'musx'|'mv'|'mvi'|'mxf'|'mxf_d10'|'mxf_opatom'|'mxg'|'nc'|'nistsphere'|\
        'nsp'|'nsv'|'null'|'nut'|'nuv'|'obu'|'oga'|'ogg'|'ogv'|'oma'|'openal'|'opengl'|'opus'|'oss'|'paf'|'pam_pipe'|\
        'pbp_pipe'|'pcx_pipe'|'pfm_pipe'|'pgmyuv_pipe'|'pgx_pipe'|'phm_pipe'|'photocd_pipe'|'pictor_pipe'|'pjs'|'pmp'|\
        'png_pipe'|'pp_bnk'|'ppm_pipe'|'psd_pipe'|'psp'|'psxstr'|'pulse'|'pva'|'pvf'|'qcp'|'qdraw_pipe'|'qoi_pipe'|\
        'r3d'|'rawvideo'|'realtext'|'redspark'|'rl2'|'rm'|'roq'|'rpl'|'rsd'|'rso'|'rtp'|'rtp_mpegts'|'rtsp'|'s16be'|\
        's16le'|'s24be'|'s24le'|'s32be'|'s32le'|'s334m'|'s8'|'sami'|'sap'|'sbc'|'sbg'|'scc'|'scd'|'sdl'|'sdl2'|'sdp'|\
        'sdr2'|'sds'|'sdx'|'segment'|'ser'|'sga'|'sgi_pipe'|'shn'|'siff'|'simbiosis_imx'|'sln'|'smjpeg'|'smk'|\
        'smoothstreaming'|'smush'|'sol'|'sox'|'spdif'|'spx'|'srt'|'stl'|'stream_segment'|'ssegment'|'streamhash'|\
        'subviewer'|'subviewer1'|'sunrast_pipe'|'sup'|'svag'|'svcd'|'svg_pipe'|'svs'|'swf'|'tak'|'tedcaptions'|'tee'|\
        'thp'|'tiertexseq'|'tiff_pipe'|'tmv'|'truehd'|'tta'|'ttml'|'tty'|'txd'|'ty'|'u16be'|'u16le'|'u24be'|'u24le'|\
        'u32be'|'u32le'|'u8'|'uncodedframecrc'|'v210'|'v210x'|'vag'|'vbn_pipe'|'vc1'|'vc1test'|'vcd'|'vidc'|\
        'video4linux2'|'v4l2'|'vividas'|'vivo'|'vmd'|'vob'|'vobsub'|'voc'|'vpk'|'vplayer'|'vqf'|'w64'|'wav'|'wc3movie'|\
        'webm'|'webm_chunk'|'web_dash_manifest'|'webp'|'webp_pipe'|'webvtt'|'wsaud'|'wsd'|'wsvqa'|'wtv'|'wv'|'wve'|\
        'x11grab'|'xa'|'xbin'|'xbm_pipe'|'xmv'|'xpm_pipe'|'xv'|'xvag'|'xwd_pipe'|'xwma'|'yop'|'yuv4mpegpipe':
        rename(self.path, f'{self.path}.original')
        console.input(f'ffmpeg -y -i {self.path}.original {self.path}', cwd=self.dir)
        remove(f'{self.path}.original')
        return self.lrzip()

    if self.ext_type != '.lrz' and exists(self.dir):
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
    console.input(f'lrzip -Q -U -D -z {self.path}', cwd=self.dir)
    self.finalize('lrz')
