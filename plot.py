import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
from colr import color

colors = {"k":"#000000",
          "orange":"#FF9736", 
          "violet":"#ECE7F2",
          "light blue":"#A1BFDA",
          "darker blue":"#008EBD",
          "purple":"#8859A6",
          "red":"#C73C41",
          "scatter green":"#009D78",
          "scatter orange":"#E77B42",
          "scatter blue":"#7877B5",
          "scatter pink":"#F1348F",
          "ggplot gray":"#999999", 
          "ggplot orange":"#E69F00", 
          "ggplot sky":"#56B4E9", 
          "ggplot green":"#009E73", 
          "ggplot yellow":"#F0E442", 
          "ggplot blue":"#0072B2", 
          "ggplot red":"#D55E00", 
          "ggplot pink":"#CC79A7"}

def print_available_colors(colors = colors):
    print("Colors available in palette.")
    for k in colors.keys():
        print(f"{k}\t{colors[k]}\t{color('    ', fore = colors[k], back = colors[k])}")

def single_horizontal_boxplot(data, figsize = (6,5), xlabel = "", ylabel = "", axis_label_fontsize = 14, title = "",
            title_fontsize = 16, xticks = [], xticklabels = [], xticklabels_fontsize = 12, 
            yticks = [], yticklabels = [], yticklabels_fontsize = 12, box_colors = [],
            median_lw = 2.5, colors_dict = colors, savename = "", dpi = 300):

    ## Make figure
    plt.figure(figsize = figsize)
    ## Set figure properties for median, font, get rid of border, and add grid in the background
    medianprops = dict(linestyle='-.', linewidth= median_lw, color='k')
    plt.rcParams["font.family"] = "sans-serif"
    plt.box(False)
    plt.grid(True, alpha = 0.3)
    plt.rcParams['axes.axisbelow'] = True

    ## Create axis object
    ax = plt.gca()

    ## Make boxplot
    bplot = ax.boxplot(x = data, vert=False, notch = True, patch_artist = True, medianprops = medianprops)

    ## Set colors of the boxes in the plot
    for patch, color in zip(bplot["boxes"], [colors_dict[C] for C in box_colors]):
        patch.set_facecolor(color)
    
    ## Set xticks
    if xticks != []:
        ax.set_xticks(xticks)
    if xticklabels != []:
        ## In the event that we have input tick labels but no ticks set,
        ## matplotlib gets weird about it, so make sure something gets set
        ## May require additional user input
        if xticks == []:
            try:
                xticks = [float(x) for x in xticklabels]
            except:
                xticks = [i+1 for i in range(len(xticklabels))]
            ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, fontsize = xticklabels_fontsize)
    else:
        plt.xticks(fontsize = xticklabels_fontsize)
    
    ## Set yticks
    if yticks != []:
        ax.set_yticks(yticks)
    if yticklabels != []:
        ## In the event that we have input tick labels but no ticks set,
        ## matplotlib gets weird about it, so make sure something gets set
        ## May require additional user input
        if yticks == []:
            yticks = [i+1 for i in range(len(yticklabels))]
        ax.set_yticklabels(yticklabels, fontsize = yticklabels_fontsize)
    else:
        plt.yticks(fontsize = yticklabels_fontsize)

    ## Label axes
    ax.set_xlabel(xlabel, fontsize = axis_label_fontsize)
    ax.set_ylabel(ylabel, fontsize = axis_label_fontsize)

    ## Set title
    ax.set_title(title, fontsize = title_fontsize)

    ## Saving
    plt.tight_layout()
    if savename != "":
        plt.savefig(savename, dpi = dpi, bbox_inches = 'tight')
    else:
        plt.show()

