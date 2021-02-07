# Write your code here
import random


class RockPaperScissors:

    def __init__(self):
        self.score = 0
        self.name = input('Enter your name ')

    def user_name(self):
        print('Hello' + ', ' + self.name)

    def text_file(self):
        # file with users score and name
        with open('rating.txt', 'r') as rating_file:

            for line in rating_file:
                if self.name in line:
                    self.score = int(line.split(' ')[1])

            if self.score == 0:
                print(self.name, self.score, '\n', file=rating_file)

    def update_score(self):
        # updating score in the file
        with open('rating.txt', 'a+') as r:
            for count, line in enumerate(r):
                if self.name in line:
                    line[count] = (self.name + ' ' + str(self.score) + '\n')

    def rock_paper_scissors(self):

        options = ['rock', 'paper', 'scissors']

        while True:
            user_choice = input()
            computer_choice = random.choice(options)

            # repeated data
            win = 'Well done. The computer chose', computer_choice, 'and failed'
            lose = 'Sorry, but the computer chose', computer_choice
            draw = 'There is a draw', computer_choice

            # game logic
            # scissors
            if user_choice.lower() == 'scissors':
                if computer_choice == 'rock':
                    print(lose)
                elif computer_choice == 'paper':
                    print(win)
                    self.score += 100
                else:
                    print(draw)
                    self.score += 50
            # paper
            elif user_choice.lower() == 'paper':
                if computer_choice == 'scissors':
                    print(lose)
                elif computer_choice == 'rock':
                    print(win)
                    self.score += 100
                else:
                    print(draw)
                    self.score += 50
            # rock
            elif user_choice.lower() == 'rock':
                if computer_choice == 'paper':
                    print(lose)
                elif computer_choice == 'scissors':
                    print(win)
                    self.score += 100
                else:
                    print(draw)
                    self.score += 50
            # show rating
            elif user_choice.lower() == '!rating':
                print('Your rating: ', self.score)
            # exit choice
            elif user_choice == '!exit':
                print('Bye!')
                break
            else:
                print('Invalid input')


new_game = RockPaperScissors()
new_game.user_name()
new_game.text_file()
new_game.rock_paper_scissors()
new_game.update_score()
