;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Spinning Illusion 
;;;
;;; Description:
;;;   You may ask ...
;;;   Where is the Illusion
;;;   Stare at the middle
;;;   Bring your head closer
;;;   Rubberduck

(define (init)
	(bgcolor "#000000")
	(setup 1000 800 0 0)
	(hideturtle)
	(mode "logo")
	(pensize 0.1)
	(speed 10))

(define bsize 20)

(define color-g
	;green
	"#A0C39E")
(define color-r
	;red
	"#AF7871")
(define color-y
	;yellow
	"#D7CA93")
(define pcolor
	;gray
	"#808080")

(define (draw)
	(init)
	(back-groud)
	(draw-box)
	(draw-circle)
	(exitonclick))

(define (draw-box)
	(pat1 0 0 color-g color-r color-y pcolor)
	(pat2 0 0 color-g color-r color-y pcolor)
	(pat3 0 0 color-g color-r color-y pcolor)
	(pat4 0 0 color-g color-r color-y pcolor)
	(pat5 0 0 color-g color-r color-y pcolor)
	(pat6 0 0 color-g color-r color-y pcolor)
	(pat7 0 0 color-g color-r color-y pcolor)
	(pat8 0 0 color-g color-r color-y pcolor)
	)

(define (pat1 starx stary c1 c2 c3 c4)
	; middle back
	(setposition starx stary) (set-up 0 0 c1 c2 c3 c4)
	(setposition starx stary) (set-l 0 0 c1 "#917972" c3 c4)
	(setposition starx stary) (set-r 0 0 c1 c2 c3 c4)
	)

(define (pat2 starx stary c1 c2 c3 c4)
	; upper
	(setposition starx stary) (set-up -3.5 -3.5 c1 "#776D6B" c3 c4)
	(setposition starx stary) (set-l -5.5 -5.5 c1 "#917972" c3 c4)
	(setposition starx stary) (set-r -5.5 -5.5 c1 c2 "#AB9C7F" c4)
	(setposition starx stary)
	)


(define (pat3 starx stary c1 c2 c3 c4)
	; down left
	(setposition starx stary) (set-l 0 2.5 c1 c2 c3 c4)
	(setposition starx stary) (set-up 0 5.5 c1 c2 c3 c4)
	(setposition starx stary) (set-r 0 5.5 c1 c2 "#AB9C7F" c4)
	(setposition starx stary)
	)

(define (pat4 starx stary c1 c2 c3 c4)
	; up left
	(setposition starx stary) (set-l -5.5 -3 c1 c2 c3 c4)
	(setposition starx stary) (set-up -3.5 2 c1 c2 c3 c4)
	(setposition starx stary) (set-r -5.5 0 c1 c2 "#AB9C7F" c4)
	(setposition starx stary)
	)

(define (pat5 starx stary c1 c2 c3 c4)
	; down right
	(setposition starx stary) (set-r 2.5 0 c1 c2 c3 c4)
	(setposition starx stary) (set-up 5.5 0 c1 "#A07E70" c3 c4)
	(setposition starx stary) (set-l 5.5 0 c1 "#917972" c3 c4)
	(setposition starx stary)
	)

(define (pat6 starx stary c1 c2 c3 c4)
	; up right
	(setposition starx stary) (set-r -3 -5.5 c1 c2 c3 c4)
	(setposition starx stary) (set-up 2 -3.5 c1 "#776D6B" c3 c4)
	(setposition starx stary) (set-l 0 -5.5 c1 "#917972" c3 c4)
	(setposition starx stary)
	)

(define (pat7 starx stary c1 c2 c3 c4)
	; down
	(setposition starx stary) (set-l 5.5 2.5 c1 c2 c3 c4)
	(setposition starx stary) (set-r 2.5 5.5 c1 c2 c3 c4)
	(setposition starx stary) (set-up 5.5 5.5 c1 c2 c3 c4)
	(setposition starx stary)
	)

(define (pat8 starx stary c1 c2 c3 c4)
	; middle frount
	(setposition starx stary) (set-r -3 0 c1 c2 c3 c4)
	(setposition starx stary) (set-l 0 -3 c1 c2 c3 c4)
	(setposition starx stary) (set-up 2 2 c1 c2 c3 c4)
	)

