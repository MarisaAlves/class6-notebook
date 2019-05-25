import os
import matplotlib.pyplot as plt
import pandas as pd

diabetes = pd.read_csv(filepath_or_buffer='diabetes.data', sep ='\t', header=0)

os.makedirs('plots', exist_ok=True)

fig, axes = plt.subplots(2, 1, figsize=(5,5))

axes[0].plot(diabetes['BP'])
axes[1].plot(diabetes['BP'], diabetes['AGE'])

axes[0].set_xlabel('Index')
axes[0].set_ylabel('BP')
axes[0].set_title('Blood Pressure')

axes[1].set_xlabel('BP')
axes[1].set_ylabel('Age')
axes[1].set_title('BP to Age')


plt.tight_layout()

plt.savefig(f'plots/figures.png', format='png', dpi=300)
plt.clf()


plt.scatter(diabetes['BP'], diabetes['AGE'], color='b', marker="p", alpha=0.3)
plt.title('BP to Age')
plt.xlabel('BP')
plt.ylabel('Age')
plt.savefig(f'plots/bp_to_age.png', format='png')
plt.show()
plt.clf()

plt.close()

