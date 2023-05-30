import pygame

#inicializar mixer
pygame.mixer.init()

#inicializar o PyGame
pygame.init()

#Código para tocar a música
pygame.mixer.music.load('des_21.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()