import numpy as np
import pandas as pd
from collections import Counter

from matplotlib import pyplot as plt
import csv
plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
        
print(language_counter)