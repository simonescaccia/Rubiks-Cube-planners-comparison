import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

RESULTS_PATH = "./results/"
PLOTS_PATH = "./plots/"


SCORPION_2023_FILE = RESULTS_PATH + "scorpion_2023.csv"
FAST_DOWNWARD_IDA_STAR_ADD_FILE = RESULTS_PATH + "fast_downward_ida_star_add.csv"
FAST_DOWNWARD_IDA_STAR_HMAX_FILE = RESULTS_PATH + "fast_downward_ida_star_hmax.csv"
FAST_DOWNWARD_IDA_STAR_FF_FILE = RESULTS_PATH + "fast_downward_ida_star_ff.csv"
OPTIMAL_SOLVER_FILE = RESULTS_PATH + "optimal_solver.csv"

RESULT_FILES = [SCORPION_2023_FILE, FAST_DOWNWARD_IDA_STAR_ADD_FILE, FAST_DOWNWARD_IDA_STAR_HMAX_FILE, FAST_DOWNWARD_IDA_STAR_FF_FILE]

# result files columns
COLUMNS = ["RANDOM_MOVES", "SEARCH_EXIT_CODE", "TOTAL_TIME", "PLAN_LENGTH", "PEAK_MEMORY", "GENERATED_STATES", "TIME_LIMIT_SEC", "MEMORY_LIMIT_MB"]

def compute_plot_1(data_x: list, data_y: dict):
    # plot 1
    # x-axis: optimal plan length, y-axis: plan length. 
    # Column chart, one column per planner for each problem. There is no column if the planner did not find a plan.
    data_y = data_y["PLAN_LENGTH"]
    # Set figure dimensions
    fig = plt.figure(figsize=(10, 6))  # Width = 10 inches, Height = 6 inches
    # create the plot
    bar_width = 0.2
    x_shift = [-bar_width, 0, bar_width, 2*bar_width]
    labels = ["scorpion_2023", "fast_downward_ida_star_add", "fast_downward_ida_star_hmax", "fast_downward_ida_star_ff"]
    y_ticks = 0
    for i, y in enumerate(data_y):
        y_ticks = max(y_ticks, max(data_y[y]))
        plt.bar([x + x_shift[i] for x in data_x], data_y[y], bar_width, label=labels[i])
    # set labels
    plt.xlabel('Optimal plan length')
    plt.ylabel('Plan length')
    # set x-ticks to match categories
    plt.xticks(data_x)
    plt.yticks(range(0, int(y_ticks+1), 1))
    # set title
    plt.title('Plan length by planner')
    # add background grid
    plt.grid(axis='both', linestyle='--')
    ax = plt.gca()
    ax.set_axisbelow(True)
    # add legend
    plt.legend()
    # save the plot
    plt.savefig(PLOTS_PATH + "plot1.png", dpi=300)