def single_series_single_scatter_plot(xdata = [], ydata = [], comparison_line_coords = [[0,1],[0,1]],
                        show_comparison_line = False, figsize = (6,5), 
                        xlabel = "", ylabel = "", axis_label_fontsize = 14, title = "",
                        marker = "o",
                        title_fontsize = 16, xticks = [], xticklabels = [], xticklabels_fontsize = 12, 
                        yticks = [], yticklabels = [], yticklabels_fontsize = 12, color = "k", plot_alpha = 0.6,
                        colors_dict = colors, savename = "", dpi = 300):
    ## Make figure
    plt.figure(figsize = figsize)
    ## Set figure properties for font, get rid of border, and add grid in the background
    plt.rcParams["font.family"] = "sans-serif"
    plt.box(False)
    plt.grid(True, alpha = 0.3)
    plt.rcParams['axes.axisbelow'] = True

    ## Create axis object
    ax = plt.gca()

    ## Make scatter plot
    if show_comparison_line:
        ax.plot(comparison_line_coords[0], comparison_line_coords[1], c = "k", ls = "-", lw = 1)
    ax.scatter(xdata, ydata, alpha = plot_alpha, c = colors_dict[color], marker = marker)
    
    ## Set xticks
    if xticks != []:
        ax.set_xticks(xticks)
    if xticklabels != []:
        ## In the event that we have input tick labels but no ticks set,
        ## matplotlib gets weird about it, so make sure something gets set
        ## May require additional user input
        if xticks == []:
            try:
                xticks = [float(x) for x in xticklabels]
            except:
                xticks = [i+1 for i in range(len(xticklabels))]
            ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, fontsize = xticklabels_fontsize)
    else:
        plt.xticks(fontsize = xticklabels_fontsize)
    
    ## Set yticks
    if yticks != []:
        ax.set_yticks(yticks)
    if yticklabels != []:
        ## In the event that we have input tick labels but no ticks set,
        ## matplotlib gets weird about it, so make sure something gets set
        ## May require additional user input
        if yticks == []:
            try:
                yticks = [float(y) for y in yticklabels]
            except:
                yticks = [i+1 for i in range(len(yticklabels))]
            ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels, fontsize = yticklabels_fontsize)
    else:
        plt.yticks(fontsize = yticklabels_fontsize)

    ## Label axes
    ax.set_xlabel(xlabel, fontsize = axis_label_fontsize)
    ax.set_ylabel(ylabel, fontsize = axis_label_fontsize)

    ## Set title
    ax.set_title(title, fontsize = title_fontsize)

    ## Saving
    plt.tight_layout()
    if savename != "":
        plt.savefig(savename, dpi = dpi, bbox_inches = 'tight')
    else:
        plt.show()

def multiple_series_single_scatter_plot(xdata = [], ydata = [], comparison_line_coords = [[0,1],[0,1]],
                        show_comparison_line = False, figsize = (6,5), 
                        legend = False, legend_labels = [], legend_label_fontsize = 12,
                        xlabel = "", ylabel = "", axis_label_fontsize = 14, title = "",
                        markers = [],
                        title_fontsize = 16, xticks = [], xticklabels = [], xticklabels_fontsize = 12, 
                        yticks = [], yticklabels = [], yticklabels_fontsize = 12, colors = [], plot_alpha = 0.6,
                        colors_dict = colors, savename = "", dpi = 300):
    ## Make figure
    plt.figure(figsize = figsize)
    ## Set figure properties for font, get rid of border, and add grid in the background
    plt.rcParams["font.family"] = "sans-serif"
    plt.box(False)
    plt.grid(True, alpha = 0.3)
    plt.rcParams['axes.axisbelow'] = True

    ## Create axis object
    ax = plt.gca()

    ## Make scatter plot
    if show_comparison_line:
        ax.plot(comparison_line_coords[0], comparison_line_coords[1], c = "k", ls = "-",  lw = 1)
    ## Check to make sure we have enough labels and colors and markers
    if len(legend_labels) != len(xdata):
        legend_labels = [f"Series {i+1}" for i in range(len(xdata))]
    if len(colors) != len(xdata):
        colors = ["k" for i in range(len(xdata))]
    if len(markers) != len(xdata):
        markers = ["o" for i in range(len(xdata))]
    for x,y,label,color,marker in zip(xdata, ydata, legend_labels, colors, markers):
        ax.scatter(x, y, alpha = plot_alpha, c = colors_dict[color], label = label, marker = marker)
    
    ## Set xticks
    if xticks != []:
        ax.set_xticks(xticks)
    if xticklabels != []:
        ## In the event that we have input tick labels but no ticks set,
        ## matplotlib gets weird about it, so make sure something gets set
        ## May require additional user input
        if xticks == []:
            try:
                xticks = [float(x) for x in xticklabels]
            except:
                xticks = [i+1 for i in range(len(xticklabels))]
            ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, fontsize = xticklabels_fontsize)
    else:
        plt.xticks(fontsize = xticklabels_fontsize)
    
    ## Set yticks
    if yticks != []:
        ax.set_yticks(yticks)
    if yticklabels != []:
        ## In the event that we have input tick labels but no ticks set,
        ## matplotlib gets weird about it, so make sure something gets set
        ## May require additional user input
        if yticks == []:
            try:
                yticks = [float(y) for y in yticklabels]
            except:
                yticks = [i+1 for i in range(len(yticklabels))]
            ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels, fontsize = yticklabels_fontsize)
    else:
        plt.yticks(fontsize = yticklabels_fontsize)

    ## Label axes
    ax.set_xlabel(xlabel, fontsize = axis_label_fontsize)
    ax.set_ylabel(ylabel, fontsize = axis_label_fontsize)

    ## Set title
    ax.set_title(title, fontsize = title_fontsize)

    ## Saving
    plt.tight_layout()
    if legend:
        plt.legend(fontsize = legend_label_fontsize)
    if savename != "":
        plt.savefig(savename, dpi = dpi, bbox_inches = 'tight')
    else:
        plt.show()

