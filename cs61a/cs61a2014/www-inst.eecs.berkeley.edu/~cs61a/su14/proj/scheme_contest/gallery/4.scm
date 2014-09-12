;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Strange Loop  (inspired by "I am a Strange Loop" by Douglas Hofstadter )
;;;
;;; Description:
;;;   In the end, we are:
		;self-inventing mirages
		;of self-reference

(define (draw)
  
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)

		
(define (fib n)
  (if (<= n 2)
      1
      (list (+ (fib (- n 1)) (fib (- n 2))))))


(define (new-circle n)

	(circle n)

	
	(if (< n 90)
		1
		(new-circle (- n 10))))







(new-circle 100)
(right 50)
(forward 50)
	
	
		

(a-circle 20)
; (penup)
(setposition 100 0)
; (right 40)
(pendown)
(circle 100)


; (setpostion 100 100)
; (right 50)
; (a-circle 75)
; (setposition 150 150)
; (new-circle 100)


; (def (tree b)
; 	(if (> b 5)
; 		(forward b)
; 		(right 20)
; 		(tree (- b 15))
; 		(left 40)
; 		(tree (- b 15))
; 		(right 20)
; 		(backward b)))

; (def (tree-draw)
; 	(color green)
; 	(left 90)
; 	(backward 100)
; 	(tree 75))

; (tree-draw)




	