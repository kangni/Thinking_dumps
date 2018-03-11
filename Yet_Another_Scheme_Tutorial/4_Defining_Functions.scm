; Exercise 1
; Write following functions. They are quite simple but useful.

; 1. A function that add 1 to the argument.
(define add1
    (lambda (value)
    (+ value 1)))

; 2. A function that subtract 1 from the argument.
(define minus1
    (lambda (value)
    (- value 1)))


; Exercise 2
; Let's write a function to calculate flying distances with following steps.

; 1. Write a function that convert the unit of angles from degree to radian.
; 180 degree is π radian. π is defined by
(define pi
    (* 4 (atan 1.0)))

; 2. Write a function that calculates a distance of moving at a constant velocity (vx) in t seconds.
(define radian 
    (lambda (deg)
    (* deg (/ pi 180.0))))

; 3. Write a function that calculates a duration till the object reach the ground that is launched with vertical velocity of vy.
; Ignore air drag and use 9.8 m s-2 as the value of acceleration of gravity (g). 
; hint: As the vertical velocity when the object reaches the ground is -vy,
; 2 vy = g t 
; where t is the falling duration.
(define ff-time 
    (lambda (vy)
    (/ (* vy 2.0) 9.8)))

; 4. Write a function that calculates a flying distance of a ball thrown with an initial velocity v and an angle theta degree using functions defined in questions 1--3.
; Hint: First, convert degree to radian (say theta1). The horizontal and vertical initial velocities are represented by 
; v cos(theta1) and v sin(theta1), respectively. The duration of falling can be calculated by the function of the question 3. As horizontal velocity doesn't change, the distance can be calculated using the function of the question 2.
(define dx
    (lambda (vx t)
    (* vx t)))

; 5. Calculate the distance of a ball thrown with a initial velocity of 40 m s-1 and an angle of 30 degree. It corresponds to the distance of a long cast by a professional baseball player having a strong arm.
(define distance
    (lambda (v ang)
    (dx
        (* v (cos (radian ang)))
        (ff-time (* v (sin (radian ang)))))))