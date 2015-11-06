import random

def main():
    while True:
        print "Welcome to the number guessing game!\n"
        print "I have my number..."
        
        n = 0
        while n < 5:
            guess_num = raw_input("What is your guess [1-10]? ")
            guess_num = int(guess_num)
            num = random.randint(1,10)
            if guess_num == num:
                print "You got it! Thanks for playing!\n"
                break
            else:
                if (guess_num > num):
                    print "That's too high. Try again!\n"
                else:
                    print "That's too low. Try again!\n"
            n = n + 1

        print "Replay"

if __name__ == "__main__":
    main()
