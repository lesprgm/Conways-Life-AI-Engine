from ga_solver import evolve_patterns

print("--- Running evolve_patterns with small parameters ---")

best_pattern, fitness_log = evolve_patterns()

print("\n evolve_patterns test run complete ")
print("Observed print statements above for verification.")
print(f"Returned best pattern (shape): {best_pattern.shape if best_pattern is not None else 'None'}")
print(f"Returned fitness history (length): {len(fitness_log)}")