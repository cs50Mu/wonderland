;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Recursive Probing 
;;;
;;; Description:
;;; 
;;; <An alien beam,
;;; 	So this is an abduction 
;;; 		No probe for god's sake.> 

(define (draw)
 	(speed 0)
	(penup)
	(bg "black")
	(define (loop0)
		(define (loop1 x loops1)
			(begin (forward 5) (left 15) (sp 100 0)
				(define (loop2 y loops2) 
					(if (= y -1000) (exitonclick) 
						(begin (forward (/ y 4))  (dot 5 "blue") (forward (/ y 4)) (penup) (dot 4 "green") (forward (/ y 4)) 
						(dot 4 "white") (forward (/ y 4)) (dot 2 "green") (left 269) (loop2 (- y 0.7) (- loops2 1)))))
				(loop2 x loops1)
		(exitonclick)
		(loop1 (/ x 2) (- loops1 .7))))
	(loop1 300 25))
	(loop0)
 (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)
