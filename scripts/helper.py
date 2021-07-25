import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

GRAY4 = '#646369'
GRAY5 = '#76787B'

def to_color(ax, fontsize: int, color: str, grid: bool):
    plt.sca(ax)
    if grid:
        plt.grid(color = 'lightgrey', linewidth = 0.5)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.tick_params(color = color, bottom = 'off')
    for i in ax.get_yticklabels() + ax.get_xticklabels():
        i.set_fontsize(12)
        i.set_color(color)

def suptitle_formatter(suptitle: str, subtitle: str = None):
    suptitle_formated = "$\\bf{" + '\ '.join(suptitle.split()) + '}$'
    if subtitle is not None:
        suptitle_formated += '\n' + subtitle
    return suptitle_formated
        
def axis_presentation(ax, axis_fontsize: int = 10, grid: bool = True, ylabel: str = None, xlabel: str = None,
                      legend: bool = False, **kwargs):
    to_color(ax, axis_fontsize, GRAY5, grid)
    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize = 14, color = GRAY5)
    else:
        ax.set_ylabel('', fontsize = 14, color = GRAY5)
    if ylabel is not None:
        ax.set_xlabel(xlabel, fontsize = 14, color = GRAY5)
    if not legend:
        leg = ax.get_legend()
        if leg is not None:
            leg.remove()

def presentation(fig, ax, y_label, title: str, subtitle: str = None, title_fontsize: int = 22, title_color: str = GRAY4, title_position: float = 0.135,
                 **kwargs):  
    if type(ax) is list:
        length_axis = len(ax)
        for idx in range(length_axis):
            axis_presentation(ax[idx], ylabel=y_label[idx], **kwargs)
    plt.suptitle(suptitle_formatter(title, subtitle), fontsize = title_fontsize, color = title_color, y=fig.subplotpars.top+title_position, x=fig.subplotpars.left, ha='left')
    
def legend_formatter(ax, color: list, label: list, bbox: set, title: str, frame: bool = False, loc: str = 'upper right'):
    patches = [mpatches.Patch(facecolor=c, edgecolor=GRAY5, label=l) for c, l in zip(color, label)]
    plt.sca(ax)
    leg = plt.legend(handles=patches, loc=loc, bbox_to_anchor=bbox,
               frameon=frame, labelcolor=GRAY5, title=suptitle_formatter(title))
    plt.setp(leg.get_title(), color=GRAY4)

def list_high_correlate_columns(df, threashold = 0.9):
    cor_matrix = df.corr().abs()
    cor_list = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool)).stack().reset_index()
    cor_list.columns = ['level_0', 'level_1', 'correlation']
    return cor_list.loc[cor_list['correlation'] > threashold].reset_index(drop=True)