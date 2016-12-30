test = {
  'name': 'Question 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Pair(2, nil), env)
          4b7283d4dfa392633549336acb032de7
          # locked
          >>> eval_all(Pair(4, Pair(5, nil)), env)
          39dba75757e21a295c7803a12e1e5877
          # locked
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> lst = Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, nil)))))
          >>> eval_all(lst, env)
          5
          >>> lst     # The list should not be mutated!
          Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, nil)))))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          63a2a5d7b5e29dd3e3dd3f5593bca3ba
          # locked
          scm> (begin (define x 3) x)
          ed2605996ac3b24d98b27c6d58145f06
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          2080f557b7b94a00a65c3971a7aa3007
          # locked
          # choice: (+ 2 2)
          # choice: '(+ 2 2)
          # choice: 4
          # choice: 30
          scm> (define x 0)
          c55ea5b1bca40acd76b8c213f8a08f8b
          # locked
          scm> (begin 42 (define x (+ x 1)))
          c55ea5b1bca40acd76b8c213f8a08f8b
          # locked
          scm> x
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
