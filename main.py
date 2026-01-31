#!/usr/bin/python3

from Ship import Ship

def main():
    theship = Ship()
    finished = False
    count = 0
    while count < 5:
        theship.setup(count)
        count += 1
    while True:
        theship.take_turn()
        count += 1
        if finished:
            break
        if count > 10:
            break





if __name__=="__main__":
    main()
