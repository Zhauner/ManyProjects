import os
import pygame
import eyed3
from PIL import Image

class MoveMenu:
    def __init__(self, x, y, height_y = 0):
        self._x = x
        self._y = y
        self.rect = self.paste_alf().get_rect()
        self.rect.y = self._y
        self.height_y = height_y

    def paste_alf(self):
        surf = pygame.Surface((self._x,self._y))
        return surf

    def update_move(self):
        '''Скроллинг вверх'''
        self.height_y += 51
        return self.height_y

    def min_update_move(self):
        '''Скроллинг вниз'''
        self.height_y -= 51
        return self.height_y

    def return_zero(self):
        return 0

class Menu:

    _LIGHT_BLACK = (40,40,40)

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

    def return_lenght_string(self):
        return len(self._ARTISTS)

    def create_tracks(self):
        tracks_window = pygame.Surface((360, 50))
        return tracks_window

class Click_surface:

    _BLUE = (0,0,200)
    _LAYERS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alpha = 0

    def draw_click_surafce(self):
        click_surface = pygame.Surface((self.x, self.y))
        click_surface.fill((self._BLUE))
        click_surface.set_alpha(self.alpha)
        return click_surface

    def layers_list(self, count):
        layers = [f'layer{x}' for x in range(1, count + 1)]
        return layers

class Pictures_from_mp3:

    def __init__(self, path, path_to_img):
        self.path = path
        self.path_to_img = path_to_img

    def mp3_files_path(self):
        files = os.listdir(self.path)
        return files

    def img_files_path(self):
        img_path = os.listdir(self.path_to_img)
        return img_path

    def save_pictures(self):

        for pic in range(len(self.mp3_files_path())):

            audio = eyed3.load(f'{os.getcwd()}\\music\\{self.mp3_files_path()[pic]}')

            if len(audio.tag.images._fs) > 2:
                for img in audio.tag.images:

                    image_file = open('pictures\\{0}.jpg'.format(self.mp3_files_path()[pic][:-4]), 'wb')
                    image_file.write(img.image_data)
                    image_file.close()

            elif len(audio.tag.images._fs) == 2:
                pict = Image.open(f'{os.getcwd()}\\picture_for_nonpicmusic.jpg')
                pict.save('pictures\\{0}.jpg'.format(self.mp3_files_path()[pic][:-4]))


            resize_image = Image.open(f'pictures\\{self.img_files_path()[pic]}').convert('RGBA')
            new_image = resize_image.resize((50, 50))
            new_image.save('resize images\\{0}.png'.format(self.mp3_files_path()[pic][:-4]))

        return ''