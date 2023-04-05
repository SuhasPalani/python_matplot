import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import csv
plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row=next(csv_reader)
    print(row['LanguagesWorkedWith'].split(';'))

# plt.xticks(ticks=x_indexes,labels=ages_x)

# plt.title("Median Salary (USD) by Age")
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")

# plt.tight_layout()
# plt.savefig('Fig5.png')
# plt.show()
