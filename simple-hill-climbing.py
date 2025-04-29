import numpy as np
import matplotlib.pyplot as plt

def generate_neighbors(x, step_size=1):
    return [x - step_size, x + step_size]

def hill_climbing(f, x0, max_iterations=1000):
    x = x0  # Initial solution
    iterations = 0
    path = [x]  # Track steps for visualization
    while iterations < max_iterations:
        neighbors = generate_neighbors(x)  # Generate neighbors of x
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):  # If the best neighbor is not better than x, stop
            return x, path
        x = best_neighbor  # Otherwise, continue with the best neighbor
        path.append(x)
        iterations += 1
    return x, path  # Return last found maximum if max_iterations is reached

if __name__ == "__main__":
    expr = input("Enter the function in terms of x (e.g., x**2 - 4*x + 4): ")
    f = lambda x: eval(expr, {"x": x})  # Convert input string to function
    x0 = int(input("Enter initial value: "))
    
    result, path = hill_climbing(f, x0)
    print("Local maximum found at x =", result)

    # Plot the function
    x_values = np.linspace(min(path)-10, max(path)+10, 400)
    y_values = [f(x) for x in x_values]
    
    plt.plot(x_values, y_values, label=f"Function: {expr}")
    plt.scatter(path, [f(x) for x in path], color='red', marker='o', label="Local Maxima")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Hill Climbing Algorithm Visualization")
    plt.legend()
    plt.grid()
    plt.show()
