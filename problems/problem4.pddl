;; Generated with ./domain-rubiks-cube/generator.py --output ./problems/problem4.pddl 4
(define
(problem rubiks-cube-shuffle-4)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 white blue red)
    (cube2 yellow orange blue)
    (cube3 blue red yellow)
    (cube4 green orange white)
    (cube5 white blue orange)
    (cube6 white red green)
    (cube7 orange green yellow)
    (cube8 red green yellow)
    (edge12 orange blue)
    (edge24 yellow blue)
    (edge34 yellow orange)
    (edge13 red yellow)
    (edge15 white blue)
    (edge26 orange white)
    (edge48 green orange)
    (edge37 blue red)
    (edge56 red green)
    (edge68 white green)
    (edge78 green yellow)
    (edge57 red white)
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