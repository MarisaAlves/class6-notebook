import os
import matplotlib.pyplot as plt
import pandas as pd

diabetes = pd.read_csv(filepath_or_buffer='diabetes.data', sep ='\t', header=0)


plt.style.use("ggplot")

for col1_idx, column1 in enumerate(diabetes.columns):
    for col2_idx, column2 in enumerate(diabetes.columns):
        if col1_idx < col2_idx:
            for col3_idx, column3 in enumerate(diabetes.columns):
                if col2_idx <col3_idx :
                    for col4_idx, column4 in enumerate(diabetes.columns):
                        if col3_idx < col4_idx:
                            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
                            axes.grid(axis='y', alpha=0.5)
                            axes.scatter(diabetes[column1], diabetes[column2], s=diabetes['BP']* 0.3, color='green', marker="8")
                            axes.scatter(diabetes[column1], diabetes[column3], s=diabetes['BP'] * 0.3, color='red', marker="d")
                            axes.scatter(diabetes[column1], diabetes[column4], s=diabetes['BP'] * 0.3, color='orange', marker="+")
                            axes.set_title(f'Diabetes predictor correlations')
                            axes.set_xlabel('Feature Levels')
                            axes.set_ylabel('Diabetes Progression')
                            axes.legend()
                            plt.savefig(f'plots/diabetes_correlated_to_S1S2S3.png', dpi=300)

                            axes.legend()
                            plt.savefig(f'plots/diabetes_{column1}_{column2}_scatter.png', dpi=300)
                            plt.close(fig)

fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.grid(axis='y', alpha=0.5)
axes.scatter(diabetes['Y'], diabetes['S1'], s = diabetes['BP']*0.3, color='green', marker="8")
axes.scatter(diabetes['Y'], diabetes['S2'], s =diabetes['BP']*0.3, color='red', marker="d")
axes.scatter(diabetes['Y'], diabetes['S3'], s=diabetes['BP']*0.3, color='orange', marker="+")
axes.set_title(f'Diabetes predictor correlations')
axes.set_xlabel('Serum levels')
axes.set_ylabel('Diabetes Progression')
axes.legend()
plt.savefig(f'plots/diabetes_correlated_to_S1S2S3.png', dpi=300)


plt.show()
plt.close()


#Standardize dataset so all the values are between 0 and 1
