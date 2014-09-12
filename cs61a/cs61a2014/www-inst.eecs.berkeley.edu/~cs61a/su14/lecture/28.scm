(define (assert-equal test-num func-name actual-result expected-result)
  (display (string-append "Testing case " (number->string test-num) " for " func-name ": "))
  (if (not (equal? expected-result actual-result))
      (begin
	(display "Failed.") (newline)
	(display "Expected: ")
	(display expected-result)
	(display " Got: ")
	(display actual-result)
	(newline)
	(newline))
      (begin (display "Passed!") (newline))))

(define (count-atoms lst)
  'YOUR-CODE-HERE)

(assert-equal 1 "count-atoms"
	      (count-atoms '(s u 1 4))
	      4)
(assert-equal 2 "count-atoms"
	      (count-atoms '(((1 2) 3) 4 5 (9 (10))))
	      7)


(define (count-atoms-with-map lst-or-atom)
  (if (list? lst-or-atom)
      'YOUR-CODE-HERE
      'YOUR-CODE-HERE))

(assert-equal 1 "count-atoms-with-map"
	      (count-atoms-with-map '(s u 1 4))
	      4)
(assert-equal 2 "count-atoms-with-map"
	      (count-atoms-with-map '(((1 2) 3) 4 5 (9 (10))))
	      7)