def compute_plot_2(data_x: list, data_y: dict):
    # plot 2
    # x-axis: optimal plan length, y-axis: peak memory usage. Compute peak_memory_usage/generated_states, so we can compute the number of bytes per state.
    # Column chart, one column per planner for each problem.
    data_y = data_y["PEAK_MEMORY"]
    # Set figure dimensions
    fig = plt.figure(figsize=(10, 6))  # Width = 10 inches, Height = 6 inches
    # create the plot
    bar_width = 0.2
    x_shift = [-bar_width, 0, bar_width, 2*bar_width]
    labels = ["scorpion_2023", "fast_downward_ida_star_add", "fast_downward_ida_star_hmax", "fast_downward_ida_star_ff"]
    y_ticks = 0
    # create the plot
    for i, y in enumerate(data_y):
        y_ticks = max(y_ticks, max(data_y[y]//1024))
        plt.bar([x + x_shift[i] for x in data_x], data_y[y]//1024, bar_width, label=labels[i])
    # set labels
    plt.xlabel('Optimal plan length')
    plt.ylabel('Peak memory usage (MB)')
    # set x-ticks to match categories
    plt.xticks(data_x)
    plt.yticks(range(0, int(y_ticks+1000), 1000))
    # set title
    plt.title('Peak memory usage by planner')
    # add background grid
    plt.grid(axis='both', linestyle='--')
    ax = plt.gca()
    ax.set_axisbelow(True)
    # add legend
    plt.legend()
    # save the plot
    plt.savefig(PLOTS_PATH + "plot2.png", dpi=300)

def compute_plot_3(data_x: list, data_y: dict):

    # plot 3
    # x-axis: optimal plan length, y-axis: total time.
    # Column chart, one column per planner for each problem. If search_exit_code is 23, set the time to the time limit.
    data_y_total_time = data_y["TOTAL_TIME"]
    search_exit_code = data_y["SEARCH_EXIT_CODE"]
    # Set figure dimensions
    fig = plt.figure(figsize=(10, 6))  # Width = 10 inches, Height = 6 inches
    # create the plot
    bar_width = 0.2
    x_shift = [-bar_width, 0, bar_width, 2*bar_width]
    labels = ["scorpion_2023", "fast_downward_ida_star_add", "fast_downward_ida_star_hmax", "fast_downward_ida_star_ff"]
    y_ticks = 0
    # create the plot
    # create the plot
    for i, y in enumerate(data_y):
        y_ticks = max(y_ticks, max(data_y[y]//1024))
        plt.bar([x + x_shift[i] for x in data_x], data_y[y]//1024, bar_width, label=labels[i])
    for y in data_y_total_time:
        data_y_list = data_y_total_time[y].copy()
        for i in range(len(data_y_list)):
            if search_exit_code[y][i] == 23:
                data_y_list[i] = 3600
        y_ticks = max(y_ticks, max(data_y_list))
        plt.bar([x + x_shift[i] for x in data_x], data_y[y], bar_width, label=labels[i])
    # set labels
    plt.xlabel('Optimal plan length')
    plt.ylabel('Total time (s)')
    # set x-ticks to match categories
    plt.xticks(data_x)
    plt.yticks(range(0, int(y_ticks+1000), 1000))
    # set title
    plt.title('Total time by planner')
    # add background grid
    plt.grid(axis='both', linestyle='--')
    ax = plt.gca()
    ax.set_axisbelow(True)
    # add legend
    plt.legend()
    # save the plot
    plt.savefig(PLOTS_PATH + "plot3.png")
    
def extract_info(results: list):
    tmp_data_x = {}
    data_y = {}
    data_y_search_exit_code = {}
    data_y_plan_length = {}
    data_y_peak_memory = {}
    data_y_total_time = {}
    for i, result in enumerate(results):
        # extract the relevant info
        tmp_data_x[RESULT_FILES[i]] = result["RANDOM_MOVES"]
        data_y_search_exit_code[RESULT_FILES[i]] = result["SEARCH_EXIT_CODE"]
        data_y_plan_length[RESULT_FILES[i]] = result["PLAN_LENGTH"]
        data_y_peak_memory[RESULT_FILES[i]] = result["PEAK_MEMORY"]
        data_y_total_time[RESULT_FILES[i]] = result["TOTAL_TIME"]
    # data_x is the same for all planners, so we can use the one with the most data
    data_x = tmp_data_x[max(tmp_data_x, key=lambda x: len(tmp_data_x[x]))]
    data_y["SEARCH_EXIT_CODE"] = data_y_search_exit_code
    data_y["PLAN_LENGTH"] = data_y_plan_length
    data_y["PEAK_MEMORY"] = data_y_peak_memory
    data_y["TOTAL_TIME"] = data_y_total_time
    return data_x, data_y

if __name__ == "__main__":
    # read the result files
    results = [pd.read_csv(file) for file in RESULT_FILES]
    # extract the relevant info
    data_x, data_y = extract_info(results)

    compute_plot_1(data_x, data_y)
    compute_plot_2(data_x, data_y)
    compute_plot_3(data_x, data_y)