def single_series_multiple_scatter_plot_single_row(xdata = [], ydata = [], comparison_line_coords = [[0,1],[0,1]],
                        show_comparison_line = False, figsize = (6,5), 
                        xlabel = "", ylabel = "", axis_label_fontsize = 14, titles = [],
                        markers = [],
                        title_fontsize = 16, xticks = [], xticklabels = [], xticklabels_fontsize = 12, 
                        yticks = [], yticklabels = [], yticklabels_fontsize = 12, colors = [], plot_alpha = 0.6,
                        colors_dict = colors, savename = "", dpi = 300):
    ## Make figure
    fig, axarr = plt.subplots(nrows = 1, ncols = len(xdata), figsize = figsize)
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams['axes.axisbelow'] = True
    
    if len(axarr) != len(ydata):
        raise ValueError("Number of y-axis series does not match number of x-axis series.")
    if len(titles) != len(axarr):
        titles = [f"Plot {i+1}" for i in range(len(axarr))]
    if len(markers) != len(axarr):
        markers = ["o" for i in range(len(axarr))]
    if len(colors) != len(axarr):
        colors = ["k" for i in range(len(axarr))]

    for ax, title, X, Y, C, M in zip(axarr, titles, xdata, ydata, colors, markers):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.grid(True, alpha = 0.3)
        ## Make scatter plot
        if show_comparison_line:
            ax.plot(comparison_line_coords[0], comparison_line_coords[1], c = "k", ls = "-",  lw = 1)
        ## Check to make sure we have enough labels and colors and markers
        ax.scatter(X, Y, alpha = plot_alpha, c = colors_dict[C], marker = M)
    
        ## Set xticks
        if xticks != []:
            ax.set_xticks(xticks)
        if xticklabels != []:
            ## In the event that we have input tick labels but no ticks set,
            ## matplotlib gets weird about it, so make sure something gets set
            ## May require additional user input
            if xticks == []:
                try:
                    xticks = [float(x) for x in xticklabels]
                except:
                    xticks = [i+1 for i in range(len(xticklabels))]
                ax.set_xticks(xticks)
            ax.set_xticklabels(xticklabels, fontsize = xticklabels_fontsize)
        else:
            plt.xticks(fontsize = xticklabels_fontsize)
        
        ## Set yticks
        if yticks != []:
            ax.set_yticks(yticks)
        if yticklabels != []:
            ## In the event that we have input tick labels but no ticks set,
            ## matplotlib gets weird about it, so make sure something gets set
            ## May require additional user input
            if yticks == []:
                try:
                    yticks = [float(y) for y in yticklabels]
                except:
                    yticks = [i+1 for i in range(len(yticklabels))]
                ax.set_yticks(yticks)
            ax.set_yticklabels(yticklabels, fontsize = yticklabels_fontsize)
        else:
            plt.yticks(fontsize = yticklabels_fontsize)

        ## Label axes
        ax.set_xlabel(xlabel, fontsize = axis_label_fontsize)
        ## Set title
        ax.set_title(title, fontsize = title_fontsize)

    axarr[0].set_ylabel(ylabel, fontsize = axis_label_fontsize)

    ## Saving
    plt.tight_layout()
    if savename != "":
        plt.savefig(savename, dpi = dpi, bbox_inches = 'tight')
    else:
        plt.show()

