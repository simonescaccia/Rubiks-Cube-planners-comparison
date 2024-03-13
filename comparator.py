import subprocess

SCORPION_PATH = "./planner25/scorpion.sif"
FAST_DOWNWARD_PATH = "./downward/fast-downward.py"

IDA_STAR_ADD_HEURISTIC = "--search 'iterated([astar(add())])'"
IDA_STAR_HMAX_HEURISTIC = "--search 'iterated([astar(hmax())])'"
IDA_STAR_FF_HEURISTIC = "--search 'iterated([astar(ff())])'"

SCORPION_CMD = SCORPION_PATH + " {domain_file} {problem_file} {plan_file}"
FAST_DOWNWARD_CMD = FAST_DOWNWARD_PATH + " {domain_file} {problem_file} {heuristic}"

print(subprocess.run(["ls", "-l"], capture_output=True))