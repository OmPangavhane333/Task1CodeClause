from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    def __init__(self, window):
        window.geometry('360x120');
        window.title('Music Player By Om Pangavhane');
        window.resizable(0, 0)
        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
        Load.place(x=10, y=30);
        Play.place(x=130, y=30);
        Pause.place(x=250, y=30);
        Stop.place(x=130, y=80)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()


root = Tk()
app = MusicPlayer(root)
root.mainloop()