def multiple_horizontal_boxplot(data, figsize = (6,5), xlabel = "", ylabel = "", axis_label_fontsize = 14, titles = [],
            title_fontsize = 16, xticks = [], xticklabels = [], xticklabels_fontsize = 12, 
            yticks = [], yticklabels = [], yticklabels_fontsize = 12, box_colors = [],
            median_lw = 2.5, colors_dict = colors, savename = "", dpi = 300):

    ## Make figure
    fig, axarr = plt.subplots(nrows = 1, ncols = len(data), figsize = figsize, sharey=True)
    ## Set figure properties for median, font, get rid of border, and add grid in the background
    medianprops = dict(linestyle='-.', linewidth= median_lw, color='k')
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams['axes.axisbelow'] = True

    if len(titles) != len(axarr):
        titles = [f"Plot {i+1}" for i in range(len(axarr))]

    for ax, X, title in zip(axarr, data, titles):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.grid(True, alpha = 0.3)
        ## Make boxplot
        bplot = ax.boxplot(x = X, vert=False, notch = True, patch_artist = True, medianprops = medianprops)

        ## Set colors of the boxes in the plot
        for patch, color in zip(bplot["boxes"], [colors_dict[C] for C in box_colors]):
            patch.set_facecolor(color)
    
        ## Set xticks
        if xticks != []:
            ax.set_xticks(xticks)
        if xticklabels != []:
            ## In the event that we have input tick labels but no ticks set,
            ## matplotlib gets weird about it, so make sure something gets set
            ## May require additional user input
            if xticks == []:
                try:
                    xticks = [float(x) for x in xticklabels]
                except:
                    xticks = [i+1 for i in range(len(xticklabels))]
                ax.set_xticks(xticks)
            ax.set_xticklabels(xticklabels, fontsize = xticklabels_fontsize)
        else:
            plt.xticks(fontsize = xticklabels_fontsize)
        
        ## Set yticks
        if yticks != []:
            ax.set_yticks(yticks)
        if yticklabels != []:
            ## In the event that we have input tick labels but no ticks set,
            ## matplotlib gets weird about it, so make sure something gets set
            ## May require additional user input
            if yticks == []:
                yticks = [i+1 for i in range(len(yticklabels))]
            ax.set_yticklabels(yticklabels, fontsize = yticklabels_fontsize)
        else:
            plt.yticks(fontsize = yticklabels_fontsize)

        ## Label axes
        ax.set_xlabel(xlabel, fontsize = axis_label_fontsize)

        ## Set title
        ax.set_title(title, fontsize = title_fontsize)

    axarr[0].set_ylabel(ylabel, fontsize = axis_label_fontsize)

    ## Saving
    plt.tight_layout()
    if savename != "":
        plt.savefig(savename, dpi = dpi, bbox_inches = 'tight')
    else:
        plt.show()

