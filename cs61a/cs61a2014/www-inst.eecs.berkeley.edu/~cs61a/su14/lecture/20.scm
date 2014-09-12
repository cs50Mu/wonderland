;; Demo: Scheme Basics
42
(+ 2 3)
(* 2014 2014)
(* (/ 48 2) (+ 9 3))
(/ 48 (* 2 (+ 9 3)))
+
"+"
'+
(define pi 3.14159)
pi
'pi

true
false
#t
#f
(= 2 2)
(< 2 9)
(> 2 9)
(<= 2 5)
(<= 5 5)
(<= 9 5)




; Demo: More Scheme Basics

(if (= 2 2)
    'equal
    'notequal)

(define (square x)
  (* x x))
(square 2014)
square
(define square (lambda (x) (* x x)))
(square 3)
square

(define (analyze x)
  (if (< x 0)
      'negative
      (if (= x 0)
	  'zero
	  'positive)))

(analyze -3)
(analyze 9)
(analyze 0)

(define (analyze x)
  (cond ((< x 0) 'negative)
	((= x 0) 'zero)
	(else 'positive)))


; Demo: Recursion in Scheme

(define (fact n)
  (if "check for base case here"
      1  ; No need for a return
      (* n "recursive call here")))

; (fact 4)



; Demo: Linked Lists and Pairs

(cons 1 2)
(cons 1 2 3)
(list 1 2 3)
'(1 2 3)
(define x (list 1 2 '(3 4) 5))
x
(car x)
(cdr x)
(car (cdr x))
(cadr x)
(caddr x)
(caaddr x)
(cdaddr x)
(list-ref x 3)
(list-ref x 2)
(append x (list 6 7))
x

(map square '(1 5 9))
(map (lambda (x) (+ x 1)) '(2 4 6))
(map car '((1 2) (3 4) (5 6)))
(filter even? '(9 3 8 2))
