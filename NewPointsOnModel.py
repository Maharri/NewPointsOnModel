import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to generate 2D point cloud
def generate_point_cloud(n):
    np.random.seed(0)  # For reproducibility
    x = np.random.uniform(0, 10, n)
    y = 2 * x + 1 + np.random.normal(0, 1, n)
    return x, y

# Function to perform ordinary least squares regression
def ols(x, y):
    slope, intercept, _, _, _ = linregress(x, y)
    return slope, intercept

# Function to plot data and regression line
def plot_data_and_line(x, y, slope, intercept):
    plt.scatter(x, y, color='blue', label='Original data')
    plt.plot(x, slope * x + intercept, color='red', label='OLS line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Original Data and OLS Line')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to add points on the regression line
def add_points_on_line(x, y, slope, intercept, n_points):
    x_new = np.random.uniform(min(x), max(x), n_points)  # Random x-values along the line
    y_new = slope * x_new + intercept
    return x_new, y_new

# Function to append the new points to the dataset
def append_points(x, y, x_new, y_new):
    x = np.concatenate((x, x_new))
    y = np.concatenate((y, y_new))
    return x, y

# Function to print regression statistics
def print_regression_stats(slope, intercept):
    print("Slope:", slope)
    print("Intercept:", intercept)
    print()

# Main function
def main():
    # Generate original point cloud
    x, y = generate_point_cloud(3)

    # Perform OLS on original data
    slope, intercept = ols(x, y)

    # Plot original data and regression line
    plot_data_and_line(x, y, slope, intercept)

    # Add points on the regression line
    x_new, y_new = add_points_on_line(x, y, slope, intercept, 10)

    # Append the new points to the dataset
    x, y = append_points(x, y, x_new, y_new)

    # Perform OLS on augmented data
    slope_new, intercept_new = ols(x, y)

    # Plot augmented data and new regression line
    plot_data_and_line(x, y, slope_new, intercept_new)

    # Print regression statistics for both regression lines
    print("Original Regression:")
    print_regression_stats(slope, intercept)
    print("Augmented Regression:")
    print_regression_stats(slope_new, intercept_new)

if __name__ == "__main__":
    main()
