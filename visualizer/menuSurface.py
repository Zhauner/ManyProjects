import os
import pygame
#360, 400
class MoveMenu:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.rect = self.paste_alf().get_rect()
        self.rect.y = self._y
        self.height_y = 0

    def paste_alf(self):
        surf = pygame.Surface((self._x,self._y))
        return surf

    def update_move(self):
        '''Скроллинг вверх'''
        self.height_y += 20
        return self.height_y

    def min_update_move(self):
        '''Скроллинг вниз'''
        self.height_y -= 20
        return self.height_y

class Menu:

    _LIGHT_BLACK = (120,120,40)

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def paste(self, surf):
        pl = pygame.draw.rect(surf, self._LIGHT_BLACK, (self._x, self._y, 360, 410), 0, 3)
        return pl



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
#print(ss.get_tracklist())


#ddd = MoveMenu(13,12)
#print(ddd.update_move())
#print(ddd.update_move())
#print(ddd.update_move())