# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
caminho_arquivo = r"C:\Users\Guibsh Admin\Desktop\Xenogenesis\ORIGIN Xenogenesis The Fat Rat.mp3"
pygame.mixer.music.load(caminho_arquivo)
pygame.mixer.music.play()
import time
time.sleep(360)
pygame.mixer.quit()