; Demo: Tail Recursion - Scheme

(define (fib n)
  ; Note how we define the helper function inside fib
  (define (helper n a b)
    (if (= n 0)
	a
	(helper (- n 1) b (+ a b))))
  (helper n 0 1))

(define (fact-recursive n)
  (if (= n 0)
      1
      (* n (fact-recursive (- n 1)))))

(define (fact n)
  (define (helper counter product)
    (if (= counter n)
	(* n product)
	(helper (+ counter 1) (* product counter))))
  (helper 1 1))


; Demo: More Tail Recursion

(define (reverse lst)
  (define (helper lst so-far)
    (if (null? lst)
	so-far
	(let ((new-lst (cons (car lst) so-far)))
	  (helper (cdr lst) new-lst))))
  (helper lst '()))

; Tail recursive map
(define (map f lst)
  (define (map-reverse lst so-far)
    (if (null? lst)
	so-far
	(let ((new-lst (cons (f (car lst)) so-far)))
	  (map-reverse (cdr lst) new-lst))))
  (reverse (map-reverse lst '())))

; Another tail recursive map
(define (map f lst)
  (define (helper lst so-far)
    (if (null? lst)
	so-far
	(let ((new-lst (append so-far (list (f (car lst))))))
	  (helper (cdr lst) new-lst))))
  (helper lst '()))



; Demo:  The Beauty of Map and Accumulate
(define (deep-reverse lst-or-atom)
  (if (list? lst-or-atom)
      (reverse (map deep-reverse lst-or-atom))
      lst-or-atom))

; Note: Accumulate is like reduce in Python
(accumulate + 0 '(2 3 4))
(accumulate append '() '((1) (2 3 4) (5 6)))

(define (deep-sum lst-or-num)
  (if (list? lst-or-num)
      (accumulate + 0 (map deep-sum lst-or-num))
      lst-or-num))
