;; Generated with ./domain-rubiks-cube/generator.py --output ./problems/problem10.pddl 10
(define
(problem rubiks-cube-shuffle-10)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 orange yellow blue)
    (cube2 orange yellow green)
    (cube3 orange white blue)
    (cube4 red yellow green)
    (cube5 yellow blue red)
    (cube6 white green orange)
    (cube7 red green white)
    (cube8 red blue white)
    (edge12 red blue)
    (edge24 blue yellow)
    (edge34 red white)
    (edge13 yellow red)
    (edge15 green red)
    (edge26 orange yellow)
    (edge48 white orange)
    (edge37 white green)
    (edge56 orange blue)
    (edge68 yellow green)
    (edge78 blue white)
    (edge57 green orange)
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