def comparativeDistributionPlot(x_axis_data, y_axis_data, xlabel, ylabel, 
                                savename = "",
                                show_90_10 = False, 
                                show_min_max = False, 
                                show_histograms = True,
                                figsize = (10,10),
                                show_75_25_color = "ggplot blue",
                                show_90_10_color = "purple",
                                show_min_max_color = "k",
                                median_color = "scatter blue",
                                x_histogram_color = "darker blue",
                                y_histogram_color = "darker blue",
                                log = True,
                                yticklabels = [],
                                colors_dict = colors, markersize = 9, fontsize = 12):

    def createOverlappingBins(data, quantiles = np.arange(0,110,10)):
        indices = [(i, i+2) for i in range(len(quantiles)-2)]
        quantiles = np.percentile(data, quantiles)
        return [(quantiles[ind[0]], quantiles[ind[1]]) for ind in indices]
    
    bins = createOverlappingBins(x_axis_data)

    if type(x_axis_data) != type(np.array([0])):
        x_axis_data = np.array(x_axis_data)

    if type(y_axis_data) != type(np.array([0])):
        y_axis_data = np.array(y_axis_data)

    ## Mask out any entries containing NaNs
    nan_mask = (~np.isnan(x_axis_data)) & (~np.isnan(y_axis_data))
    x_axis_data = x_axis_data[nan_mask]
    y_axis_data = y_axis_data[nan_mask]

    minimums = []
    maximums = []
    percentile_10 = []
    percentile_25 = []
    percentile_75 = []
    percentile_90 = []
    medians = []
    xticks = []

    for b in bins:
        mask = (x_axis_data >= b[0]) & (x_axis_data <= b[1])
        x_masked = x_axis_data[mask]
        y_masked = y_axis_data[mask]

        tick = round(np.nanmedian(x_masked), 1)
        if abs(tick) == 0.0:
            tick = 0.0
        xticks.append(tick)
        
        minimums.append(y_masked.min())
        maximums.append(y_masked.max())
        medians.append(np.median(y_masked))

        for p, l in zip([10,25,75,90], [percentile_10, percentile_25,percentile_75,percentile_90]):
            l.append(np.percentile(y_masked, p))
        
    ##Create figure
    fig = plt.figure(figsize = figsize)
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams['axes.axisbelow'] = True

    ##Allocate a 4x4 grid for figures
    gs = GridSpec(4,4)

    ##Define subplots on GridSpec object
    if show_histograms:
        ax_joint = fig.add_subplot(gs[0:3,0:3])
        ax_marg_x = fig.add_subplot(gs[3,0:3])
        ax_marg_y = fig.add_subplot(gs[0:3,3])

        for ax in [ax_joint, ax_marg_x, ax_marg_y]:
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.grid(True, alpha = 0.3)

    else:
        ax_joint = plt.gca()
        ax_joint.spines["top"].set_visible(False)
        ax_joint.spines["right"].set_visible(False)
        ax_joint.spines["bottom"].set_visible(False)
        ax_joint.spines["left"].set_visible(False)
        ax_joint.grid(True, alpha = 0.3)

    x = list(range(len(xticks)))

    ##First plot filled regions between min/max, 10th/90th percentile, and 
    ##25th/75th percentile regions
    if show_min_max:
        ax_joint.fill_between(x, y1 = minimums, y2 = maximums, color = "k", alpha = 0.05)
    if show_90_10:
        ax_joint.fill_between(x, y1 = percentile_10, y2 = percentile_90, color = "k", alpha = 0.05)
    ax_joint.fill_between(x, y1 = percentile_25, y2 = percentile_75, color = "k", alpha = 0.05)


    ##Plot lines corresponding to mean, min, 10th%, 25th%, 75th%, 90th%, and max
    ##against mean value of interval of column_to_bin
    ax_joint.plot(x, medians, "o-", color = colors_dict[median_color], label = "Median", markersize = markersize)

    ax_joint.set_xticks(x)
    ax_joint.set_xticklabels(xticks, fontsize = fontsize)
    if yticklabels != []:
        try:
            yticks = [float(yy) for yy in yticklabels]
        except:
            yticks = [i for i in range(len(yticklabels))]
        ax_joint.set_yticks(yticks)
        ax_joint.set_yticklabels(yticklabels, fontsize = fontsize)
    else:
        yticks = np.linspace(min(medians), max(medians), num = 6)
        print(yticks)
        yticks = np.append(yticks, np.array([2*yticks[-1] - yticks[-2]]), axis = 0)
        print(yticks)
        yticklabels = [str(round(yy, 1)) for yy in yticks]
        ax_joint.set_yticks(yticks)
        ax_joint.set_yticklabels(yticklabels, fontsize = fontsize)
    
    
    ax_joint.plot(x, percentile_25, "v--", label = "25th Percentile", color = colors_dict[show_75_25_color], markersize = markersize)
    ax_joint.plot(x, percentile_75, "^--", label = "75th Percentile", color = colors_dict[show_75_25_color], markersize = markersize)

    if show_90_10:
        ax_joint.plot(x, percentile_10, "X--", label = "10th Percentile", color = colors_dict[show_90_10_color], markersize = markersize)
        ax_joint.plot(x, percentile_90, "P--", label = "90th Percentile", color = colors_dict[show_90_10_color], markersize = markersize)

    if show_min_max:
        ax_joint.plot(x, minimums, "<--", color = colors_dict[show_min_max_color], label = "Minimum")
        ax_joint.plot(x, maximums, ">--", color = colors_dict[show_min_max_color], label = "Maximum")
    ax_joint.legend(fontsize = fontsize)

    ##Create a histogram of all similarity scores between model comparisons
    ##for both metrics. Histogram on right hand side is the histogram of values from 
    ##column_to_distribute. Histogram at the top is the histogram of values from
    ##column_to_bin
    if show_histograms:
        ax_marg_x.hist(x_axis_data, log = log, color = colors_dict[x_histogram_color], bins = len(bins), edgecolor = "k")
        ax_marg_y.hist(y_axis_data, log = log, color = colors_dict[y_histogram_color], orientation="horizontal", bins = len(bins), edgecolor = "k")

        ##Ensure axes ranges match from scatter plot to 
        ##histograms
        # plt.setp(ax_marg_x.get_xticklabels(), visible=False)
        plt.setp(ax_marg_y.get_yticklabels(), visible=False)

        ax_marg_y.set_xlabel('Count', fontsize = fontsize+2)
        ax_marg_x.set_ylabel('Count', fontsize = fontsize+2)

    ##Label axes in plot
    ax_joint.set_xlabel(xlabel, fontsize = fontsize+4)
    ax_joint.set_ylabel(ylabel, fontsize = fontsize+4)

    ##Save figure
    plt.tight_layout()
    if savename:
        plt.savefig(savename, dpi = 400, bbox_inches = 'tight')
        plt.close(fig)
    else:
        plt.show()