;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Sunflower
;;;
;;; Description:
;;;   <Each flower tried to
;;;    Eat the sun; all burnt to crisps.
;;;    The star plots revenge...>



(define (repeat n func)
  (if (> n 0)
      (begin (func) (repeat (- n 1) func))))

(define (find-base len wdt degree)
  (- wdt (* 2 len (sin degree))))

(define (filled-scale len wdt degree)
  (begin_fill)
  (blank-scale len wdt degree)
  (end_fill))

(define (blank-scale len wdt degree)
  (fd len)
  (right (+ 90 degree))
  (fd wdt)
  (right (+ 90 degree))
  (fd len)
  (right (- 90 degree))
  (fd (find-base len wdt degree))
  (left degree)
  (fd (find-base len wdt degree))
  (right (- 90 (* 2 degree))))

(define (draw-scales len wdt degree)
  (filled-scale len wdt degree) ; black
  (blank-scale len wdt degree) ; white
  (filled-scale len wdt degree) ; black
  (blank-scale len wdt degree)) ; white

(define (draw-sunflower fn count len wdt degree)
  (cond ((<= count 1))
        ((= (modulo count 2) 0) (begin (fn len wdt degree) (draw-sunflower fn (/ count 2) (+ len 5) wdt degree)))
        (else (begin len wdt degree) (draw-sunflower fn (+ 1 (* 3 count)) len wdt (- degree 1)))))

(define (draw)
  (speed 0)    
  (setpos 200 0)
  (seth 180)
  (clear)
  (pu)
  (define (draw-item-at position)
      (if (< position 5)
          (begin
              (repeat 11 (lambda () (draw-sunflower draw-scales 9 2 1 1)))
              (fd 150)
              (right 65)
              (fd 150)
              (draw-item-at (+ position 1)))))
  (draw-item-at 0)
  (exitonclick))



; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)