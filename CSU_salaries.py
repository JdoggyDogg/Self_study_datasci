import pandas as pd
import matplotlib.pyplot as plt

def dictionary_builder(df):
    title_to_salary = {}
    total_pay_index = 7
    for ix in range(len(df.iloc[:, 1].values)):
        title = df.iloc[ix, 1]
        if title in title_to_salary.keys():
            title_to_salary[title].append(df.iloc[ix, total_pay_index])
        else:
            title_to_salary[title] = [df.iloc[ix, total_pay_index]]
    return title_to_salary

def title_to_median_pay(title, pay_dict):
    salaries = sorted(pay_dict[title])
    return salaries[int(len(salaries)/2)]

def bucket_plot(pay_list, chart_title):
    full_salaries = remove_lows(pay_list)
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
    # remove salaries lower than 10,000 dollars; these workers weren't working full time for the full year
    sorted_list = sorted(pay_list)
    for ix in range(len(sorted_list)):
        if sorted_list[ix] > 10000:
            if ix > 0:
                del sorted_list[:(ix-1)]
            return sorted_list








df = pd.read_csv('/Users/Joe/Desktop/python/Self_study_datasci/california-state-university-2014.csv')
title_to_pay = dictionary_builder(df)

# make a list of the positions that employed 300 or more people
common_positions = [key for key in title_to_pay.keys() if len(title_to_pay[key]) > 300]

for title in common_positions:
	bucket_plot(title_to_pay[title], title)








