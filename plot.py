import matplotlib.pyplot as plt
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