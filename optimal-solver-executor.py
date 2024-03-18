import os
import subprocess
import re

OPTIMAL_SOLVER_PATH = "./domain-rubiks-cube/optimal-solver/"
RESULTS_PATH = "./results/"
PROBLEM_RUBIKS_CUBE_PATH = "./problems/"

PROBLEM_FILE = PROBLEM_RUBIKS_CUBE_PATH + "problem{number}.pddl"
PDDL_TO_SOLVER_INPUT_FILE = OPTIMAL_SOLVER_PATH + "pddl-to-solver-input.py"

OPTIMAL_SOLVER_FILE = RESULTS_PATH + "optimal_solver.csv"

OPTIMAL_SOLVER_EXECUTABLE = OPTIMAL_SOLVER_PATH + "optimal-solver"

PLAN_COST_PATTERN = r"Cost: (\d+)"

COLUMNS = ["PROBLEM_NUMBER", "COST"]

# variables
optimal_solver_inputs = {}

def check_result_files():
    # check if the result files exist, if not create them
    if not os.path.exists(OPTIMAL_SOLVER_FILE):
        with open(OPTIMAL_SOLVER_FILE, 'w') as f:
            f.write(",".join(COLUMNS) + "\n")

def get_next_problem_number():
    # read the result file and get the last problem number
    with open(OPTIMAL_SOLVER_FILE, 'r') as f:
        lines = f.readlines()
        # check if the file has at least two lines
        if len(lines) < 2:
            return 1
        last_line = lines[-1]
        last_problem_number = int(last_line.split(",")[0])
        return last_problem_number + 1

def run_command(command: str):
    command = command.split(' ') # transform the command into list
    return subprocess.run(command, capture_output=True, text=True)

def generate_optimal_solver_inputs(problem_number):
    # generate the optimal solver inputs
    command = "python3 " + PDDL_TO_SOLVER_INPUT_FILE + " " + PROBLEM_FILE.format(number=problem_number)
    results = run_command(command)
    return results.stdout

def store_optimal_solver_inputs():
    # get the next problem number (optimal_solver)
    next_problem_number = get_next_problem_number()
    while(True):
        # check if the problem file exists
        problem_file = PROBLEM_FILE.format(number=next_problem_number)
        if not os.path.exists(problem_file):
            break
        # generate the optimal solver inputs
        optimal_solver_input = generate_optimal_solver_inputs(next_problem_number)
        # save the optimal solver inputs
        optimal_solver_inputs[next_problem_number] = optimal_solver_input
        # check next problem number
        next_problem_number += 1

def run_optimal_solver():
    # Send the inputs to the process
    for key in optimal_solver_inputs:
        print("optimal_solver, problem:", key)    
        # start the optimal solver
        command = [OPTIMAL_SOLVER_EXECUTABLE]
        # Run the command, and establish communication with the process
        process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Wait for the process to prompt for input
        stdout, _ = process.communicate(input=optimal_solver_inputs[key])
        # get the cost from the output
        cost = re.findall(PLAN_COST_PATTERN, stdout)
        cost = cost[0] if cost else ""
        # write the cost to the result file
        with open(OPTIMAL_SOLVER_FILE, 'a') as f:
            f.write(str(key) + "," + str(cost) + "\n")

def run_planner():
    # store the optimal solver inputs
    store_optimal_solver_inputs()
    # make the optimal solver
    command = "make -C " + OPTIMAL_SOLVER_PATH
    run_command(command)
    # run the optimal solver and communicate with it
    run_optimal_solver()    

if __name__ == "__main__":
    # check if the the result files exist
    check_result_files()

    # run planner from the problem number
    run_planner()