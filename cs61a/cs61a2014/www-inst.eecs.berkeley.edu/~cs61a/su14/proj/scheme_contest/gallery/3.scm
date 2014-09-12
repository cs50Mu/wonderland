;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Cube Chains
;;;
;;; Description:
;;;    Chains of little cubes
;;;    Connected by the deep blue
;;;    That is what we are

(define (draw)
  (speed 0)
  (define (square s)
    (define (draw n)
      (if (> n 0)
        (begin (forward s) (right 90) (draw (- n 1)))))
    (draw 4))

  (define (base x y)
    (begin (right 45) (fd y) (right 45) (fd x)
    (left 45) (bk y) (right 45) (bk x) (left 90)))

  (define (cube s)
    (let ((y (* (/ 2 3) s)))
      (square s) (base s y)
      (fd s) (base s y) (bk s) (right 45)
      (fd y) (left 45) (square s)
      ))
  (define (draw-pretty num degrees size colors shape)
    (if (> num 0)
            (begin (color (car colors)) (shape size) (right degrees)
                   (draw-pretty (- num 1) degrees size
                   (append (cdr colors) (list (car colors))) shape))))
  (define (reset)
    (penup) (goto 0 0) (pendown))
  (penup)
  (goto -350 -350)
  (begin_fill)
  (pendown)
  (square 700)
  (end_fill)
  (reset)
  (draw-pretty 30 6 100 '("blue") square)
  (draw-pretty 30 6 100 '("blue") square)
  (define l1 '("darkred" "turquoise" "darkgreen" "purple" "darkorange" "darkblue"))
  (define l2 '("grey" "black" "black"))
  (define (lolz s lst)
    (define (dp)
      (draw-pretty 30 6 s lst cube)
      (draw-pretty 30 6 s lst cube))
  (seth 0)
  (reset)
  (dp)
  (seth 90)
  (penup)
  (reset)
  (pendown)
  (dp)
  (seth 180)
  (reset)
  (dp)
  (seth 270)
  (penup)
  (reset)
  (pendown)
  (dp)
  )
  (lolz 15 l2)
  (lolz 20 l1)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)