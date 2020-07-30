from plot import print_available_colors, single_horizontal_boxplot
import numpy as np

print_available_colors()

single_horizontal_boxplot(data = [np.random.rand(20) for _ in range(5)], 
                          xlabel = "X", 
                          box_colors = ["orange", "violet", "scatter green", "purple", "red"],
                          ylabel = "Y",
                          yticklabels = ["Method 1", "Method 2", "Method 3", "Method 4", "Method 5"],
                          figsize=(5,5),
                          title="Trial Boxplot",
                          xticklabels=["0.0", "0.5", "1.0"],
                          savename="trial_boxplot.png")