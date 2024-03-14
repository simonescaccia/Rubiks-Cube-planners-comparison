import subprocess
import re
import os
from datetime import datetime

# hyperparameters
PROBLEM_NUMBER = 10
TIME_LIMIT_SEC = 3600 # 1h

# paths
SCORPION_PATH = "./planner25/scorpion.sif"
FAST_DOWNWARD_PATH = "./downward/fast-downward.py"
DOMAIN_RUBIKS_CUBE_PATH = "./"
PROBLEM_RUBIKS_CUBE_PATH = "./problems/"
PLAN_PATH = "./plans/"
RESULTS_PATH = "./results/"
GENERATOR_PATH = "./domain-rubiks-cube/generator.py"

# heuristics
IDA_STAR_ADD_HEURISTIC = "iterated([astar(add())])"
IDA_STAR_HMAX_HEURISTIC = "iterated([astar(hmax())])"
IDA_STAR_FF_HEURISTIC = "iterated([astar(ff())])"

FAST_DOWNWARD_HEURISTICS = [IDA_STAR_ADD_HEURISTIC, IDA_STAR_HMAX_HEURISTIC, IDA_STAR_FF_HEURISTIC]

# planner commands
SCORPION_CMD = SCORPION_PATH + " {domain_file} {problem_file} {plan_file}"
FAST_DOWNWARD_CMD = FAST_DOWNWARD_PATH + " --search-time-limit {time_limit_sec} --plan-file {{plan_file}} {{domain_file}} {{problem_file}} --search {heuristic}"
GENERATOR_CMD = "python3 " + GENERATOR_PATH + " --output {problem_file} {moves_num}"

# info regex
SEARCH_EXIT_CODE_PATTERN = r"search exit code: (\d+)"
TOTAL_TIME_PATTERN = r"Total time: (\d+(?:\.\d+)?)s"
PLAN_LENGTH_PATTERN = r"Plan length: (\d+) step\(s\)"
PEAK_MEMORY_PATTERN = r"Peak memory: (\d+) KB"
GENERATED_STATES_PATTERN = r"Generated (\d+) state\(s\)"

# files
DOMAIN_FILE = DOMAIN_RUBIKS_CUBE_PATH + "domain.pddl"
PROBLEM_FILE = PROBLEM_RUBIKS_CUBE_PATH + "problem{number}.pddl"
PLAN_FILE = PLAN_PATH + "plan{number}.txt"
SCORPION_2023_FILE = RESULTS_PATH + "scorpion_2023.csv"
FAST_DOWNWARD_IDA_STAR_ADD_FILE = RESULTS_PATH + "fast_downward_ida_star_add.csv"
FAST_DOWNWARD_IDA_STAR_HMAX_FILE = RESULTS_PATH + "fast_downward_ida_star_hmax.csv"
FAST_DOWNWARD_IDA_STAR_FF_FILE = RESULTS_PATH + "fast_downward_ida_star_ff.csv"

RESULT_FILES = [SCORPION_2023_FILE, FAST_DOWNWARD_IDA_STAR_ADD_FILE, FAST_DOWNWARD_IDA_STAR_HMAX_FILE, FAST_DOWNWARD_IDA_STAR_FF_FILE]

FILE_COMMAND_MAP = {
    SCORPION_2023_FILE: SCORPION_CMD,
    FAST_DOWNWARD_IDA_STAR_ADD_FILE: FAST_DOWNWARD_CMD.format(time_limit_sec=TIME_LIMIT_SEC, heuristic=IDA_STAR_ADD_HEURISTIC),
    FAST_DOWNWARD_IDA_STAR_HMAX_FILE: FAST_DOWNWARD_CMD.format(time_limit_sec=TIME_LIMIT_SEC, heuristic=IDA_STAR_HMAX_HEURISTIC),
    FAST_DOWNWARD_IDA_STAR_FF_FILE: FAST_DOWNWARD_CMD.format(time_limit_sec=TIME_LIMIT_SEC, heuristic=IDA_STAR_FF_HEURISTIC)
}

# result files columns
COLUMNS = ["RANDOM_MOVES", "SEARCH_EXIT_CODE", "TOTAL_TIME", "PLAN_LENGTH", "PEAK_MEMORY", "GENERATED_STATES"]

