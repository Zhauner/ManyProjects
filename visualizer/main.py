
import os


from AudioAnalyzer import *
from menuSurface import Menu
from menuSurface import ScrollMenu
from menuSurface import MoveMenu

import random
import colorsys

def rnd_color():
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    return [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]


filename = "music\\saluki_repriza.mp3"

analyzer = AudioAnalyzer()
#analyzer.load(filename)


pygame.init()

text = pygame.font.SysFont('arial', 20)

menu = Menu(50,20)

track_list = ScrollMenu(f'{os.getcwd()}\\music\\')

menu_alpha_scroll = MoveMenu(360,(51 * len(track_list.get_artists())))
menu_alpha_tracklist = menu_alpha_scroll.paste_alf()
infoObject = pygame.display.Info()
#int(infoObject.current_w/2.2) Изначальная ширина
screen_w = 900
screen_h = int(infoObject.current_w/2.2)

# Set up the drawing window
screen = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption('MP3 Player')



t = pygame.time.get_ticks()
getTicksLastFrame = t

timeCount = 0

avg_bass = 0
bass_trigger = -30
bass_trigger_started = 0

min_decibel = -80
max_decibel = 80

circle_color = (40, 40, 40) #40 * 3
polygon_default_color = [255, 255, 255]
polygon_bass_color = polygon_default_color.copy()
polygon_color_vel = [0, 0, 0]

poly = []
poly_color = polygon_default_color.copy()

circleX = int(screen_w / 1.5)
circleY = int(screen_h/2)

min_radius = 100
max_radius = 150
radius = min_radius
radius_vel = 0


bass = {"start": 50, "stop": 100, "count": 12}
heavy_area = {"start": 120, "stop": 250, "count": 40}
low_mids = {"start": 251, "stop": 2000, "count": 50}
high_mids = {"start": 2001, "stop": 6000, "count": 20}

freq_groups = [bass, heavy_area, low_mids, high_mids]


bars = []

tmp_bars = []


length = 0

for group in freq_groups:

    g = []

    s = group["stop"] - group["start"]

    count = group["count"]

    reminder = s%count

    step = int(s/count)

    rng = group["start"]

    for i in range(count):

        arr = None

        if reminder > 0:
            reminder -= 1
            arr = np.arange(start=rng, stop=rng + step + 2)
            rng += step + 3
        else:
            arr = np.arange(start=rng, stop=rng + step + 1)
            rng += step + 2

        g.append(arr)

        length += 1

    tmp_bars.append(g)


angle_dt = 360/length

ang = 0

for g in tmp_bars:
    gr = []
    for c in g:
        gr.append(
            RotatedAverageAudioBar(circleX+radius*math.cos(math.radians(ang - 90)), circleY+radius*math.sin(math.radians(ang - 90)), c, (255, 0, 255), angle=ang, width=8, max_height=370))
        ang += angle_dt

    bars.append(gr)

menu_surf = pygame.Surface((450,450), pygame.SRCALPHA) #плоскость для меню
menu_surf.fill((0,255,0))

scroll_surface = pygame.Surface((360, 410))#Плоскость скроллинга треков
#scroll_surface.set_alpha(100)

menu_rect = pygame.draw.rect(menu_surf, (204,0,204, 200), (30,2,400,450), 0, 15) #полупрозрачное меню +10


track_lists_field = track_list.create_tracks() # поле трека


menu_alpha_tracklist.fill((255,0,0))    # поле для отображения треков (360,408)

hh = 0
for x in range(len(track_list.get_tracklist())): #Вывод слоев под треки в зависимости от их количества в папке
    artists = text.render(track_list.get_tracklist()[x], True, (204,0,204))
    track_lists_field.fill((40,40,40))
    track_lists_field.blit(artists, (0,0))
    menu_alpha_tracklist.blit(track_lists_field, (0, hh))
    hh += 51

menu.paste(menu_surf)

#pygame.mixer.music.load(filename)
#pygame.mixer.music.play(0)
pygame.mixer.music.stop()
yy = 0 #Расположение плоскости треков
#pygame.display.update()
running = True
while running:

    avg_bass = 0
    poly = []

    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    timeCount += deltaTime
    scroll_surface.fill((120,120,40))
    screen.fill(circle_color)

    (x, y) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and x >= 50 and x <= 410 and y >= 50 and y <= 460:
            if event.button == 4:
                yy = menu_alpha_scroll.update_move()
            elif event.button == 5:
                yy = menu_alpha_scroll.min_update_move()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                analyzer.load(filename)
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play(0)
                polygon_default_color[0] = 100
            elif event.key == pygame.K_l:
                pygame.mixer.music.stop()
                polygon_default_color[0] = 225
            elif event.key == pygame.K_k:
                filename = 'music\\kriminalnyj-bit-plohoj-horoshij.mp3'
                analyzer.load(filename)
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play(0)



    for b1 in bars:
        for b in b1:
            b.update_all(deltaTime, pygame.mixer.music.get_pos() / 1000.0,analyzer)

    for b in bars[0]:
        avg_bass += b.avg

    avg_bass /= len(bars[0])

    if avg_bass > bass_trigger:
        if bass_trigger_started == 0:
            bass_trigger_started = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - bass_trigger_started)/1000.0 > 2:
            polygon_bass_color = rnd_color()
            bass_trigger_started = 0
        if polygon_bass_color is None:
            polygon_bass_color = rnd_color()
        newr = min_radius + int(avg_bass * ((max_radius - min_radius) / (max_decibel - min_decibel)) + (max_radius - min_radius))
        radius_vel = (newr - radius) / 0.15

        #polygon_color_vel = [(polygon_bass_color[x] - poly_color[x])/0.15 for x in range(len(poly_color))]

    elif radius > min_radius:
        bass_trigger_started = 0
        polygon_bass_color = None
        radius_vel = (min_radius - radius) / 0.15
        polygon_color_vel = [(polygon_default_color[x] - poly_color[x])/0.15 for x in range(len(poly_color))]

    else:
        bass_trigger_started = 0
        poly_color = polygon_default_color.copy()
        polygon_bass_color = None
        polygon_color_vel = [0, 0, 0]

        radius_vel = 0
        radius = min_radius

    radius += radius_vel * deltaTime

    for x in range(len(polygon_color_vel)):
        value = polygon_color_vel[x]*deltaTime + poly_color[x]
        #poly_color[x] = value

    for b1 in bars:
        for b in b1:
            b.x, b.y = circleX+radius*math.cos(math.radians(b.angle - 90)), circleY+radius*math.sin(math.radians(b.angle - 90))
            b.update_rect()

            poly.append(b.rect.points[3])
            poly.append(b.rect.points[2])

    pygame.draw.polygon(screen, poly_color, poly)
    pygame.draw.circle(screen, circle_color, (circleX, circleY), int(radius))

    screen.blit(menu_surf, (0, 30))
    scroll_surface.blit(menu_alpha_tracklist, (0, yy))
    screen.blit(scroll_surface, (50, 50))

    pygame.display.flip()

pygame.quit()