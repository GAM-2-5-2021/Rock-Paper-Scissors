from Configurator import *
import random

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.run = True  # Glavni uvjet za izvršavanje while petlje u main metodi
        self.gameStarted = False  # Boolean je li igrač pirisnuo Enter na početnom zaslonu
        self.isPlaying = False  # Boolean je li igra u tijeku ili ne
        self.playerDidChoose = False  # Boolean je li igrač napravio odabir
        self.playerChoice = "None"  # Odabir igrača
        self.computerChoice = "None"  # Random odabir računala

        #  Y koordinate prikazanih tekstova koje služe za njihovu animaciju  #
        self.yPositionOfChoseText = 0
        self.yPositionOfYouText = 0
        self.yPositionOfVsText = 0
        self.yPositionOfComputerText = 0

        self.result = ""  # Tekst koji se prikazuje na kraju svake partije
        self.playerScore = 0  # Rezultat igrača / Broj pobjeda igrača
        self.computerScore = 0  # Rezultat računala / Broj pobjeda računala

        self.playerHandImageIndex = 0  # Označava trenutno prikazanu sličicu igrača
        self.computerHandImageIndex = 0  # Označava trenutno prkazanu sličicu računala
        self.animationFinished = False  # Boolean je li animacija partije gotova

        self.drawnButtonRectangle = False;

        loadData()  # Učitava pygame i neke osnovne podatke za korištenje tog modula

        print("Loading...")

    def startGame(self):
        print("Started game")
        self.main()

    # Završava igru i zatvara pygame modul
    def gameOver(self):
        pygame.display.quit()
        pygame.quit()
        print("Quit pygame module")
        exit(1)

    # ------------------------ MAIN PETLJA ------------------------ #
    def main(self):
        #pygame.mixer.music.play(-1)
        while self.run:
            self.clock.tick(framerate)  # Postavlja framerate igre

            # Petlja koja prolazi kroz evente koje generira korisnik
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Provjerava je li korisnik klikuo na X za izlaz iz igre
                    self.run = False
                    self.gameOver()
                    print("Pressed X (exit)")

                # Dohvaća poziciju kursora kada igrač klikne na kamen, škare ili papir
                if event.type == pygame.MOUSEBUTTONDOWN and self.playerChoice == "None":
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if (mouseX >= 32 and mouseX <= 190 and mouseY >= 295 and mouseY <= 465):
                        self.playerChoice = "Rock"
                        self.drawButtonRectangle(32, 295, 190, 465, (252, 45, 241))
                    elif (mouseX >= 277 and mouseX <= 456 and mouseY >= 247 and mouseY <= 465):
                        self.playerChoice = "Paper"
                        self.drawButtonRectangle(277, 247, 456, 465, (0, 223, 184))
                    elif (mouseX >= 581 and mouseX <= 734 and mouseY >= 230 and mouseY <= 465):
                        self.playerChoice = "Scissors"
                        self.drawButtonRectangle(582, 230, 733, 465, (11, 124, 235))
                    else:
                        self.playerChoice = "None"

                if event.type == pygame.MOUSEBUTTONUP:
                    self.playerDidChoose = (self.playerChoice != "None")

                    self.computerChoice = self.generateComputerChoice()  # Generira odabir računala
                    self.result = self.calculateBattleResult()  # Izračun rezultata partije

                    # Postavlja indekse sličica na 0 kako bi animacija mogla započeti
                    self.playerHandImageIndex = 0
                    self.computerHandImageIndex = 0

            #  Poziva određene funkcije ovisno o pritisnutoj tipki  #
            keys = pygame.key.get_pressed()

            #  Igrač je kliknuo tipku ENTER
            if keys[pygame.K_RETURN]:
                pygame.time.delay(200)
                if (self.gameStarted):
                    self.isPlaying = True
                self.gameStarted = True

            #  Igrač je kliknuo tipku ESC
            if keys[pygame.K_ESCAPE]:
                self.run = False
                self.gameOver()
                print("Pressed ESC (exit)")

            #  Igrač je kliknuo tipku Y -> Ponovna igra
            if keys[pygame.K_y]:
                self.resetGameAttributes()  # Resetiranje vrijednosti za novu rundu

            #  Igrač je kliknuo tipku N -> Kraj igre
            if keys[pygame.K_n]:
                self.run = False
                self.gameOver()
                print("Game over")
                break
            
            self.redrawWindow()  # Ažurira pygame prozor

    #  Resetiranje vrijednosti za novu rundu  #
    def resetGameAttributes(self):
        self.playerDidChoose = False
        self.playerChoice = "None"
        self.computerChoice = "None"
        self.yPositionOfChoseText = 0
        self.yPositionOfYouText = 0
        self.yPositionOfVsText = 0
        self.yPositionOfComputerText = 0
        self.drawnButtonRectangle = False

    # Prikazuje pygame prozor i objekte u njemu
    def redrawWindow(self):
        if (self.gameStarted):
            self.drawInstructionsWindow()  # Prikazuje upute igre

        if (self.isPlaying):
            self.drawChooseHandWindow()  # Prikazuje prozor za odabir ruke

        if (self.playerDidChoose):
            self.drawWindowBattle()  # Prikaz krajnjeg dijela igre (animacija, ishod, rezultat)

        pygame.display.update()  # Ažurira prozor kako bi se vidjele napravljene promjene

    #  Prikazuje upute igre  #
    def drawInstructionsWindow(self):
        backgroundImage = pygame.image.load('Multimedia/Images/Instructions.jpeg')  # Importira sliku pozadine
        window.blit(backgroundImage, (0, 0))  # Postavlja sliku pozadine (Upute za igru)

        # Prikazuje pomoćni tekst za nastavak na igru
        pressEnterToStartText = font2Italic.render("~ Press ENTER to continue ~", True, white)
        window.blit(pressEnterToStartText, (400 - pressEnterToStartText.get_width() // 2, 735))

    #  Prikazuje prozor za odabir ruke  #
    def drawChooseHandWindow(self):
        backgroundImage = pygame.image.load('Multimedia/Images/ChooseHand.png')  # Importira sliku pozadine
        window.blit(backgroundImage, (0, 0))  # Postavlja sliku pozadine (Odabir ruke)

        # Prikazuje pomoćni tekst za odabir ruke
        chooseHandText = font1.render("Choose rock, paper or scissors", True, white)
        window.blit(chooseHandText, (400 - chooseHandText.get_width() // 2, self.yPositionOfChoseText))
        if (self.yPositionOfChoseText < 50):
            self.yPositionOfChoseText += 2  # Animacija pomoćnog teksta

    #  Prikaz krajnjeg dijela igre (animacija, ishod, rezultat)  #
    def drawWindowBattle(self):
        # Postavljanje pozadinske boje
        rect = pygame.Rect(0, 0, windowWidth, windowHeight)
        pygame.draw.rect(window, (255, 170, 105), rect)

        self.drawTitleText()  # Prikazivanje pomoćnih tekstova i njihova animacija
        self.animateBattle()  # Animiranje sličica ruke igrača i računala

        # Animacija je došla do kraja
        if (self.playerHandImageIndex == 7):
            self.showBattleResult()  # Prikazuje tekst s ishodom partije

    #  Prikazivanje pomoćnih tekstova i njihova animacija  #
    def drawTitleText(self):
        youText = font1.render("You", True, white)
        window.blit(youText, (400 - 250, self.yPositionOfYouText))
        if (self.yPositionOfYouText < 50):
            self.yPositionOfYouText += 2

        vsText = font1Italic.render("VS", True, white)
        window.blit(vsText, (400 - vsText.get_width() // 2, self.yPositionOfVsText))
        if (self.yPositionOfVsText < 50):
            self.yPositionOfVsText += 2

        computerText = font1.render("Computer", True, white)
        window.blit(computerText, (400 + 120, self.yPositionOfComputerText))
        if (self.yPositionOfComputerText < 50):
            self.yPositionOfComputerText += 2

    #  Animiranje sličica ruke igrača i računala  #
    def animateBattle(self):
        playerImage = pygame.image.load(
            'Multimedia/Images/Player/' + self.playerChoice + '/' + str(int(self.playerHandImageIndex // 1)) + '.png')
        playerImage = pygame.transform.scale(playerImage, (400, playerImage.get_height()))
        window.blit(playerImage, (0, 80))

        computerImage = pygame.image.load('Multimedia/Images/Computer/' + self.computerChoice + '/' + str(
            int(self.computerHandImageIndex // 1)) + '.png')
        computerImage = pygame.transform.scale(computerImage, (400, computerImage.get_height()))
        window.blit(computerImage, (800 - computerImage.get_width(), 80))

        # Svakih 1/60 (framerate je 60fps) sekundi indeks se poveća za 0.2, a sličica se promijeni svakih 5 frameova (1/12 sekundi)
        # Kada dođe do najvećeg mogućeg indeksa (7) više se ne mijenja kako bi se nastavila prikazivati zadnja sličica animacije
        self.playerHandImageIndex = 7 if (self.playerHandImageIndex + 0.2) > 7 else (self.playerHandImageIndex + 0.2) % 8
        self.computerHandImageIndex = 7 if (self.computerHandImageIndex + 0.2) > 7 else (self.computerHandImageIndex + 0.2) % 8

    #  Prikazuje tekst s ishodom partije  #
    def showBattleResult(self):
        textBackgroundBar = pygame.Rect(0, 520, windowWidth, 120)
        pygame.draw.rect(window, (28, 28, 28), textBackgroundBar)

        resultText = font1.render(self.result, True, white)
        window.blit(resultText, (400 - resultText.get_width() // 2, 530))

        playAgainText = font2Italic.render("~ Play again? (Y - Yes, N - No) ~", True, white)
        window.blit(playAgainText, (400 - playAgainText.get_width() // 2, 530 + resultText.get_height() + 10))

        #  Prikaz rezultata igrača i računala  #
        playerScoreText = font2.render("You: " + str(self.playerScore), True, white)
        window.blit(playerScoreText, (50, 700))
        computerScoreText = font2.render("Computer: " + str(self.computerScore), True, white)
        window.blit(computerScoreText, (50, 740))

    #  Prikazuje rub pravokutnika kako bi igrač stekao dojam da je kliknuo na gumb  #
    def drawButtonRectangle(self, x1, y1, x2, y2, color):
        buttonRect = pygame.Rect(x1 - 3, y1 - 3, x2 - x1 + 2 * 3, y2 - y1 + 2 * 3)
        pygame.draw.rect(window, color, buttonRect, 1)
        pygame.display.update()
        pygame.time.delay(50)

    #  Izračun ishoda igre  #
    def calculateBattleResult(self):
        if (self.playerChoice == self.computerChoice):
            return "It's a tie!"
        else:
            if (self.playerChoice == "Rock" and self.computerChoice == "Scissors"
                    or self.playerChoice == "Paper" and self.computerChoice == "Rock"
                    or self.playerChoice == "Scissors" and self.computerChoice == "Paper"):
                self.playerScore += 1
                return "You win!"
            elif (self.playerChoice == "Scissors" and self.computerChoice == "Rock"
                  or self.playerChoice == "Rock" and self.computerChoice == "Paper"
                  or self.playerChoice == "Paper" and self.computerChoice == "Scissors"):
                self.computerScore += 1
                return "You lose!"

    #  Nasumično generiranje odabira računala  #
    def generateComputerChoice(self):
        random_num = random.randint(0, 2)
        if random_num == 0:
            return "Rock"
        elif random_num == 1:
            return "Paper"
        elif random_num == 2:
            return "Scissors"
        else:
            return "None"
