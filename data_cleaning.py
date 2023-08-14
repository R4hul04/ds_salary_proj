import pandas as pd
import re

df = pd.read_csv('glassdoor_jobs.csv')

'''
Salary parsing
'''

#Salary Parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'Per Hour' in x.lower() else 0)
df['employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'Per Hour' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0])
minus_kd = salary.apply(lambda x:x.replace('K', '').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(float(x.split('-')[0])))
df['max_salary'] = min_hr.apply(lambda x: int(float(x.split('-')[1])) if len(x.split('-')) > 1 else int(float(x.split('-')[0])))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

#Company Name and Rating
df['company_txt'] = df['Company Name'].apply(lambda x: re.sub(r'\s*\d+\.\d+', '', x))
df['Rating'] = df['Company Name'].apply(lambda x : float(re.search(r'\d+\.\d+', x).group()) if re.search(r'\d+\.\d+', x) else -1)

#State Field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if len(x.split(',')) > 1 else -1)
df.job_state.value_counts()

#df['same_state'] = df.apply(lambda x: x.Location == x.Headquaters else 0, axis = 1)

#age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2023 - x)

#parsing the job description
df['Job Description'][1]

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()
#r studio
df['r_studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.r_studio.value_counts()
#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()
#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df.to_csv('salary_data_cleaned.csv', index = False)

#duplicate_mask = df.duplicated()
# Show the duplicate rows
#duplicate_rows = df[duplicate_mask]
#print(duplicate_rows)