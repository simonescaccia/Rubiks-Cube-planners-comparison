;; Generated with ./domain-rubiks-cube/generator.py --output ./problems/problem12.pddl 12
(define
(problem rubiks-cube-shuffle-12)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 yellow green red)
    (cube2 blue yellow orange)
    (cube3 orange yellow green)
    (cube4 blue white orange)
    (cube5 blue white red)
    (cube6 green white red)
    (cube7 yellow red blue)
    (cube8 orange green white)
    (edge12 red white)
    (edge24 white orange)
    (edge34 yellow green)
    (edge13 yellow blue)
    (edge15 green white)
    (edge26 white blue)
    (edge48 green red)
    (edge37 orange yellow)
    (edge56 blue orange)
    (edge68 orange green)
    (edge78 red blue)
    (edge57 red yellow)
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
