; basic stream of 1, 2, 3
(define first (cons-stream 1 (cons-stream 2 (cons-stream 3 the-empty-stream))))

; infinite streams of ones and twos
(define ones (cons-stream 1 ones))
(define twos (cons-stream 2 twos))

; infinite stream of natural numbers
(define (make-nats n)
  (cons-stream n (make-nats (+ n 1))))

(define nats (make-nats 1))

; Helpful functions
; ss    (short for show-stream, outputs the first 10 elements of a stream)
; stream-ref (takes in an stream and an index and outputs the element)
(define (stream-add a b)
  (if (equal? a the-empty-stream)
      a
      (if (equal? b the-empty-stream)
          b
          (cons-stream (+ (stream-car a) (stream-car b))
                       (stream-add (stream-cdr a)
                                   (stream-cdr b)) )) ))

(define fib-stream
  (cons-stream 0
               (cons-stream 1
                            (stream-add fib-stream (stream-cdr fib-stream)))))

; HOW DO YOU WRITE ME? HINT: STREAM-MAP IS A THING
(define fact-stream
  (cons-stream 1
               (stream-map * fact-stream nats)))

(define divisible? (lambda (x y) (= 0 (remainder x y))))

(define (sieve stream)
  (cons-stream
    (stream-car stream)
    (sieve (stream-filter
             (lambda (x)
               (not (divisible? x (stream-car stream))))
             (stream-cdr stream)))))

(define primes (sieve (nats 2)))
