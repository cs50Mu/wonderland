; SCHEME CHEATSHEET
; Remember, this is a comment

; PAIRS
; cons -> make a pair
; car  -> get the first thing in a pair
; cdr  -> get the second thing in a pair

; LISTS
; Recall that linked lists is defined as follows:
;   - either the empty list OR
;   - a pair whose car can be anything
;     and whose cdr must be another list
; We won't use link in Scheme, but instead just directly use cons.
; Remember that link just called cons
; 
; Useful functions to know
; null?  -> check if a list is empty
; list?  -> is my argument a proper linked list?
; cons   -> same cons as above. Takes an element and a list and
;           makes a new list
; list   -> makes a list of its arguments
; append -> takes n linked LISTS and joins them together
;           like the + operator for PYTHON lists

(define (map f lst)
  (if (null? lst)
      '()
      (cons (f (car lst))
            (map f (cdr lst)) )))

(define (list-ref lst index)
  (cond ((null? lst) (error "List too short"))
        ((= index 0) (car lst))
        (else (list-ref (cdr lst) (- index 1))) ))

(define (broken-reverse lst)
  (if (null? lst)
      '()
      (cons (reverse (cdr lst))
            (car lst) )))

 (define (reverse lst)
   (if (null? lst)
       '()
       (append (reverse (cdr lst))
               (list (car lst)) )))

 (define (deep-reverse lst)
   (cond ((null? lst) '())
         ((list? (car lst))
           (append (deep-reverse (cdr lst))
                   (list (deep-reverse (car lst))) ))
         (else
           (append (deep-reverse (cdr lst))
                   (list (car lst)) )) ))

; Deep reverse using let
; let gives us local variables that can be used inside the body of the let
; makes things more readable, but also saves us from making the same
; procedure calls (i.e. calling (car lst) more than once)
(define (deep-reverse lst)
  (if (null? lst)
      '()
      (let ((first (car lst))
            (new-rest (deep-reverse (cdr lst))))
        (if (list? first)
            (append new-rest (list (deep-reverse first)))
            (append new-rest (list first)) )) ))
