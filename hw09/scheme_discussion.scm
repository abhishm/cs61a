(define (factorial n)
  (if (= n 0) 1 (* n (factorial (- n 1)))))

(define (fib n)
  (if (< n 2) n (+ (fib (- n 2)) (fib (- n 1))))
)

(define (concat a b)
  (if (null? a)
    b
    (cons (car a) (concat (cdr a) b))
  )
)

(define (replicate a n)
  (if (= n 0)
    nil
    (cons a (replicate a (- n 1)))
  )
)

(define (uncompress s)
  (if (null? s)
    nil
    (concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))
  )
)

(define (map fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map fn (cdr lst)))
  )
)

(define (deep-map fn lst)
  (cond
  ((not (list? lst)) (fn lst))
  ((null? lst) lst)
  ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
  ((not (list? (car lst))) (cons (fn (car lst)) (deep-map fn (cdr lst))))
  )
)

; Tree
(define (make_tree root branches) (cons root branches))

(define (root tree) (car tree))

(define (branches tree) (cdr tree))

(define (sum-list lst)
  (if (null? lst)
    0
    (+ (car lst) (sum-list (cdr lst)))
  )
)

(define t (make_tree 3 (list (make_tree 0 (list (make_tree 10 ()) (make_tree 2 ()))) (make_tree 8 ()) (make_tree -2
(list (make_tree -3 ()))))))

(define (tree-sum tree)
  (if (null? (branches tree))
    (root tree)
    (+ (root tree) (sum-list (map tree-sum (branches tree))))
  )
)

(define (map1 fn lst scale)
  (if (null? lst)
    nil
    (cons (fn (car lst) scale) (map1 fn (cdr lst) scale))
  )
)

(define (path-product-tree tree)
  (define (path-product-tree-helper tree scale)
    (if (null? tree) tree
        (make_tree (* (root tree) scale) (map1 path-product-tree-helper (branches tree) (* (root tree) scale)))
    )
  )
  (path-product-tree-helper tree 1)
)
