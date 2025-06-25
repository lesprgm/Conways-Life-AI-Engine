from ga_solver import evolve_patterns

from main import plot_ga_history

from ga_parameters import ga_num_generations


print("--- Running evolve_patterns with small parameters ---")

best_pattern, fitness_log = evolve_patterns()

print("\n evolve_patterns test run complete ")
print("Observed print statements above for verification.")
print(f"Returned best pattern (shape): {best_pattern.shape if best_pattern is not None else 'None'}")
print(f"Returned fitness history (length): {len(fitness_log)}")

plot_ga_history(fitness_log)