import json
import pandas as pd
import csv
from random import randint, random

#файл с отдельными OID-ами, которые встречаются в трапах
devinitions_csv = "G:\\tmp\\trap_definition.csv"

#файл с сообщениями о трапах
traps_csv = "G:\\tmp\\sova_trap_1.csv"

df = pd.read_csv(devinitions_csv)

print(df)



