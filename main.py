#!/usr/bin/python3

from Ship import Ship

def main():
    theship = Ship()
    finished = False
    count = 0
    print(f"--Turn {count}--")
    theship.setup()
    count += 1
    while True:
        print(f"--Turn {count}--")
        finished = theship.take_turn()
        count += 1
        if finished:
            break






if __name__=="__main__":
    main()
