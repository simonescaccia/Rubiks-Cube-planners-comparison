import subprocess
import re

SCORPION_PATH = "./planner25/scorpion.sif"
FAST_DOWNWARD_PATH = "./downward/fast-downward.py"
DOMAIN_RUBIKS_CUBE_PATH = "./"
PROBLEM_RUBIKS_CUBE_PATH = "./try-problems/"
PLAN_PATH = "./plans/"

IDA_STAR_ADD_HEURISTIC = "--search 'iterated([astar(add())])'"
IDA_STAR_HMAX_HEURISTIC = "--search 'iterated([astar(hmax())])'"
IDA_STAR_FF_HEURISTIC = "--search 'iterated([astar(ff())])'"

FAST_DOWNWARD_HEURISTICS = [IDA_STAR_ADD_HEURISTIC, IDA_STAR_HMAX_HEURISTIC, IDA_STAR_FF_HEURISTIC]

SCORPION_CMD = SCORPION_PATH + " {domain_file} {problem_file} {plan_file}"
FAST_DOWNWARD_CMD = FAST_DOWNWARD_PATH + " {domain_file} {problem_file} {heuristic}"

SEARCH_EXIT_CODE_PATTERN = r"search exit code: (\d+)"
SEARCH_TIME_PATTERN = r"Search time: (\d+\.\d+)s"
PLAN_LENGTH_PATTERN = r"Plan length: (\d+) step\(s\)"
PEAK_MEMORY_PATTERN = r"Peak memory: (\d+) KB"
GENERATED_STATES_PATTERN = r"Generated (\d+) state\(s\)"

DOMAIN_FILE = DOMAIN_RUBIKS_CUBE_PATH + "domain.pddl"
PROBLEM_FILE = PROBLEM_RUBIKS_CUBE_PATH + "problem1.pddl"
PLAN_FILE = PLAN_PATH + "plan1.pddl"

# code: 0 for scorpion, code: 1 for fast_downward
def get_plan_and_search_time(output: str, code: int):
    search_exit_code = re.findall(SEARCH_EXIT_CODE_PATTERN, output)
    search_time = re.findall(SEARCH_TIME_PATTERN, output)
    plan_length = re.findall(PLAN_LENGTH_PATTERN, output)
    peak_memory = re.findall(PEAK_MEMORY_PATTERN, output)
    generated_states = re.findall(GENERATED_STATES_PATTERN, output)

    search_exit_code = search_exit_code[-1] if len(search_exit_code) > 0 else ''
    search_time = search_time[-1] if len(search_time) > 0 else ''
    plan_length = plan_length[-1] if len(plan_length) > 0 else ''
    peak_memory = peak_memory[-1] if len(peak_memory) > 0 else ''
    generated_states = generated_states[-1] if len(generated_states) > 0 else ''

    print("search_exit_code:", search_exit_code)
    print("search_time:", search_time)
    print("plan_length:", plan_length)
    print("peak_memory:", peak_memory)
    print("generated_states:", generated_states)

    return search_exit_code, search_time, plan_length, peak_memory, generated_states

# command = FAST_DOWNWARD_CMD.format(domain_file=DOMAIN_FILE, problem_file=PROBLEM_FILE, heuristic=IDA_STAR_FF_HEURISTIC)
command = SCORPION_CMD.format(domain_file=DOMAIN_FILE, problem_file=PROBLEM_FILE, plan_file=PLAN_FILE)
output = subprocess.run(command.replace("'",'').split(' '), capture_output=True, text=True)
get_plan_and_search_time(output.stdout, 1)