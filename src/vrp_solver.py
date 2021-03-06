import pandas as pd
import random as rnd
from math import exp, log
import params
from lns import lns_class
import viz

def random_chance_of_accepting(repaired_routes, current_route, SA_Temp):
    """
    Prob of accepting a repaired route based on what the current SA temp is and also the difference in cost between that
    and the best route
    """


def simulated_annealing_init_temp(cost):
    """
    Function to calculate the SA temperature that would allow you to accept a solution that is control_temp above the
    best with a 50% prob
    """


def record_perf(record_perf_df, lns_iter_count, SA_Temp, current_route, best_route):
    perf_dict = {"iter": lns_iter_count,
                 "SA_temp": SA_Temp,
                 "route_cost": current_route.total_time,
                 "best_cost": best_route.total_time,
                 "route_num_vans": len(current_route.van_num_stops),
                 "best_num_vans": len(best_route.van_num_stops),
                 "route_drive_time": str([round(t[-1], 3) for t in current_route.van_times]),
                 "best_drive_time": str([round(t[-1], 3) for t in best_route.van_times])
                 }

    return record_perf_df.append(pd.DataFrame(perf_dict, index=[0]))

def run_vrp_solver(puzzle, init_route):
    rnd.seed(20201128)

    record_perf_df = pd.DataFrame()

    ### Initialise the SA algorithm

    lns_iter_count = 0
    while lns_iter_count < params.lns_max_iter:

        lns_iter_count += 1

        ### Run lns
        search = lns_class(puzzle, current_route, params.lns_destroy_frac, lns_iter_count)
        repaired_routes = search.run()

        ### Extra constraints?

        ### Simulated Annealing

        ### Print output
        # print(" Iter - %d \t\t Driving Time: \t\t Current = %.f \t\t Repaired = %.f \t\t Best = %.f  [min]" %
        #       (lns_iter_count, current_route.total_time, repaired_routes.total_time, best_route.total_time))

        ### Keep track for plots
        # record_perf_df = record_perf(record_perf_df, lns_iter_count, SA_Temp, current_route, best_route)

        ### Updating Simulated Annealing Temperature for next iteration


    ### Analysis and Save
    record_perf_df = record_perf_df.reset_index(drop=True)
    record_perf_df.to_csv(puzzle.output_path +"/solutions/vrp_performance.csv")

    # return best_route, record_perf_df