(define (set-up x-cor y-cor cor1 cor2 cor3 pcor)
	(pu) (seth 120) (fd (* x-cor bsize)) 
	(seth 240) (fd (* y-cor bsize)) (pd)
	(cube cor1 cor2 cor3 pcor) (seth 0) (fd bsize)
	(cube cor1 cor2 cor3 pcor) (seth 0) (fd bsize)
	(cube cor1 cor2 cor3 pcor)
	(pu)
	)

(define (set-l x-cor y-cor cor1 cor2 cor3 pcor)
	(pu) (seth 120) (fd (* x-cor bsize))
	(seth 240) (fd (* y-cor bsize)) (pd)
	(seth 240) (fd bsize) (cube cor1 cor2 cor3 pcor)
	(seth 240) (fd bsize) (cube cor1 cor2 cor3 pcor)
	(pu)
	)

(define (set-r x-cor y-cor cor1 cor2 cor3 pcor)
	(pu) (seth 120) (fd (* x-cor bsize))
	(seth 240) (fd (* y-cor bsize)) (pd)
	(seth 120) (fd bsize) (cube cor1 cor2 cor3 pcor)
	(seth 120) (fd bsize) (cube cor1 cor2 cor3 pcor)
	(pu)
	)

(define (cube color-1 color-2 color-3 pen-color)
	(pencolor pen-color)
	(pensize 1)
	(rhombus1 color-1) (rhombus2 color-2) (rhombus3 color-3)
	)

(define (rhombus1 color)
	(fillcolor color)
	(begin_fill)
	(seth 90) (left 30) (fd bsize) (left 120) (fd bsize)
	(left 60) (fd bsize) (left 120) (fd bsize) (end_fill)
	)

(define (rhombus2 color)
	(fillcolor color)
	(begin_fill)
	(seth 270) (right 30) (fd bsize) (left 120) (fd bsize)
	(left 60) (fd bsize) (left 120) (fd bsize) (end_fill)
	)

(define (rhombus3 color)
	(fillcolor color)
	(begin_fill)
	(seth 90) (left 30) (fd bsize) (right 120) (fd bsize)
	(right 60) (fd bsize) (right 120) (fd bsize) (end_fill)
	)

(define (draw-circle)
	(pensize 2)
	(speed 10)
	(patter-box 300 36 17 right)
	(patter-box 220 26 -13 left))

(define (circle-box-draw radius num-of-box angle turn)
	(define (helper count)
		(setpos 0 0)
		(cond ((> count 0) (left (/ 720 num-of-box)) (pu) 
			  (fd radius) (pd) (left angle) (box 30 turn) 
			  (right angle) (pu) (helper (- count 1)))))
	(helper (/ num-of-box 2)))

(define (box n turn)
	(fillcolor "#8F8F8F")
	(begin_fill)
	(pensize 2) (pencolor "#FFFFFF") (fd n) (pencolor "#5E5E5E") (turn 120) 
	(pensize 1) (fd n) (pencolor "#5E5E5E") (turn 60) (pensize 1) (fd n) 
	(pencolor "#FFFFFF") (turn 120) (pensize 2) (fd n) (turn 60)
	(end_fill)
	)

(define (patter-box radius num-of-box angle turn)
	(circle-box-draw radius num-of-box angle turn)
	(left (/ 360 num-of-box))
	(circle-box-draw radius num-of-box angle turn)
	)

(define (back-groud)
	(hideturtle) (speed 10)
	(drawrr 0 0) (drawrr 0 60) (drawrr 0 120)
	(drawrr 0 180) (drawrr 0 240) (drawrr 0 300)
	)

(define (shap length count)
	(left 80)
	(pencolor "#404040")
	(cond ((< length 1000) (pensize 1) (fd length) 
		(shap (* length 1.3) (+ count 1))))
	)

(define (drawrr angle starang)
	(define (helper angle)
		(cond ((< angle 12) (seth starang) (left angle) (setposition 0 0)
		(pd) (shap 20 0) (pu)
		(helper (+ angle 1)))))
	(helper angle))

; Please leave this last line alone.  You may add additional procedures above
; this line.  All Scheme tokens in this file (including the one below) count
; toward the token limit.
(draw)
