def students_checker(name):
    students = ['1',
                '3',
                '5',
                '7']
    if name in students: print "Yes, that student is enrolled in the class!"
    else: print "No, that student is not in the class."


def main():
    print "Welcome to the student checker!"
    while True:
        name = raw_input("Please give me the name of a student (enter 'q' to quit): ")
        if name == 'q':
            break
        students_checker(name)

    print "\n"
    print "Goodbye!"

if __name__ == "__main__":
        main()
#TODO: How to use return True & False to judgment? that I cann't fix it right now
