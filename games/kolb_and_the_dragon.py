import time
import sys
import keyboard 

###########################
### KOLB AND THE DRAGON ###
###########################



class Game():
    def __init__(self):
        self.skip_text = False

    def waiting(self, num_dots=3, delay=1):
        for _ in range(num_dots):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(delay)

    def typer(self, text, delay=0.05):
        for char in text:
            if self.skip_text:
                sys.stdout.write(text[text.index(char):])
                sys.stdout.flush()
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        self.skip_text = False

    def welcome_page(self):

        print("\n\n")
        self.typer("                     .----------------.  .----------------.  .----------------.  .----------------.                     ", 0.0025)
        self.typer("                    | .--------------. || .--------------. || .--------------. || .--------------. |                    ", 0.0025)
        self.typer("                    | |  ___  ____   | || |     ____     | || |   _____      | || |   ______     | |                    ", 0.0025)
        self.typer("                    | | |_  ||_  _|  | || |   .'    `.   | || |  |_   _|     | || |  |_   _ \    | |                    ", 0.0025)
        self.typer("                    | |   | |_/ /    | || |  /  .--.  \  | || |    | |       | || |    | |_) |   | |                    ", 0.0025)
        self.typer("                    | |   |  __'.    | || |  | |    | |  | || |    | |   _   | || |    |  __'.   | |                    ", 0.0025)
        self.typer("                    | |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__/ |  | || |   _| |__) |  | |                    ", 0.0025)
        self.typer("                    | | |____||____| | || |   `.____.'   | || |  |________|  | || |  |_______/   | |                    ", 0.0025)
        self.typer("                    | |              | || |              | || |              | || |              | |                    ", 0.0025)
        self.typer("                    | '--------------' || '--------------' || '--------------' || '--------------' |                    ", 0.0025)
        self.typer("                     '----------------'  '----------------'  '----------------'  '----------------'                     ", 0.0025)
        self.typer("                                                   .----------------.                                                   ", 0.0025)
        self.typer("                                                  | .--------------. |                                                  ", 0.0025)
        self.typer("                                                  | |    ___       | |                                                  ", 0.0025)
        self.typer("                                                  | |  .' _ '.     | |                                                  ", 0.0025)
        self.typer("                                                  | |  | (_) '___  | |                                                  ", 0.0025)
        self.typer("                                                  | |  .`___'/ _/  | |                                                  ", 0.0025)
        self.typer("                                                  | | | (___)  \_  | |                                                  ", 0.0025)
        self.typer("                                                  | | `._____.\__| | |                                                  ", 0.0025)
        self.typer("                                                  | |              | |                                                  ", 0.0025)
        self.typer("                                                  | '--------------' |                                                  ", 0.0025)
        self.typer("                                                   '----------------'                                                   ", 0.0025)
        self.typer("                               .----------------.  .----------------.  .----------------.                               ", 0.0025)
        self.typer("                              | .--------------. || .--------------. || .--------------. |                              ", 0.0025)
        self.typer("                              | |  _________   | || |  ____  ____  | || |  _________   | |                              ", 0.0025)
        self.typer("                              | | |  _   _  |  | || | |_   ||   _| | || | |_   ___  |  | |                              ", 0.0025)
        self.typer("                              | | |_/ | | \_|  | || |   | |__| |   | || |   | |_  \_|  | |                              ", 0.0025)
        self.typer("                              | |     | |      | || |   |  __  |   | || |   |  _|  _   | |                              ", 0.0025)
        self.typer("                              | |    _| |_     | || |  _| |  | |_  | || |  _| |___/ |  | |                              ", 0.0025)
        self.typer("                              | |   |_____|    | || | |____||____| | || | |_________|  | |                              ", 0.0025)
        self.typer("                              | |              | || |              | || |              | |                              ", 0.0025)
        self.typer("                              | '--------------' || '--------------' || '--------------' |                              ", 0.0025)
        self.typer("                               '----------------'  '----------------'  '----------------'                               ", 0.0025)
        self.typer(" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.", 0.0025)
        self.typer("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |", 0.0025)
        self.typer("| |  ________    | || |  _______     | || |      __      | || |    ______    | || |     ____     | || | ____  _____  | |", 0.0025)
        self.typer("| | |_   ___ `.  | || | |_   __ \    | || |     /  \     | || |  .' ___  |   | || |   .'    `.   | || ||_   \|_   _| | |", 0.0025)
        self.typer("| |   | |   `. \ | || |   | |__) |   | || |    / /\ \    | || | / .'   \_|   | || |  /  .--.  \  | || |  |   \ | |   | |", 0.0025)
        self.typer("| |   | |    | | | || |   |  __ /    | || |   / ____ \   | || | | |    ____  | || |  | |    | |  | || |  | |\ \| |   | |", 0.0025)
        self.typer("| |  _| |___.' / | || |  _| |  \ \_  | || | _/ /    \ \_ | || | \ `.___]  _| | || |  \  `--'  /  | || | _| |_\   |_  | |", 0.0025)
        self.typer("| | |________.'  | || | |____| |___| | || ||____|  |____|| || |  `._____.'   | || |   `.____.'   | || ||_____|\____| | |", 0.0025)
        self.typer("| |              | || |              | || |              | || |              | || |              | || |              | |", 0.0025)
        self.typer("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |", 0.0025)
        self.typer(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ", 0.0025)
        
        print("\n\n\n")
        self.waiting(3, 0.5), print("\n")
        self.waiting(3, 0.5), print("\n")
        self.waiting(3, 0.5), print("\n")
        print("\n\n")

        self.typer('Kolb was a brave Nord warrior. One day his Chief asked Kolb to slay an evil dragon that threatened their village. "Go through the mountain pass, Kolb", his Chief said. "You will find the Dragon on the other side."\n')
        self.waiting(3, 0.5), print("\n")
        self.typer('Kolb took his favorite axe and shield and walked to the pass, where he found a cold cave, a windy cave, and a narrow trail.\n')
        self.waiting(3, 0.5), print("\n")
        print("1: Enter the cold cave.") 
        print("2: Enter the windy cave.")
        print("3: Walk up the trail")
        print("\n")
        input("Enter your choice (1-3): ")  

    # def page_2(self):
    
    # def page_3(self):

    # def page_4(self):

    # def page_5(self):

    # def page_6(self):

    # def page_7(self):

    # def page_8(self):

    # def page_9(self):

    # def page_10(self):

    # def page_11(self):

    # def page_12(self):

    # def page_13(self):
    
    # def page_14(self):

    # def page_15(self):

    # def page_16(self):

    # def page_17(self):


    def game_loop(self):

        keyboard.on_press_key("space", lambda _: self.skip_typing())                                     

        play = True 

        while play:
            current_page = "welcome_page"
            while True:
                if current_page == "welcome_page":
                    current_page, play = self.welcome_page()

    def skip_typing(self):
        self.skip_text = True

    def start_game(self):
        self.game_loop()


if __name__ == "__main__":
    game = Game()
    game.start_game()