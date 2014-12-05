import random
from operator import add, sub, pow, mul
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc

Base = declarative_base()

class Player(Base):
    __tablename__ = "highscores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

engine = create_engine("sqlite:///players.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)

print("Welcome to the 'Do you even math?' game!")
print("Here are your options:")
print("-start")
print("-highscores")
print("-exit")

exit = False
while not exit:
    player_input = input("Please enter a command: ").lower()
    if player_input == "start":
        username = str(input("Enter your username: "))
        print("Welcome {}. Let the game begin!".format(username))
        answers = 0

        notOver = True
        while notOver:
            question_number = answers + 1
            print("Question {}.".format(question_number))
            operations_available = (add, sub, mul)
            random_operation = random.choice(operations_available)
            if random_operation == add:
                print_operation = "+"
            elif random_operation == sub:
                print_operation = "-"
            # elif random_operation == pow:
            #     print_operation = "^"
            elif random_operation == mul:
                print_operation = "*"

            if answers < 20:
                first_variable = random.randint(1, 10)
                second_variable = random.randint(1, 10)
            elif answers < 60:
                first_variable = random.randint(11, 25)
                second_variable = random.randint(1, 10)
            elif answers < 40:
                first_variable = random.randint(1, 100)
                second_variable = random.randint(1, 25)
            answer = random_operation(first_variable, second_variable)

            print("What is the answer to: {} {} {} = ?".format(first_variable, print_operation, second_variable))

            user_answer = input()
            if user_answer == str(answer):
                answers += 1
                print("Correct!")
            else:
                result = answers * answers
                print("Incorrect! Ending game. Your score is: {}".format(result))
                notOver = False
                session.add(Player(name=username, score=result))
                session.commit()
    elif player_input == "highscores":
        top10 = session.query(Player).order_by(desc(Player.score)).all()
        pos_index = 1
        for player in top10:
            print("{}. {} with {} points.".format(pos_index, player.name, player.score))
            pos_index += 1
            if pos_index > 10:
                break
    elif player_input == "exit":
        exit = True
    else:
        print("Not a valid command. Try agian.")
