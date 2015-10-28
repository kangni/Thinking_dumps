# -*- coding: utf-8 -*-
# #  Author:
# #  2015/10/25 PM 4:00

def main():
    states = dict()
    while True:
        name = raw_input("Please give me the name of the student (q to quit): ")
        if name == 'q':
            break
        grade = raw_input("Please give me their grade: ")
        states[name] = [grade]

    print "Okay, printing grades!\n"
    print "Student  Grade"
    for name, grade in states.items():
        print name, ':', grade


if __name__ == "__main__":
        main()
