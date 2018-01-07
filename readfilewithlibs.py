#!/usr/bin/python
print("Start program");

import pandas as pd
import os

filename = 'campaigns.txt'

moviespath = os.path.expanduser(filename)
movies = pd.read_csv(moviespath, delimiter="\t")
print(movies)

print("End program");
