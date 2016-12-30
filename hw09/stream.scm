;; Sequence operations

;; Map f over s.
(define (map f s)
  (if (null? s)
      nil
      (cons (f (car s))
            (map f
                 (cdr s)))))

;; Filter s by f.
(define (filter f s)
  (if (null? s)
      nil
      (if (f (car s))
          (cons (car s)
                (filter f (cdr s)))
          (filter f (cdr s)))))

;; Reduce s using f and start value.
(define (reduce f s start)
  (if (null? s)
      start
      (reduce f
              (cdr s)
              (f start (car s)))))

;; Define range
(define (range a b)
  (if (>= a b)
    nil
    (cons a (range (+ a 1) b))
  )
)

;; define sum
(define (sum s)
  (reduce (lambda (x y) (+ x y)) s 0)
)

;; find prime
(define (prime? a)
  (define (prime-helper a t)
    (if (null? t)
      true
      (if (= 0 (remainder a (car t)))
        false
        (prime-helper a (cdr t))
      )
    )
  )
  (if (<= a 1) false (prime-helper a (range 2 a)))
)

;; summing primes between a and b
(define (sum-prime a b)
  (sum (filter (lambda (x) (prime? x)) (range a b)))
)

;; range-stream
(define (range-stream a b)
  (if (>= a b)
    nil
    (cons-stream a (range-stream (+ a 1) b))
  )
)

(define (prefix stream n)
  (if (= n 0)
    nil
    (cons (car stream) (prefix (cdr-stream stream) (- n 1)))
  )
)

(define (int-stream start)
  (cons-stream start (int-stream (+ start 1)))
)

(define (square-stream s)
  (cons-stream (* (car s) (car s)) (square-stream (cdr-stream s)))
)

(define ones (cons-stream 1 ones))

(define (sum-stream a b)
  (cons-stream (+ (car a) (car b)) (sum-stream (cdr-stream a) (cdr-stream b)))
)

(define ints (cons-stream 1 (sum-stream ints ones)))


;; Stream operations

;; Map f over s.
(define (map-stream f s)
  (if (null? s)
      nil
      (cons-stream (f (car s))
            (map-stream f
                 (cdr-stream s)))))

;; Filter s by f.
(define (filter-stream f s)
  (if (null? s)
      nil
      (if (f (car s))
          (cons-stream (car s)
                (filter-stream f (cdr-stream s)))
          (filter-stream f (cdr-stream s)))))

;; Reduce s using f and start value.
(define (reduce-stream f s start)
  (if (null? s)
      start
      (reduce-stream f
              (cdr-stream s)
              (f start (car s)))))

;; s is a stream that is already filtered by each element less that (car s)
;; SIEVES is ERATOSTHENES sieve
(define (sieves s)
  (cons-stream (car s)
    (sieves
      (filter-stream
        (lambda (x) (not (= 0 (remainder x (car s)))))
        (cdr-stream s)
      )
    )
  )
)

(define primes (sieves (int-stream 2)))
