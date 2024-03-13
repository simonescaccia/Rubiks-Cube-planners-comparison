;; Generated with ./domain-rubiks-cube/generator.py --output ./problems/problem3.pddl 3
(define
(problem rubiks-cube-shuffle-3)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 yellow red blue)
    (cube2 white red blue)
    (cube3 blue orange white)
    (cube4 green orange white)
    (cube5 yellow red green)
    (cube6 white red green)
    (cube7 blue orange yellow)
    (cube8 green orange yellow)
    (edge12 red blue)
    (edge24 white blue)
    (edge34 yellow orange)
    (edge13 yellow blue)
    (edge15 red white)
    (edge26 orange white)
    (edge48 green orange)
    (edge37 blue orange)
    (edge56 red green)
    (edge68 white green)
    (edge78 yellow red)
    (edge57 yellow green)
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