def get_info(output: str):
    # find relevant info using regex
    search_exit_code = re.findall(SEARCH_EXIT_CODE_PATTERN, output)
    total_time = re.findall(TOTAL_TIME_PATTERN, output)
    plan_length = re.findall(PLAN_LENGTH_PATTERN, output)
    peak_memory = re.findall(PEAK_MEMORY_PATTERN, output)
    generated_states = re.findall(GENERATED_STATES_PATTERN, output)

    search_exit_code = search_exit_code[-1] if len(search_exit_code) > 0 else ''
    total_time = total_time[-1] if len(total_time) > 0 else ''
    plan_length = plan_length[-1] if len(plan_length) > 0 else ''
    peak_memory = peak_memory[-1] if len(peak_memory) > 0 else ''
    generated_states = generated_states[-1] if len(generated_states) > 0 else ''

    # print("search_exit_code:", search_exit_code)
    # print("total_time:", total_time)
    # print("plan_length:", plan_length)
    # print("peak_memory:", peak_memory)
    # print("generated_states:", generated_states)

    return (search_exit_code, total_time, plan_length, peak_memory, generated_states)

def run_command(command: str):
    command = command.split(' ') # transform the command into list
    return subprocess.run(command, capture_output=True, text=True)

def run_planner_command(command: str):
    print("\n" + command)
    print("timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    output = run_command(command)
    info = get_info(output.stdout)
    print("info:", info)
    return info

def get_last_problem_number(file_path: str):
    # read one csv and get the last problem number
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # check if the file has at least two lines
        if len(lines) < 2:
            return 0
        last_line = lines[-1]
        last_problem = last_line.split(",")[0]
        return int(last_problem)

def write_results(file_path: str, problem_number: int, results: tuple):
    # write results to file
    with open(file_path, 'a') as f:
        f.write(str(problem_number) + "," + ",".join(results) + "\n")

def align_planners():
    print("\nAligning planners problem number.")
    # select problem to start
    problem_number_list = [get_last_problem_number(file) + 1 for file in RESULT_FILES]
    # compute the minimum problem number
    min_problem_number = min(problem_number_list)
    # compute the maximum problem number
    max_problem_number = max(problem_number_list)
    # align problem numbers
    if min_problem_number != max_problem_number:
        # run planners with the minimum problem number
        for i in range(len(problem_number_list)):
            if problem_number_list[i] == min_problem_number:
                command = FILE_COMMAND_MAP[RESULT_FILES[i]]
                command = command.format(domain_file=DOMAIN_FILE, problem_file=PROBLEM_FILE.format(number=min_problem_number), plan_file=PLAN_FILE.format(number=min_problem_number))
                results = run_planner_command(command)
                write_results(RESULT_FILES[i], min_problem_number, results)
    return max_problem_number

def generate_problem_file(number: int):
    # generate the problem file
    print("\nGenerating problem file with ", number, " random moves.")
    command = GENERATOR_CMD.format(problem_file=PROBLEM_FILE.format(number=number), moves_num=number)
    run_command(command)

def run_planners():
    # align planners problem number if needed
    next_problem_number = align_planners()
    # check if all the problems are solved
    if next_problem_number > PROBLEM_NUMBER:
        return
    print("\nRunning planners from problem number ", next_problem_number, " to ", PROBLEM_NUMBER, ".")
    # run planners with the next problem number until all problems are solved    
    for i in range(next_problem_number, PROBLEM_NUMBER+1):
        # generate the problem file
        generate_problem_file(i)
        # run planners
        for file in RESULT_FILES:
            command = FILE_COMMAND_MAP[file]
            command = command.format(domain_file=DOMAIN_FILE, problem_file=PROBLEM_FILE.format(number=i), plan_file=PLAN_FILE.format(number=i))
            results = run_planner_command(command)
            write_results(file, i, results) 

def check_result_files():
    # check if the result files exist, if not create them
    for file in RESULT_FILES:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                f.write(",".join(COLUMNS) + "\n")


if __name__ == "__main__":
    # check if the the result files exist
    check_result_files()

    # run planners from the problem number
    run_planners()
