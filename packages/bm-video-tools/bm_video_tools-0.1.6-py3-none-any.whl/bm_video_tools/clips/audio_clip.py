from moviepy.audio.AudioClip import AudioClip

from .audio_reader import AudioReader


class AudioFileClip(AudioClip):
    def __init__(self, filename, buffersize=200000, nbytes=2, fps=44100):
        AudioClip.__init__(self)

        self.filename = filename
        self.reader = AudioReader(filename, fps=fps, nbytes=nbytes, buffersize=buffersize)
        self.fps = fps
        self.duration = self.reader.duration
        self.end = self.reader.duration
        self.buffersize = self.reader.buffersize

        self.make_frame = lambda t: self.reader.get_frame(t)
        self.nchannels = self.reader.nchannels

    def coreader(self):
        """ Returns a copy of the AudioFileClip, i.e. a new entrance point
            to the audio file. Use copy when you have different clips
            watching the audio file at different times. """
        return AudioFileClip(self.filename, self.buffersize)

    def close(self):
        """ Close the internal reader. """
        if self.reader:
            self.reader.close_proc()
            self.reader = None
