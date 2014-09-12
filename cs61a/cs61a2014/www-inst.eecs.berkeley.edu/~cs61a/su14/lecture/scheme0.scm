(define (loop0)
  (display "Scheme0> ")
  ; Force the "Scheme0> " to be displayed immediately
  (flush)
  ;; Remember, evaluation is innermost to outermost
  ;; (print (eval (read) (interaction-environment))) for Ikarus
  (print (eval (read)))
  (loop0))

;; (loop0)
;; 3
;; (+ 1 2)
;; (list 1 2 3)
;; (define (square x)
;;   (* x x))
;; (square 9)
;; ;; Ctrl-D ARGH HOW TO QUIT
;; (exit)


; Modify this to make it quit when the user types Ctrl-D
(define (loop1)
  (display "Scheme0> ")
  (flush)
  (print (eval (read)))
  (loop1))

;; (loop1)
;; (+ 2 3)
;; (list 1 2 3)
;; Ctrl-D
;; (trace eval)
;; (loop1)
;; (* 2 4)
;; (if (= 2 4) true false)
;; Ctrl-D
;; (define example-if '(if (= 2 4) true false))
;; (eval example-if)
;; (car example-if)
;; (list-ref example-if 2)
;; (caddr example-if)

(define (if-test exp)
  (list-ref exp 1))

(define (if-true-case exp)
  (list-ref exp 2))

(define (if-false-case exp)
  (list-ref exp 3))

(define (if? exp)
  (and (list? exp)
       (= (length exp) 4)
       (equal? (car exp) 'if)))

(define (bad-if? exp)
  (and (if? exp)
       (or (equal? (if-true-case exp) 'true)
	   (equal? (if-true-case exp) #t))
       (or (equal? (if-false-case exp) 'false)
	   (equal? (if-false-case exp) #f))))

; Fix pet peeve.
; Any occurrences of (if ___ true false) should be replaced by the blank.
(define (fix-pet-peeve exp)
  "Code here"
)

; Copy definition of loop1, then start fixing pet peeve
(define (loop2)
  "Code here"
)

;; (trace eval)  ; If not already traced
;; (loop2)
;; (if (= 2 4) true false)
;; (if (= 2 0) true 'nope)
;; (or (if (= 2 4) #t #f) false (if (= 2 2) #t #f))
