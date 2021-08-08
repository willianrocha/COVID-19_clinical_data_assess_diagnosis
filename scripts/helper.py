import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np

GRAY4 = '#646369'
GRAY5 = '#76787B'
GENDER_0 = '#59AB61'
GENDER_1 = '#3791AB'
ABOVE65_0 = '#74F782'
ABOVE65_1 = '#5CD5F7'
ICU_0 = '#ADA476'
ICU_1 = '#FF4336'

ICU_0_LABEL = 'Não Admitido na UTI'
ICU_1_LABEL = 'Admitido na UTI'

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

def demographic_distribution_plot(demographic_data):
    fig = plt.figure(figsize=(10,7))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 1, 2)
    axis = [ax1, ax2, ax3]
    g = sns.countplot(data=demographic_data, ax=ax1, x="GENDER", hue='ICU', palette=[GENDER_0, GENDER_1], edgecolor=GRAY5);
    g = sns.countplot(data=demographic_data, ax=ax2, x="AGE_ABOVE65", hue='ICU', palette=[ABOVE65_0, ABOVE65_1], edgecolor=GRAY5);
    g = sns.countplot(data=demographic_data, ax=ax3, x="AGE_PERCENTIL", hue='ICU', palette=[ICU_0, ICU_1], edgecolor=GRAY5);
    xticks_g = [ICU_0_LABEL, ICU_1_LABEL]
    ax1.set_xticklabels(xticks_g, fontsize=12)
    ax2.set_xticklabels(xticks_g, fontsize=12)

    suptitle = 'Dados de internação do hospital Sírio-Linabês'
    subtitle = 'Distribuição Demográfica'
    y_label = ['Gênero', 'Acima de 65 anos', 'Distribuição de Idade']
    presentation(fig=fig, ax=axis, y_label=y_label, title=suptitle, subtitle=subtitle, grid=False)
    sns.despine()

    gen_0 = mpatches.Patch(facecolor=GENDER_0, edgecolor=GRAY5, label="Gênero 0")
    gen_1 = mpatches.Patch(facecolor=GENDER_1, edgecolor=GRAY5, label="Gênero 1")
    abv65_0 = mpatches.Patch(facecolor=ABOVE65_0, edgecolor=GRAY5, label="Abaixo de 65")
    abv65_1 = mpatches.Patch(facecolor=ABOVE65_1, edgecolor=GRAY5, label="Acima de 65")
    icu_0 = mpatches.Patch(facecolor=ICU_0, edgecolor=GRAY5, label=ICU_0_LABEL)
    icu_1 = mpatches.Patch(facecolor=ICU_1, edgecolor=GRAY5, label=ICU_1_LABEL)
    plt.sca(ax2)
    plt.legend(handles=[gen_0, gen_1, abv65_0, abv65_1, icu_0, icu_1], loc='upper right', bbox_to_anchor=(1.63, 1.0), frameon=False, labelcolor=GRAY5)
    plt.show()

def prexisting_disease_plot(preexisting_disease_data):
    xticks_g = [ICU_0_LABEL, ICU_1_LABEL]
    preexisting_disease_columns = ['DISEASE GROUPING 1', 'DISEASE GROUPING 2', 'DISEASE GROUPING 3', 'DISEASE GROUPING 4', 'DISEASE GROUPING 5', 'DISEASE GROUPING 6', 'HTN', 'IMMUNOCOMPROMISED', 'OTHER']
    preexisting_disease_labels = ['Doença do Grupo 1', 'Doença do Grupo 2', 'Doença do Grupo 3', 'Doença do Grupo 4', 'Doença do Grupo 5', 'Doença do Grupo 6', 'Hipertensão', 'Imunocomprometido', 'Outros']
    suptitle = 'Dados de internação do hospital Sírio-Linabês'
    subtitle = 'Doenças Pré-Existentes'
    DISEASE_0 = '#5CFF82'
    DISEASE_1 = '#FA4151'

    fig, ((ax11, ax12, ax13),(ax21,ax22,ax23),(ax31,ax32,ax33)) = plt.subplots(nrows=3, ncols=3, figsize=(16, 10)) #(10, 6)
    axes = [ax11, ax12, ax13,ax21,ax22,ax23,ax31,ax32,ax33]
    for i, ax in enumerate(axes):
        sns.countplot(data=preexisting_disease_data, x=preexisting_disease_columns[i], hue='ICU',ax=ax, palette=[DISEASE_0, DISEASE_1], edgecolor=GRAY5)
        ax.set_xticklabels(xticks_g, fontsize=12)
    presentation(fig=fig, ax=axes, y_label=preexisting_disease_labels, title=suptitle, subtitle=subtitle,
                 title_position = 0.085, grid=False, legend=False)

    disease_0 = mpatches.Patch(facecolor=DISEASE_0, edgecolor=GRAY5, label="Não tem")
    disease_1 = mpatches.Patch(facecolor=DISEASE_1, edgecolor=GRAY5, label="Tem")
    plt.sca(ax13)
    plt.legend(handles=[disease_0, disease_1], loc='upper right', bbox_to_anchor=(1.3, 1.0), frameon=False, labelcolor=GRAY5)

    sns.despine()

