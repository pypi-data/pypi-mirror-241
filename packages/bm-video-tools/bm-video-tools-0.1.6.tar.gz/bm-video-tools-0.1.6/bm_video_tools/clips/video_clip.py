from moviepy.video.VideoClip import VideoClip

from .video_reader import VideoReader
from .audio_clip import AudioFileClip


class VideoFileClip(VideoClip):
    def __init__(self, filename, codec=None, has_mask=False,
                 audio=True, audio_buffersize=200000,
                 target_resolution=None, resize_algorithm='bicubic',
                 audio_fps=44100, audio_nbytes=2, fps_source='tbr'):

        VideoClip.__init__(self)

        # Make a reader
        pix_fmt = "rgba" if has_mask else "rgb24"
        self.reader = VideoReader(filename, codec=codec, pix_fmt=pix_fmt,
                                  target_resolution=target_resolution,
                                  resize_algo=resize_algorithm,
                                  fps_source=fps_source)

        self.duration = self.reader.duration
        self.end = self.reader.duration

        self.fps = self.reader.fps
        self.size = self.reader.size
        self.rotation = self.reader.rotation

        self.filename = self.reader.filename

        if has_mask:

            self.make_frame = lambda t: self.reader.get_frame(t)[:, :, :3]
            mask_mf = lambda t: self.reader.get_frame(t)[:, :, 3] / 255.0
            self.mask = (VideoClip(ismask=True, make_frame=mask_mf)
                         .set_duration(self.duration))
            self.mask.fps = self.fps

        else:

            self.make_frame = lambda t: self.reader.get_frame(t)

        if audio and self.reader.infos['audio_found']:
            self.audio = AudioFileClip(filename,
                                       buffersize=audio_buffersize,
                                       fps=audio_fps,
                                       nbytes=audio_nbytes)

    def close(self):
        """ Close the internal reader. """
        if self.reader:
            self.reader.close()
            self.reader = None

        try:
            if self.audio:
                self.audio.close()
                self.audio = None
        except AttributeError:
            pass
