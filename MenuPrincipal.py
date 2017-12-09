
import sys, pygame
from image import *
from menu import *
from Historia import*


screen = pygame.display.set_mode((1200, 750), pygame.FULLSCREEN)
## ---[ main ]------------------------------------------------------------------
#  This function runs the entire screen and contains the main while loop
#
def main():
   # Initialize Pygame
   pygame.init()

   #importa Musica
   pygame.mixer.music.load("Musica/MenuPrincipal.mp3")
   pygame.mixer.music.play(-1)

   # Create a window of 800x600 pixels
   screen = pygame.display.set_mode((1200, 750), pygame.FULLSCREEN)

   # Set the window caption
   pygame.display.set_caption("Menu Example - (c) Scott Barlow")

   # Load some images to use for sample buttons
   image1  = load_image('1.png', 'images')
   image2  = load_image('2.png', 'images')
   image3  = load_image('3.png', 'images')
   image4  = load_image('4.png', 'images')
   image5  = load_image('5.png', 'images')
   bkg = load_image('MenuPrincipal1.jpeg', 'images')

   # Set a background image - this is to show that the buttons will be
   # transparent around the text/image so it is safe to use this menu over a
   # picture - just make sure that the picture it will be written to is on the
   # screen that you pass into as the background for the menu when it is
   # created.  We must draw everything we want onto the surface before creating
   # the button if we want the background to be applied correctly.
   screen.blit(bkg, (0, 0))
   pygame.display.flip()

   # Create 3 diffrent menus.  One of them is only text, another one is only
   # images, and a third is -gasp- a mix of images and text buttons!  To
   # understand the input factors, see the menu file
   menu = cMenu(50, 50, 20, 5, 'vertical', 300, screen,
               [("Inicia Alex's Nightmare", 1, None),
                ('Tutorial',  2, None),
                ('Alex ql sin historia',    3, None),
                ('Salir del Juego',       4, None)])

   # Center the menu on the draw_surface (the entire screen here)
   menu.set_center(True, True)

   # Center the menu on the draw_surface (the entire screen here)
   menu.set_alignment('center', 'center')

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = 0
   prev_state = 1

   # rect_list is the list of pygame.Rect's that will tell pygame where to
   # update the screen (there is no point in updating the entire screen if only
   # a small portion of it changed!)
   rect_list = []

   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)

   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state

      # Get the next event
      e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
         if state == 0:
            rect_list, state = menu.update(e, state)
         elif state == 1:
            print 'Start Game!'
            sonido = pygame.mixer.Sound("Sonidos/Aceptar.wav")
            sonido.play()
            pygame.mixer.music.stop()
            Introduccion(e,screen)
            pygame.mixer.music.stop()
            import main
         elif state == 2:
            print 'Tutorial Game!'
            sonido = pygame.mixer.Sound("Sonidos/Aceptar.wav")
            sonido.play()
            Tutorial(screen)
            while 1:
               for e in pygame.event.get():
                  if e.key == pygame.K_x:
                     screen.blit(bkg, (0, 0))
                     pygame.display.flip()
                     state = 0
                     break
               break
         elif state == 3:
            print 'Options!'
            sonido = pygame.mixer.Sound("Sonidos/Aceptar.wav")
            sonido.play()
            import main
         else:
            print 'Exit!'
            sonido = pygame.mixer.Sound("Sonidos/Error.wav")
            sonido.play()
            pygame.quit()
            sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      # Update the screen
      pygame.display.update(rect_list)


## ---[ The python script starts here! ]----------------------------------------
# Run the script
if __name__ == "__main__":
   main()


#---[ END OF FILE ]-------------------------------------------------------------
