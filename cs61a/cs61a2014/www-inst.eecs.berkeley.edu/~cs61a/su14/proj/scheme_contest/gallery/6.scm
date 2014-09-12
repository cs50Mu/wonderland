;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: The Kracken
;;;
;;; Description:
;;;   Take a paper strip
;;;   Fold it end over end times n
;;;   Unfold a dragon

;The next 3 functions are used to create a list of the dragon sequence
;Tail recursive list reversal and 
(define (new-reverse lst)
	(define (helper lst so-far)
    	(if (null? lst)
		so-far
		(let ((new-lst (cons (if (eq? (car lst) 'R) 'L 'R) so-far)))
	 	 (helper (cdr lst) new-lst))))
  	(helper lst '()))

;Takes a list of turns and creates the next iteration
(define (turns lst)
	(define new-lst (append lst (list 'R)))
	(append new-lst (new-reverse lst)))

;Recursive function to create a list of dragon fractal of iteration n
(define (create-iter n)
	(define (helper n lst)
		(if (< n 1) lst
			(helper (- n 1) (turns lst))))
	(helper n '()))

;Take a list of the dragon iteration and draw it out
(define (draw-dragon lst len)
	(if (null? lst) (forward len)
		(begin (forward len) 
			(if (eq? (car lst) 'R) (rt 90) (lt 90)) 
			(draw-dragon (cdr lst) len))))

;create and draw out a dragon spiral
(define (create-dragon len depth)
  (define dragon-lst (create-iter depth))
  (speed 0)
  (goto 0 0) (color "red")
  (draw-dragon dragon-lst len)
  (penup) (goto 0 0) (pendown) (color "black")
  (draw-dragon dragon-lst len)
  (penup) (goto 0 0) (pendown) (color "blue")
  (draw-dragon dragon-lst len)
  (penup) (goto 0 0) (pendown) (color "green")
  (draw-dragon dragon-lst len)
  (hideturtle))

(define (draw)
  ;If you were to call the create-dragon with anything past a depth of 5 or so
  ;it will take an exponentially LONG time to draw out since you are
  ;creating a list of size ((2^n) - 1)
  ;For exapmle (create-dragon 2 15) took over an hour to draw
  ;because it had a pattern list of ((2^15) - 1) ans turtle is slow as dirt.
  ;Look up dragon fractal if you want to know more about this pattern
  (create-dragon 3 12)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)
