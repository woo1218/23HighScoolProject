import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data.csv', encoding='cp949')
kor = df[df['팀'] == '대한민국']
print(kor)