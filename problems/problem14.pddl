;; Generated with ./domain-rubiks-cube/generator.py --output ./problems/problem14.pddl 14
(define
(problem rubiks-cube-shuffle-14)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 orange blue white)
    (cube2 blue red yellow)
    (cube3 green white orange)
    (cube4 green red yellow)
    (cube5 blue white red)
    (cube6 blue orange yellow)
    (cube7 white red green)
    (cube8 green orange yellow)
    (edge12 white green)
    (edge24 green yellow)
    (edge34 red yellow)
    (edge13 green red)
    (edge15 red white)
    (edge26 red blue)
    (edge48 orange blue)
    (edge37 yellow orange)
    (edge56 blue yellow)
    (edge68 orange white)
    (edge78 green orange)
    (edge57 blue white)
)
(:goal
    (and
        (cube1 red white blue)
        (cube2 orange white blue)
        (cube3 red yellow blue)
        (cube4 orange yellow blue)
        (cube5 red white green)
        (cube6 orange white green)
        (cube7 red yellow green)
        (cube8 orange yellow green)

        (edge12 white blue)
        (edge24 orange blue)
        (edge34 yellow blue)
        (edge13 red blue)

        (edge15 red white)
        (edge26 orange white)
        (edge48 orange yellow)
        (edge37 red yellow)

        (edge56 white green)
        (edge68 orange green)
        (edge78 yellow green)
        (edge57 red green)

    )
)
)
