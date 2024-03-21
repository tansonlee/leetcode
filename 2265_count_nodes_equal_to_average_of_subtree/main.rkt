; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (average-of-subtree root)
  (-> (or/c tree-node? #f) exact-integer?)

  (define (recursive-case node)
    (define left-info (helper (tree-node-left node)))
    (define right-info (helper (tree-node-right node)))
    
    (define total-sum (+ (first left-info) (first right-info) (tree-node-val node)))
    (define total-count (+ (second left-info) (second right-info) 1))
    (define result (+ (third left-info) (third right-info)))

    (if (= (floor (/ total-sum total-count)) (tree-node-val node))
      (list total-sum total-count (+ result 1))
      (list total-sum total-count result)))

  (define (helper node)
    (if (false? node)
        (list 0 0 0)
        (recursive-case node)))

  (third (helper root)))
