import pandas as pd
import matplotlib.pyplot as plt

def dictionary_builder(df):
    title_to_salary = {}
    for ix in range(len(df.iloc[:, 1].values)):
        title = df.iloc[ix, 1]
        salary = 8
        if title in title_to_salary.keys():
            title_to_salary[title].append(df.iloc[ix, 7])
        else:
            title_to_salary[title] = [df.iloc[ix,7]]
    return title_to_salary

def title_to_median_pay(title, pay_dict):
    salaries = sorted(pay_dict[title])
    return salaries[int(len(salaries)/2)]

def bucket_plot(pay_list, chart_title):
    full_salaries = remove_lows(pay_list)
    max_pay = max(full_salaries)
    c = {}
    for salary in full_salaries:
        bucket = 5000*int(salary/5000)
        if bucket in c.keys():
            c[bucket] += 1
        else:
            c[bucket] = 1
    x=[]
    y=[]
    for key in c.keys():
        x.append(key)
        y.append(c[key])
    plt.bar(x,y, width = 4000)
    plt.title(chart_title)
    plt.show()

def remove_lows(pay_list):
    sorted_list = sorted(pay_list)
    for ix in range(len(sorted_list)):
        if sorted_list[ix] > 10000:
            if ix > 0:
                del sorted_list[:(ix-1)]
            return sorted_list

df = pd.read_csv('/Users/Joe/Desktop/python/Self_study_datasci/california-state-university-2014.csv')
title_to_pay = dictionary_builder(df)

common_positions = []
for key in title_to_pay.keys():
    if len(title_to_pay[key]) > 300:
        common_positions.append(key)

for title in common_positions:
	bucket_plot(title_to_pay[title], title)








