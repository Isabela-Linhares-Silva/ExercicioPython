import pygame
pygame.init()
pygame.mixer.music.load(*arquivo*)
pygame.mixer.music.play()
pygame.event.wait()