def vital_signs_plot(dados, suptitle, subtitle):
    attributes_suffix = ['DIFF', 'DIFF_REL', 'MAX', 'MEAN', 'MEDIAN', 'MIN']
    vital_signs = ['BLOODPRESSURE_DIASTOLIC', 'BLOODPRESSURE_SISTOLIC', 'HEART_RATE', 'OXYGEN_SATURATION', 'RESPIRATORY_RATE', 'TEMPERATURE']

    attributes_label = ['Diff', 'Diff Relativa', 'Máximo', 'Média', 'Mediana', 'Mínimo']
    vital_signs_label = ['PAD', 'PAS', 'Freq. Cardíaca', 'Sat. do Oxigênio', 'Freq. Respiratória', 'Temperatura']

    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows=6, ncols=1, figsize=(12, 14), sharex=True) #(10, 6)
    axes = [ax1, ax2, ax3, ax4, ax5, ax6]
    for i, vital in enumerate(vital_signs):
        vs_columns = [f'{vital}_{attr}' for attr in attributes_suffix]
        vs_melt = dados.melt(id_vars=['ICU'], value_vars=vs_columns, var_name='col', value_name='value').reset_index(drop=True)
#         vs_melt['value'] = vs_melt['value'].replace(-1, np.nan)
#         vs_melt['value'] = vs_melt['value'].replace(1, np.nan)
        sns.boxplot(x="col", y="value", hue='ICU', data=vs_melt, ax=axes[i], palette=[ICU_0, ICU_1])
    ax6.set_xticklabels(attributes_label, fontsize=12)
    presentation(fig=fig, ax=axes, y_label=vital_signs_label, title=suptitle, subtitle=subtitle,
                 title_position = 0.055, grid=False, legend=False)

    disease_0 = mpatches.Patch(facecolor=ICU_0, edgecolor=GRAY5, label=ICU_0_LABEL)
    disease_1 = mpatches.Patch(facecolor=ICU_1, edgecolor=GRAY5, label=ICU_1_LABEL)
    plt.sca(ax1)
    leg = plt.legend(handles=[disease_0, disease_1], loc='upper right', bbox_to_anchor=(1.225, 1.0),
               frameon=False, labelcolor=GRAY5, title=suptitle_formatter('Status da UTI'))
    plt.setp(leg.get_title(), color=GRAY4)

    sns.despine()

def blood_results_plot(dados, suptitle, subtitle):
    attributes_suffix = ['DIFF', 'MAX', 'MEAN', 'MEDIAN', 'MIN']
    blood_results = ['ALBUMIN', 'BE_ARTERIAL', 'BE_VENOUS', 'BIC_ARTERIAL', 'BIC_VENOUS', 'BILLIRUBIN', 'BLAST', 'CALCIUM', 'CREATININ', 'FFA', 'GGT', 'GLUCOSE', 'HEMATOCRITE', 'HEMOGLOBIN', 'INR', 'LACTATE', 'LEUKOCYTES', 'LINFOCITOS', 'NEUTROPHILES', 'P02_ARTERIAL', 'P02_VENOUS', 'PC02_ARTERIAL', 'PC02_VENOUS', 'PCR', 'PH_ARTERIAL', 'PH_VENOUS', 'PLATELETS', 'POTASSIUM', 'SAT02_ARTERIAL', 'SAT02_VENOUS', 'SODIUM', 'TGO', 'TGP', 'TTPA', 'UREA', 'DIMER']
    blood_results_columns = [f'{blood}_MEAN' for blood in blood_results]
    fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(12, 14))
    blood_results_lines = np.array_split(blood_results_columns, 6)
    blood_results_labels = np.array_split(blood_results, 6)
    y_label = [None]*6

    for i, blood in enumerate(blood_results_lines):
        br_melt = dados.melt(id_vars=['ICU'], value_vars=blood, var_name='col', value_name='value').reset_index(drop=True)
#         br_melt['value'] = br_melt['value'].replace(-1, np.nan)
#         br_melt['value'] = br_melt['value'].replace(1, np.nan)
        sns.boxplot(x="col", y="value", hue='ICU', data=br_melt, ax=axes[i], palette=[ICU_0, ICU_1])
        axes[i].set_xticklabels(blood_results_labels[i], fontsize=12)
    presentation(fig=fig, ax=axes.tolist(), y_label=y_label, title=suptitle, subtitle=subtitle,
                 title_position = 0.055, grid=False, legend=False)
    sns.despine()

    icu_color = [ICU_0, ICU_1]
    icu_label = [ICU_0_LABEL, ICU_1_LABEL]
    legend_formatter(axes[0], icu_color, icu_label, bbox=(1.205, 1.0), title='Status da UTI')
    axes[-1].set_xlabel('')
    plt.show()