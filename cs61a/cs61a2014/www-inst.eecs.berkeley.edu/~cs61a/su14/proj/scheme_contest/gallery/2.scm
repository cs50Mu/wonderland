;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Do you even square?
;;;
;;; Description:
;;;    We present to you
;;;    Genertic Recursive Art
;;;    Sponsored by no skill. 

(define (repeat k fn) (if (> k 0)
                            (begin (fn) (repeat (- k 1) fn))
                            nil))

(define (polygon length sides)
    (define angle (- 180 (/ (* 180 (- sides 2)) sides)))
    (pendown)
    (repeat sides (lambda () 
                 (fd length)
                 (rt angle)))
    (penup))

(define (recursive loops length sides color-num depth)
    (color (change-color color-num))
    (cond ((< length 24) 'done)
        ((> loops 0) (shape (- loops 1) (* length 0.96) sides color-num depth))
        (else (recursive 10 length sides (- color-num 1) (- depth 1)))))

(define (shape loops length sides color-num depth)
    (rt 6)
    (polygon length sides)
    (recursive loops length sides color-num depth))

(define (change-color n)
    (cond ((= n 1) "#919191")
        ((= n 2) "#b6b6b6")
        ((= n 3) "#dadada")
        ((= n 4) "#ffffff")))

(define (draw)
    (penup)
    (speed 180)
    (bgcolor "black")
    (pendown)
    (begin (seth 270) (recursive 150 1500 4 1 11) 
        (seth 180) (recursive 150 1500 4 2 11)
        (seth 90) (recursive 150 1500 4 3 11)
        (seth 0) (recursive 150 1500 4 4 11))
    (hideturtle)
    (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)


