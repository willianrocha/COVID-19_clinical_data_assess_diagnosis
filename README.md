[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/willianvrocha/)
# COVID-19 - Análise de dados clínicos para diagnóstico da necessidade de UTI

1. [Resumo](#summary)
2. [Notebooks](#notebook)
3. [Conclusão](#conclusion)

<a name="summary"></a>
# Resumo
Como a COVID-19 é uma doença que tem alta taxa de hospitalização. Os recursos precisam ser previstos e alocados com o máximo de antecedência possível para maximizar a recuperação dos pacientes. O Hospital Sírio-Libanês e sua equipe de data science publicou na plataforma do [kaggle](https://www.kaggle.com/S%C3%ADrio-Libanes/covid19) um desafio de predição se o paciente precisará ou não de UTI.

Desta forma, este projeto tem como objtivo criar um modelo robusto de machine learning para prever quais pacientes precisarão ser adimitidos na UTI.

<a name="notebook"></a>
# Notebooks

## [EDA](https://github.com/willianrocha/COVID-19_clinical_data_assess_diagnosis/blob/main/notebooks/EDA.ipynb)
Este notebook foi dedicado ao entendimento dos dados apresentados, levantamento de hipóteses de quais dados teriam maior impacto na preedição do modelo e eliminação de colunas que agregam pouca informação. O resultado desde notebook pode ser conferido no arquivo [Kaggle_Sirio_Libanes_ICU_Prediction_reduced.csv](https://github.com/willianrocha/COVID-19_clinical_data_assess_diagnosis/raw/main/data/Kaggle_Sirio_Libanes_ICU_Prediction_reduced.csv)

## [ML](https://github.com/willianrocha/COVID-19_clinical_data_assess_diagnosis/blob/main/notebooks/ML.ipynb)
Neste notebook, realizamos o procedimento de preenchimento de dados faltantes, exploração de modelos, eliminação de colunas correlacionadas e comparação entre modelos. Dadas as instruções dos dados iniciais, foi utilizada apenas a janela de tempo de 0-2 no modelo de machine learning.

## [Pipeline](https://github.com/willianrocha/COVID-19_clinical_data_assess_diagnosis/blob/main/notebooks/Pipeline.ipynb)
Aqui, consolidademos todo o trabalho feito de modo que podemos utilizar a mesma estrutura de dados disponibilizados pelo Sírio-Libanês para realizar o treinamento, predição e deploy.

<a name="conclusion"></a>
# Conclusão
Como conclusão temos um modelo com F1-Score de 0.7 e a seguinte matrix de confusão.
<p align="center">
  <img src="https://github.com/willianrocha/COVID-19_clinical_data_assess_diagnosis/raw/main/img/confusion_matrix.png">
</p>

