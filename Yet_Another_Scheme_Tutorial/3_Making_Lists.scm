; Exercise 1
; Make data structures using cons that the front end responds like as follows.

; 1. ("hi" . "everybody")
(cons "hi" "everybody")

; 2. (0)
(cons 0 '())

; 3. (1 10 . 100)
(cons 1 (cons 10 100))

; 4. (1 10 100)
(cons 1 (cons 10 (cons 100 '())))

; 5. (#\I "saw" 3 "girls")
(cons #\I (cons "saw" (cons 3 (cons "girls" '()))))

; 6. ("Sum of" (1 2 3 4) "is" 10)
(cons "Sum of" (cons (cons 1 (cons 2 (cons 3 (cons 4 '())))) (cons "is" (cons 10 '()))))


; Exercise 2
; Evaluated following S-expressions.

; 1. (car '(0))
0

; 2. (cdr '(0))
()

; 3. (car '((1 2 3) (4 5 6)))
(1 2 3)

; 4. (cdr '(1 2 3 . 4))
(2 3 . 4)

; 5. (cdr (cons 3 (cons 2 (cons 1 '()))))
(2 1)
