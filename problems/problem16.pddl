;; Generated with ./domain-rubiks-cube/generator.py --output ./problems/problem16.pddl 16
(define
(problem rubiks-cube-shuffle-16)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 yellow green red)
    (cube2 blue orange white)
    (cube3 blue white red)
    (cube4 red green white)
    (cube5 orange yellow green)
    (cube6 yellow red blue)
    (cube7 orange yellow blue)
    (cube8 orange green white)
    (edge12 red yellow)
    (edge24 red white)
    (edge34 yellow blue)
    (edge13 blue orange)
    (edge15 red green)
    (edge26 white blue)
    (edge48 green orange)
    (edge37 orange yellow)
    (edge56 yellow green)
    (edge68 green white)
    (edge78 blue red)
    (edge57 orange white)
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