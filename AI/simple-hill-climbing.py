equation = input("Enter the equation in terms of x (example: -x**2 + 5): ")
initial_x = float(input("Enter the initial value of x: "))

def objective_function(x):
    return eval(equation)

def hill_climb(x):
    step_size = 0.1
    max_iterations = 100

    for _ in range(max_iterations):
        left = x - step_size
        right = x + step_size

        if objective_function(left) > objective_function(x):
            x = left
        elif objective_function(right) > objective_function(x):
            x = right
        else:
            break

    return x, objective_function(x)

best_x, best_value = hill_climb(initial_x)
print("Local maximum at x =", round(best_x, 4))
print("Maximum value =", round(best_value, 4))