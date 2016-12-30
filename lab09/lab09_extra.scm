;; Extra Scheme Questions ;;

; Q5
(define (square x) (* x x))

(define (pow b n)
  (if (zero? n)
    1
    (if (even? n)
      (square (pow b (/ n 2)))
      ( * b (square (pow b (/ (- n 1) 2)))))))

; Q6
(define lst
  'YOUR-CODE-HERE
)

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q8
(define (remove item lst)
  (define (filter f lst)
    (if
      (zero? (length lst))
      lst
      (if
        (f (car lst))
        (cons (car lst) (filter f (cdr lst)))
        (filter f (cdr lst)))))
  (filter (lambda (x) (not (equal? item x))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (define max_ (max a b))
  (define min_ (min a b))
  (if (zero? min_)
    max_
    (if (zero? (modulo max_ min_))
      min_
      (gcd min_ (modulo max_ min_)))))

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q10
(define (no-repeats s)
  (if (zero? (length s))
    s
    (cons (car s) (no-repeats (remove (car s) (cdr s))))
  )
)

; Q11
(define (substitute s old new)
  (define (sub f lst)
    (if
      (zero? (length lst))
      lst
      (if (pair? (car lst))
        (cons (sub f (car lst)) (sub f (cdr lst)))
        (if (f (car lst))
          (cons (car lst) (sub f (cdr lst)))
          (cons new (sub f (cdr lst)))))))
  (sub (lambda (x) (not (equal? old x))) s))

; Q12
(define (sub-all s olds news)
  (if (zero? (length olds))
    s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)
