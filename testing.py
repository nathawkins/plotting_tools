from plot import *
import numpy as np

single_horizontal_boxplot(data = [np.abs(np.random.rand(20)) for _ in range(5)], 
                          xlabel = "X", 
                          box_colors = ["orange", "violet", "scatter green", "purple", "red"],
                          ylabel = "Y",
                          yticklabels = ["Method 1", "Method 2", "Method 3", "Method 4", "Method 5"],
                          figsize=(5,5),
                          title="Trial Boxplot",
                          xticklabels=["0.0", "0.5", "1.0"],
                          savename="trial_boxplot.png")

single_series_single_scatter_plot(xdata = np.abs(np.random.rand(10)), ydata = np.abs(np.random.rand(10)),
                                  show_comparison_line = True, 
                                #   xlabel = "X",
                                  color = "scatter pink",
                                  marker = "*",
                                #   ylabel = "Y",
                                  xticklabels=["0.0", "0.5", "1.0"],
                                  yticklabels=["0.0", "0.5", "1.0"],
                                  figsize=(5,5),
                                #   title="Single Series Scatter",
                                  savename="trial_single_series_scatter.png")

multiple_series_single_scatter_plot(xdata = [np.abs(np.random.rand(10)) for _ in range(5)], ydata = [np.abs(np.random.rand(10)) for _ in range(5)],
                                  colors = ["scatter green", "scatter blue", "scatter orange", "scatter pink", "red"],
                                  markers = ["o", ".", "*", "^", "v"],
                                  legend = True,
                                  figsize=(5,5),
                                  savename="trial_multiple_series_scatter.png")

single_series_multiple_scatter_plot_single_row(xdata = [np.abs(np.random.rand(10)) for _ in range(5)], ydata = [np.abs(np.random.rand(10)) for _ in range(5)],
                                  colors = ["scatter green", "scatter blue", "scatter orange", "scatter pink", "red"],
                                  markers = ["o", ".", "*", "^", "v"],
                                  figsize=(20,5),
                                  xticklabels=["0.0", "0.5", "1.0"],
                                  yticklabels=["0.0", "0.5", "1.0"],
                                  savename="trial_single_series_scatter_multiple_scatter.png")                                

multiple_horizontal_boxplot(data = [[np.abs(np.random.rand(20)) for _ in range(5)] for Z in range(4)], 
                          xlabel = "X", 
                          box_colors = ["orange", "violet", "scatter green", "purple", "red"],
                          ylabel = "Y",
                          yticklabels = ["Method 1", "Method 2", "Method 3", "Method 4", "Method 5"],
                          figsize=(20,5),
                          xticklabels=["0.0", "0.5", "1.0"],
                          savename="trial_multiple_boxplot.png")                                    