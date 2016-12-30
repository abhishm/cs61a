(define (find s predicate)
  (cond
    ((null? s) #f)
    ((predicate (car s)) (car s))
    (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  (if (null? s) (nil)
                (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k))
  )
)

(define (has-cycle s)
  (define (has-cycle-helper slow fast)
    (cond
      ((null? fast) #f)
      ((null? (cdr-stream fast)) #f)
      ((eq? slow fast) #t)
      (else (has-cycle-helper (cdr-stream slow) (cdr-stream (cdr-stream fast))))
    )
  )
  (has-cycle-helper s (cdr-stream s))
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
