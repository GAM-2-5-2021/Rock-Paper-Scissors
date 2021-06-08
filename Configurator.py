import pygame
pygame.init()

display = pygame.display.Info()
windowWidth, windowHeight = display.current_w, display.current_h

framerate = 60

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font1 = pygame.font.SysFont("arial", 46, False, False)
font1Italic = pygame.font.SysFont("arial", 46, False, True)
font2 = pygame.font.SysFont("arial", 28, False, False)
font2Italic = pygame.font.SysFont("arial", 28, False, True)

window = pygame.display.set_mode((800, 800))  # Definira pygame prozor i njegove dimenzije

backgroundTrack = pygame.mixer.music.load('Multimedia/Music/BackgroundTrack.wav')  # Import pozadinske melodije
pygame.mixer.music.set_volume(0.3)  # Razina zvuka pozadinske melodije

def loadData():
    pygame.display.set_caption("Rock, Paper, Scissors")  # Postavlja naslov pygame prozora

    backgroundImage = pygame.image.load('Multimedia/Images/Background.jpeg')  # Importira sliku pozadine
    window.blit(backgroundImage, (0, 0))

    textBackgroundBar = pygame.Rect(0, 430, windowWidth, 120)
    pygame.draw.rect(window, (32, 32, 32), textBackgroundBar)

    welcomeTextTitle = font1.render("Rock, Paper, Scissors", True, white)
    window.blit(welcomeTextTitle, (400 - welcomeTextTitle.get_width() // 2, 440))

    pressEnterToStartText = font2Italic.render("~ Press ENTER to start ~", True, white)
    window.blit(pressEnterToStartText, (400 - pressEnterToStartText.get_width() // 2, 440 + welcomeTextTitle.get_height() + 10))
