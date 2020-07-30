import matplotlib.pyplot as plt
from colr import color

colors = {"orange":"#FF9736", 
          "violet":"#ECE7F2",
          "light blue":"#A1BFDA",
          "darker blue":"#008EBD",
          "purple":"#8859A6",
          "red":"#C73C41",
          "scatter green":"#009D78",
          "scatter orange":"#E77B42",
          "scatter blue":"#7877B5",
          "scatter pink":"#F1348F"}

def print_available_colors(colors = colors):
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