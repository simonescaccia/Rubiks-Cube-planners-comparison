import subprocess

SCORPION_PATH = "./planner25/scorpion.sif"
FAST_DOWNWARD_PATH = "./downward/fast-downward.py"
DOMAIN_RUBIKS_CUBE_PATH = "./domain-rubiks-cube/"

IDA_STAR_ADD_HEURISTIC = "--search 'iterated([astar(add())])'"
IDA_STAR_HMAX_HEURISTIC = "--search 'iterated([astar(hmax())])'"
IDA_STAR_FF_HEURISTIC = "--search 'iterated([astar(ff())])'"

SCORPION_CMD = SCORPION_PATH + " {domain_file} {problem_file} {plan_file}"
FAST_DOWNWARD_CMD = FAST_DOWNWARD_PATH + " {domain_file} {problem_file} {heuristic}"

DOMAIN_FILE = DOMAIN_RUBIKS_CUBE_PATH + "domain.pddl"
PROBLEM_FILE = DOMAIN_RUBIKS_CUBE_PATH + "problem1.pddl"

# code: 0 for scorpion, code: 1 for fast_downward
def get_plan_and_search_time(output: str, code: int):
    # find "search exit code"
    # if search exit code == 0
    # find "search time"
    # find plan
    # compare plan with optimal plan
    print(output)

command = FAST_DOWNWARD_CMD.format(domain_file=DOMAIN_FILE, problem_file=PROBLEM_FILE, heuristic=IDA_STAR_FF_HEURISTIC)
output = subprocess.run(command.replace("'",'').split(' '), capture_output=True)
get_plan_and_search_time(output, 1)