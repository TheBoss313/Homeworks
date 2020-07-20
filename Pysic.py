# rgb(34,31,30)
import pygame
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((8*87+150, 300))
screen.fill((34, 31, 30))


def buttons():
    global vol_dec_rect, vol_inc_rect, play_rect, pause_rect, mute_rect, stop_rect, prev_s_rect, next_s_rect
    x = 50
    vol_dec = pygame.image.load('icons/decrease_volume.jpg')
    vol_dec_rect = vol_dec.get_rect()
    vol_dec_rect.x, vol_dec_rect.y = x, 50
    screen.blit(vol_dec, (vol_dec_rect.x, 50))
    x += vol_dec.get_width()
    x += 5

    vol_inc = pygame.image.load('icons/increase_volume.jpg')
    vol_inc_rect = vol_inc.get_rect()
    vol_inc_rect.x, vol_inc_rect.y = x, 50
    screen.blit(vol_inc, (vol_inc_rect.x, 50))
    x += vol_inc.get_width()
    x += 5

    play = pygame.image.load('icons/play.jpg')
    play_rect = play.get_rect()
    play_rect.x, play_rect.y = x, 50
    screen.blit(play, (play_rect.x, 50))
    x += play.get_width()
    x += 5

    pause = pygame.image.load('icons/pause.jpg')
    pause_rect = pause.get_rect()
    pause_rect.x, pause_rect.y = x, 50
    screen.blit(pause, (pause_rect.x, 50))
    x += pause.get_width()
    x += 5

    stop = pygame.image.load('icons/stop.jpg')
    stop_rect = stop.get_rect()
    stop_rect.x, stop_rect.y = x, 50
    screen.blit(stop, (stop_rect.x, 50))
    x += stop.get_width()
    x += 5

    next_s = pygame.image.load('icons/next_song.jpg')
    next_s_rect = next_s.get_rect()
    next_s_rect.x, next_s_rect.y = x, 50
    screen.blit(next_s, (next_s_rect.x, 50))
    x += next_s.get_width()
    x += 5

    prev_s = pygame.image.load('icons/previous_song.jpg')
    prev_s_rect = prev_s.get_rect()
    prev_s_rect.x, prev_s_rect.y = x, 50
    screen.blit(prev_s, (prev_s_rect.x, 50))
    x += prev_s.get_width()
    x += 5

    mute = pygame.image.load('icons/mute.jpg')
    mute_rect = mute.get_rect()
    mute_rect.x, mute_rect.y = x, 50
    screen.blit(mute, (mute_rect.x, 50))
    x += mute.get_width()
    x += 5


buttons()
clock = pygame.time.Clock()
FPS = 60
num_song = 0
song_list = []
pygame.mixer.music.load(song_list[num_song])
pygame.display.update()
volume = 1
while True:
    clock.tick(FPS)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.MOUSEBUTTONUP:
            if stop_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.stop()
                screen.fill((34, 31, 30))
                buttons()
            elif play_rect.collidepoint(pygame.mouse.get_pos()):
                screen.fill((34, 31, 30))
                buttons()
                textsurface = myfont.render(f'Now Playing: {song_list[num_song]}', False, (255, 255, 255))
                screen.blit(textsurface, (150, 150))
                pygame.mixer.music.play()
            elif pause_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.pause()
            elif mute_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.music.set_volume(0)
            elif vol_dec_rect.collidepoint(pygame.mouse.get_pos()):
                volume -= 0.1
                pygame.mixer.music.set_volume(volume)
            elif vol_inc_rect.collidepoint(pygame.mouse.get_pos()):
                volume += 0.1
                pygame.mixer.music.set_volume(volume)
            elif prev_s_rect.collidepoint(pygame.mouse.get_pos()):
                num_song -= 1
                if num_song < 0:
                    num_song = len(song_list)-1
                screen.fill((34, 31, 30))
                buttons()
                textsurface = myfont.render(f'Now Playing: {song_list[num_song]}', False, (255, 255, 255))
                screen.blit(textsurface, (150, 150))
                pygame.mixer.music.load(song_list[num_song])
                pygame.mixer.music.play()
            elif next_s_rect.collidepoint(pygame.mouse.get_pos()):
                num_song += 1
                if num_song > len(song_list)-1:
                    num_song = 0
                screen.fill((34, 31, 30))
                buttons()
                textsurface = myfont.render(f'Now Playing: {song_list[num_song]}', False, (255, 255, 255))
                screen.blit(textsurface, (150, 150))
                pygame.mixer.music.load(song_list[num_song])
                pygame.mixer.music.play()
    pygame.display.update()
