;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Taijitu>
;;;
;;; Description:
;;;   <Pure black and pure white
;;;    Yin in Yang and Yang in Yin
;;;    Perfect harmony>

(define (draw)
  (define (helper startx starty scale depth last)
    (if (> depth 2) 
        (begin
         (pu)
         (color last)
         (goto startx starty)
         (pd)
         (begin_fill)
         (circle scale)
         (end_fill))
        (begin
        (pu)
        (goto startx starty) 
        (pd)
        (seth 0)
        (color "black")
        (circle scale)
        (begin_fill)
        (circle scale 180)
        (end_fill)
        (pu) 
        (goto startx starty) 
        (pd) 
        (right 180)
        (begin_fill)
        (circle (/ scale 2) -180)
        (end_fill)
        (color "white")
        (begin_fill)
        (circle (- (/ scale 2)) -180)
        (end_fill)
        (helper startx (+ starty (/ (* 4 scale) 3)) (/ scale 6) (+ 1 depth) "black")
        (helper startx (+ starty (/ (* 2 scale) 3)) (/ scale 6) (+ 1 depth) "white"))
    )
  )
  (ht)(helper 0 (- 250) 250 0 "white")
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)
