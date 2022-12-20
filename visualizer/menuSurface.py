import os
import pygame
#360, 400
class SurfAlfa():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def paste_alf(self):
        pygame.Surface((self._x,self._y))

class Menu:

    _LIGHT_BLACK = (40,40,40)

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def paste(self, surf):
        pygame.draw.rect(surf, self._LIGHT_BLACK, (self._x, self._y, 360, 400), 0, 3)

class ScrollMenu:

    _FILES = []
    _ARTISTS = []

    def __init__(self, path: str):
        self._path = path


    def get_tracklist(self) -> list:

        for mp3_file in os.listdir(self._path):
            if os.path.splitext(mp3_file)[1] == '.mp3':
                self._FILES.append(mp3_file)
        return self._FILES
    def get_artists(self):
        for artists in os.listdir(self._path):
            if os.path.splitext(artists)[1] == '.mp3':
                self._ARTISTS.append(os.path.splitext(artists)[0])
        return self._ARTISTS

    def create_tracks(self):
        tracks_window = pygame.Surface((360, 50))
        return tracks_window


#ss = ScrollMenu(f'{os.getcwd()}\\music\\')
#print(ss.get_artists())
