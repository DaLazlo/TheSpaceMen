#!/usr/bin/python3

from Ship import Ship

def main():
    theship = Ship()
    finished = False
    count = 0
    while not finished:
        theship.take_turn(count)
        count += 1






if __name__=="__main__":
    main()
