> (skip '(1 2 3 4) 2) ; [1, 2, 3, 4][::2]
(1 3)
> (skip '(1 2 3 4 5) 3)
(1 4)

(define (skip lst n)
  (if (null? lst)
      '()
      (if (< (length lst) n)
          (list (car lst))
          (cons (car lst)
                (skip (helper lst n) n) )) ))

(define (helper lst n)
  (if (= n 0)
      lst
      (helper (cdr lst) (- n 1)) ))
