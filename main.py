# Utilización de la interfaz gráfica del módulo PyGame para crear un termómetro.

import pygame, sys
from pygame.locals import *

class Termometro():
   def __init__(self):
      self.custome = pygame.image.load("images/termo1.png")

class NumberInput():
   __valor = 0
   __strValue = "0"
   __position = [0, 0]
   __size = [0, 0]

   def __init__(self, valor=0):
      self.__font = pygame.font.SysFont("Arial", 24)
      textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
      rect = textBlock.get.rect()
      rect.left = self.__position[0]
      rect.top = self.__position[1]
      rect.size = self.__size



class MainApp():
   termometro = None
   entrada = None
   selector = None

   def __init__(self):
      self.__screen = pygame.display.set_mode((290, 415))
      pygame.display.set_caption("Termómetro")
      self.__screen.fill((244, 236, 203))

      # Instancias de clases
      self.termometro = Termometro()
      self.entrada = NumberInput()


   def __on_close(self):
      pygame.quit()
      sys.exit()

   def star(self):
      while True:
         for event in pygame.event.get():
            if event.type == QUIT:
               self.__on_close()
         
         self.__screen.blit(self.termometro.custome, (50, 34))
         pygame.display.flip()




if __name__ == "__main__":
   pygame.font.init()
   app = MainApp()
   app.star()

