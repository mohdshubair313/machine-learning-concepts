import pandas as pd
import numpy as np

# =====================================================================
# 🐼 PANDAS MASTER CHEATSHEET & IMPORTANT FUNCTIONS
# =====================================================================
# Pandas = "Panel Data" -> Python ki sabse powerful library jo tabular 
# (rows x columns) data ko handle karti hai. Jaise Excel spreadsheet 
# hoti hai, waise hi Pandas mein DataFrame hota hai.
#
# Pandas vs Numpy ka fark (Quick Recap):
# - Numpy = Numbers ke saath maths karna (Engine)
# - Pandas = Real-world data (CSV, Excel, SQL) ko padhna, saaf karna, 
#            analyze karna (Dashboard + Steering Wheel)
# =====================================================================


# =====================================================================
# 1. DATA STRUCTURES (Pandas ke 2 Main Dabba)
# =====================================================================

# ---- 1a. SERIES (1D - Ek Column) ----
# Kya hai: Ek single column of data with index (label). 
# Kab use hota hai: Jab aapko sirf ek column ka data chahiye.
# Example:
marks = pd.Series([85, 90, 78, 92], index=['Math', 'Science', 'English', 'Hindi'])
# Output:
# Math       85
# Science    90
# English    78
# Hindi      92


# ---- 1b. DATAFRAME (2D - Poori Table / Spreadsheet) ----
# Kya hai: Rows aur Columns wali ek poori table. Har column ek Series hai.
# Kab use hota hai: Jab CSV, Excel ya database se data read karna ho.
# Example (Dictionary se DataFrame banana):
student_data = {
    'Name':   ['Shubair', 'Alice', 'Bob'],
    'Age':    [25, 22, 28],
    'Marks':  [92, 88, 75]
}
df = pd.DataFrame(student_data)
# Output:
#      Name  Age  Marks
# 0  Shubair   25     92
# 1    Alice   22     88
# 2      Bob   28     75


# =====================================================================
# 2. DATA READING & WRITING (File se Data Laana / Bhejna)
# =====================================================================

# ---- pd.read_csv('file.csv') ----
# Kya karta hai: CSV file ko padhkar DataFrame mein load karta hai.
# Kab use hota hai: Jab bhi koi dataset CSV format mein ho (90% time yahi hota hai).
# Kaise use karein:
# df = pd.read_csv('data.csv')
# df = pd.read_csv('data.csv', encoding='utf-8')   # Agar Hindi/special characters hain
# df = pd.read_csv('data.csv', sep=';')             # Agar separator comma nahi semicolon hai

# ---- pd.read_excel('file.xlsx') ----
# Kya karta hai: Excel file padhta hai.
# Kab use hota hai: Office/corporate data mein bahut common.
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# ---- pd.read_json('file.json') ----
# Kya karta hai: JSON file (APIs se aata hai) ko DataFrame mein convert karta hai.
# df = pd.read_json('data.json')

# ---- pd.read_sql(query, connection) ----
# Kya karta hai: Database se direct SQL query karke data laata hai.
# Kab use hota hai: Production/backend mein jab database se data nikalna ho.
# df = pd.read_sql("SELECT * FROM users", db_connection)

# ---- df.to_csv('output.csv') ----
# Kya karta hai: DataFrame ko wapas CSV file mein save karta hai.
# df.to_csv('output.csv', index=False)  # index=False taaki extra index column na aaye

# ---- df.to_excel('output.xlsx') ----
# df.to_excel('output.xlsx', index=False)


# =====================================================================
# 3. DATA EXPLORATION (Data ko Pehli Baar Dekhna / Samajhna)
# =====================================================================
# Jab bhi naya data mile, pehle usse "explore" karo — ye sabse important step hai!

# ---- df.head(n) ----
# Kya karta hai: Pehli n rows dikhata hai (default 5).
# Kab use hota hai: Naya data load karne ke TURANT baad — dekhne ke liye ki data kaisa dikhta hai.
# df.head()     # Pehli 5 rows
# df.head(10)   # Pehli 10 rows

# ---- df.tail(n) ----
# Kya karta hai: Aakhiri n rows dikhata hai.
# Kab use hota hai: Data ke end mein kya hai ye check karna.
# df.tail()     # Aakhiri 5 rows

# ---- df.shape ----
# Kya karta hai: (Rows, Columns) ki count deta hai.
# Kab use hota hai: Kitna bada dataset hai ye jaanne ke liye. Ye function nahi hai, property hai!
# df.shape      # (1000, 15) matlab 1000 rows aur 15 columns

# ---- df.info() ----
# Kya karta hai: Har column ka naam, data type, kitne non-null values hain — sab batata hai.
# Kab use hota hai: Missing data hai ya nahi, aur data types sahi hain ya nahi ye check karne ke liye.
# df.info()

# ---- df.describe() ----
# Kya karta hai: Sirf number wale columns ka statistical summary deta hai (mean, std, min, max, etc.)
# Kab use hota hai: Quick overview chahiye data ke distribution ka.
# df.describe()

# ---- df.dtypes ----
# Kya karta hai: Har column ka data type batata hai (int64, float64, object, etc.)
# df.dtypes

# ---- df.columns ----
# Kya karta hai: Sabhi column names ki list deta hai.
# df.columns

# ---- df.index ----
# Kya karta hai: Index (row labels) dikhata hai.
# df.index

# ---- df.nunique() ----
# Kya karta hai: Har column mein kitni unique values hain ye batata hai.
# Kab use hota hai: Categorical columns identify karne ke liye.
# df.nunique()

# ---- df.value_counts() ----
# Kya karta hai: Kisi column mein kaunsi value kitni baar aayi hai ye count karta hai.
# Kab use hota hai: Category data (jaise Gender, City) ka distribution dekhne ke liye.
# df['City'].value_counts()


# =====================================================================
# 4. DATA SELECTION & INDEXING (Data Nikalna)
# =====================================================================

# ---- Column Select karna ----
# Ek column:
# df['Name']                # Series return karta hai
# df.Name                   # Ye bhi same hai (par column name mein space ho toh kaam nahi karega)

# Multiple columns:
# df[['Name', 'Age']]       # Double brackets [[]] se multiple columns milte hain

# ---- Row Select karna ----

# df.loc[row_label, col_label]  — Label-based selection
# Kya karta hai: Row aur Column ke NAAM (label) se data nikalta hai.
# Kab use hota hai: Jab aapko pata ho ki row ka index label kya hai.
# df.loc[0, 'Name']         # Row 0 ki 'Name' column ki value
# df.loc[0:3, 'Name':'Age'] # Row 0 se 3 tak, 'Name' se 'Age' tak (INCLUSIVE dono ends)

# df.iloc[row_number, col_number]  — Integer/Position-based selection
# Kya karta hai: Row aur Column ke NUMBER (position) se data nikalta hai.
# Kab use hota hai: Jab aapko row/col ka exact position number pata ho.
# df.iloc[0, 1]              # Pehli row, dusra column
# df.iloc[0:3, 0:2]          # Row 0-2, Col 0-1 (EXCLUSIVE end)

# ⚠️ LOC vs ILOC ka IMPORTANT FARK:
# loc[0:3]  -> 0, 1, 2, 3 (3 INCLUDED hai — label based)
# iloc[0:3] -> 0, 1, 2    (3 EXCLUDED hai — position based, Python jaisa)

# ---- Conditional Filtering (WHERE jaisa) ----
# Kya karta hai: Condition laga kar rows filter karta hai.
# Kab use hota hai: "Mujhe sirf wo students dikhao jinka Age 25 se zyada hai"
# df[df['Age'] > 25]
# df[(df['Age'] > 20) & (df['Marks'] > 80)]   # Multiple conditions (&=AND, |=OR)


# =====================================================================
# 5. DATA CLEANING (Gandhe Data ko Saaf karna)
# =====================================================================
# Real-world data hamesha gandha hota hai! Missing values, duplicates, galat types — sab milega.

# ---- Missing Values (NaN) Handle karna ----

# df.isnull() / df.isna()
# Kya karta hai: Har cell mein True/False lagata hai — True matlab value missing hai.
# df.isnull()

# df.isnull().sum()
# Kya karta hai: Har column mein kitne missing values hain wo count deta hai.
# Kab use hota hai: Pehle dekhna ki kitna data missing hai.
# df.isnull().sum()

# df.dropna()
# Kya karta hai: Jis bhi row mein koi bhi NaN ho, poori row hata deta hai.
# Kab use hota hai: Bahut kam data missing ho tab use karo — warna bahut data chala jaayega!
# df.dropna()                    # Koi bhi NaN wali row hata do
# df.dropna(subset=['Age'])      # Sirf 'Age' column mein NaN wali rows hatao

# df.fillna(value)
# Kya karta hai: NaN values ko kisi value se replace/fill kar deta hai.
# Kab use hota hai: Zyada data missing ho toh drop karne ki jagah fill karo.
# df['Age'].fillna(0)                        # NaN ko 0 se bharo
# df['Age'].fillna(df['Age'].mean())         # NaN ko column ke average se bharo (BEST PRACTICE)
# df.fillna(method='ffill')                  # Forward fill — upar wali value se bharo
# df.fillna(method='bfill')                  # Backward fill — neeche wali value se bharo

# ---- Duplicates Handle karna ----

# df.duplicated()
# Kya karta hai: Duplicate rows ko True mark karta hai.
# df.duplicated()

# df.drop_duplicates()
# Kya karta hai: Duplicate rows hata deta hai (pehla wala rakhta hai).
# df.drop_duplicates()
# df.drop_duplicates(subset=['Name'])         # Sirf 'Name' column ke basis par duplicates hatao

# ---- Data Type Badalna ----

# df['col'].astype(type)
# Kya karta hai: Column ka data type change karta hai.
# Kab use hota hai: Jab CSV se padhne par "Age" column string ban jaaye, toh integer banana padta hai.
# df['Age'] = df['Age'].astype(int)
# df['Price'] = df['Price'].astype(float)

# ---- Column Rename karna ----
# df.rename(columns={'old_name': 'new_name'})
# df.rename(columns={'Marks': 'Score', 'Name': 'Student_Name'}, inplace=True)
# inplace=True matlab original DataFrame mein hi change ho jaayega (naya banana nahi padega)


# =====================================================================
# 6. DATA MANIPULATION (Data mein Changes karna)
# =====================================================================

# ---- Naya Column banana ----
# df['new_col'] = values
# Kab use hota hai: Existing columns se naya column derive karna ho.
# df['Pass'] = df['Marks'] >= 40                # True/False column
# df['Percentage'] = (df['Marks'] / 100) * 100  # Calculated column
# df['Grade'] = df['Marks'].apply(lambda x: 'A' if x >= 90 else 'B')  # Custom logic

# ---- Column ya Row Delete karna ----

# df.drop(columns=['col_name'])
# Kya karta hai: Column hata deta hai.
# df.drop(columns=['Marks'])
# df.drop(columns=['Marks', 'Age'])      # Multiple columns hatao

# df.drop(index=[0, 1])
# Kya karta hai: Row hata deta hai (index number se).

# ---- Sorting (Data ko Order mein laana) ----

# df.sort_values(by='col')
# Kya karta hai: Kisi column ke hisaab se rows ko sort karta hai.
# Kab use hota hai: "Sabse zyada marks wala student kaun hai" jaisa sawaal.
# df.sort_values(by='Marks')                     # Chhote se bade (ascending)
# df.sort_values(by='Marks', ascending=False)     # Bade se chhote (descending)
# df.sort_values(by=['Age', 'Marks'])             # Pehle Age se, phir Marks se sort

# ---- Apply Function (Har Element par Custom Logic) ----

# df['col'].apply(function)
# Kya karta hai: Kisi column ke har ek element par aapka function chala deta hai.
# Kab use hota hai: Complex transformations jo simple operators se nahi ho sakte.
# 
# Lambda function ke saath (chhota one-line function):
# df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')
#
# Normal function ke saath:
# def double(x):
#     return x * 2
# df['Double_Marks'] = df['Marks'].apply(double)

# ---- Map Function (Values Replace karna) ----
# df['col'].map(dictionary)
# Kya karta hai: Purani values ko naye values se replace karta hai dictionary ke basis par.
# df['Gender'] = df['Gender'].map({'M': 'Male', 'F': 'Female'})

# ---- Replace Function ----
# df['col'].replace(old, new)
# df['City'].replace('Dli', 'Delhi')


# =====================================================================
# 7. GROUPBY & AGGREGATION (Data ko Group karke Summary Nikalna)
# =====================================================================
# Ye SQL ke GROUP BY jaisa hai — industry mein SABSE ZYADA use hota hai!

# ---- df.groupby('col') ----
# Kya karta hai: Data ko groups mein todta hai aur phir har group par calculation karta hai.
# Kab use hota hai: "Har city ke students ka average marks kya hai?" type ke questions mein.
#
# Basic usage:
# df.groupby('City')['Marks'].mean()       # Har city ka average marks
# df.groupby('City')['Marks'].sum()        # Har city ka total marks
# df.groupby('City')['Marks'].count()      # Har city mein kitne students

# Multiple aggregations ek saath:
# df.groupby('City')['Marks'].agg(['mean', 'sum', 'count', 'max', 'min'])

# Multiple columns par groupby:
# df.groupby(['City', 'Gender'])['Marks'].mean()

# ---- Pivot Table (Excel ki Pivot Table jaisi) ----
# pd.pivot_table(df, values='Marks', index='City', columns='Gender', aggfunc='mean')
# Kab use hota hai: 2D summary table banana ho jaise Excel mein banate hain.


# =====================================================================
# 8. MERGING & JOINING (Do DataFrames ko Jodna)
# =====================================================================
# Jaise SQL mein JOIN hota hai, waise hi Pandas mein merge/join hota hai.

# ---- pd.merge(df1, df2) ----
# Kya karta hai: Do DataFrames ko ek common column ke basis par jodta hai.
# Kab use hota hai: Jab ek table mein student info ho aur doosre mein marks ho.
#
# df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
# df2 = pd.DataFrame({'ID': [1, 2, 4], 'Marks': [90, 80, 70]})
#
# Inner Join (sirf matching rows):
# pd.merge(df1, df2, on='ID', how='inner')    # Sirf ID 1 aur 2 aayenge
#
# Left Join (left table ke saare rows):
# pd.merge(df1, df2, on='ID', how='left')     # ID 3 bhi aayega (Marks NaN hoga)
#
# Right Join (right table ke saare rows):
# pd.merge(df1, df2, on='ID', how='right')    # ID 4 bhi aayega (Name NaN hoga)
#
# Outer Join (dono ke saare rows):
# pd.merge(df1, df2, on='ID', how='outer')    # Sab aayenge, missing mein NaN

# ---- pd.concat([df1, df2]) ----
# Kya karta hai: Do DataFrames ko upar-neeche (ya side-by-side) chipka deta hai.
# pd.concat([df1, df2])                  # Rows add ho jaayengi (upar-neeche)
# pd.concat([df1, df2], axis=1)          # Columns add ho jaayengi (side-by-side)


# =====================================================================
# 9. STRING OPERATIONS (Text/String Data par Kaam karna)
# =====================================================================
# Pandas mein .str accessor se sabhi Python string methods use kar sakte ho!

# df['Name'].str.lower()        # Sab chhote (lowercase) mein
# df['Name'].str.upper()        # Sab bade (uppercase) mein
# df['Name'].str.strip()        # Extra spaces hatao (aage/peeche ke)
# df['Name'].str.contains('ali')   # Kya 'ali' word hai isme? (True/False)
# df['Name'].str.replace('Bob', 'Robert')  # Bob ko Robert se replace karo
# df['Name'].str.split(' ')     # Space se todke list bana do
# df['Name'].str.len()          # Har name ki length kitni hai


# =====================================================================
# 10. DATE & TIME OPERATIONS (Tareekh/Date ke saath Kaam karna)
# =====================================================================
# Time-series data (jaise stock prices, sales data) mein bahut important!

# ---- pd.to_datetime(col) ----
# Kya karta hai: String date ko proper DateTime object mein badalta hai.
# Kab use hota hai: CSV se date string aaye toh usse DateTime banana padta hai calculations ke liye.
# df['Date'] = pd.to_datetime(df['Date'])

# ---- Date se Parts Nikalna ----
# df['Date'].dt.year          # Sirf saal
# df['Date'].dt.month         # Sirf mahina
# df['Date'].dt.day           # Sirf din
# df['Date'].dt.day_name()    # Din ka naam (Monday, Tuesday...)
# df['Date'].dt.hour          # Ghanta (agar time bhi ho toh)

# ---- Date Range banana ----
# pd.date_range(start='2024-01-01', periods=10, freq='D')  # 10 din ki dates
# freq options: 'D'=Daily, 'W'=Weekly, 'M'=Monthly, 'Y'=Yearly, 'H'=Hourly


# =====================================================================
# 11. ADVANCED OPERATIONS (Pro-Level Functions)
# =====================================================================

# ---- df.query() ----
# Kya karta hai: SQL jaisa syntax mein filter karta hai (readable hota hai).
# df.query('Age > 25 and Marks > 80')
# Same as: df[(df['Age'] > 25) & (df['Marks'] > 80)]

# ---- df.sample(n) ----
# Kya karta hai: DataFrame se random n rows nikalta hai.
# Kab use hota hai: Bahut bada dataset ho toh chhota sample lekar test karna.
# df.sample(5)         # Random 5 rows
# df.sample(frac=0.1)  # 10% data randomly

# ---- df.nlargest(n, 'col') / df.nsmallest(n, 'col') ----
# Kya karta hai: Top n ya bottom n rows deta hai kisi column ke basis par.
# df.nlargest(3, 'Marks')    # Top 3 highest marks wale students
# df.nsmallest(3, 'Age')     # 3 sabse kam age wale students

# ---- df.corr() ----
# Kya karta hai: Sabhi numeric columns ke beech correlation calculate karta hai.
# Kab use hota hai: ML mein features ke beech relationship samajhne ke liye.
# df.corr()
# Value +1 ke paas = strong positive relation
# Value -1 ke paas = strong negative relation
# Value 0 ke paas = koi relation nahi

# ---- df.melt() ----
# Kya karta hai: Wide format data ko long format mein convert karta hai.
# Kab use hota hai: Visualization ke liye Seaborn ko long format chahiye hota hai.
# pd.melt(df, id_vars=['Name'], value_vars=['Math', 'Science'])

# ---- df.set_index('col') ----
# Kya karta hai: Kisi column ko row index bana deta hai.
# df.set_index('Name')

# ---- df.reset_index() ----
# Kya karta hai: Index ko wapas normal column bana deta hai.
# df.reset_index()

# ---- df.copy() ----
# Kya karta hai: DataFrame ki ek independent copy banata hai.
# Kab use hota hai: ZAROORI hai jab original data safe rakhna ho!
# df2 = df.copy()   # df2 mein changes karo, df safe rahega
# ⚠️ df2 = df likhoge toh dono SAME hain — ek mein change dono mein dikhega!


# =====================================================================
# 12. COMMON PATTERNS (Industry mein Roz kaam aane wale Patterns)
# =====================================================================

# ---- Pattern 1: CSV Read -> Explore -> Clean -> Analyze ----
# df = pd.read_csv('data.csv')
# df.head()
# df.info()
# df.isnull().sum()
# df.dropna(inplace=True)       # inplace=True taaki naya variable na banana pade
# df.describe()

# ---- Pattern 2: GroupBy -> Aggregate -> Sort ----
# result = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
# Top cities by sales!

# ---- Pattern 3: Filtering + New Column ----
# df['Status'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
# pass_students = df[df['Status'] == 'Pass']

# ---- Pattern 4: Multiple CSV files combine karna ----
# import glob
# files = glob.glob('data/*.csv')
# all_data = pd.concat([pd.read_csv(f) for f in files])


# =====================================================================
# 📊 QUICK REFERENCE TABLE
# =====================================================================
# 
# | Function              | Kya Karta Hai                    | Kitna Use Hota Hai |
# |-----------------------|----------------------------------|---------------------|
# | pd.read_csv()         | CSV file padhta hai              | ⭐⭐⭐⭐⭐            |
# | df.head()             | Pehli 5 rows dikhata hai         | ⭐⭐⭐⭐⭐            |
# | df.info()             | Data types + missing info        | ⭐⭐⭐⭐⭐            |
# | df.describe()         | Statistical summary              | ⭐⭐⭐⭐⭐            |
# | df.isnull().sum()     | Missing values count             | ⭐⭐⭐⭐⭐            |
# | df.fillna()           | Missing values bharta hai        | ⭐⭐⭐⭐⭐            |
# | df.dropna()           | Missing rows hatata hai          | ⭐⭐⭐⭐             |
# | df.groupby()          | Data group + aggregate           | ⭐⭐⭐⭐⭐            |
# | df.sort_values()      | Data sort karta hai              | ⭐⭐⭐⭐⭐            |
# | df.apply()            | Custom function lagata hai       | ⭐⭐⭐⭐⭐            |
# | pd.merge()            | 2 tables join karta hai          | ⭐⭐⭐⭐             |
# | df.loc[] / df.iloc[]  | Rows/Cols select karta hai       | ⭐⭐⭐⭐⭐            |
# | df.value_counts()     | Category distribution            | ⭐⭐⭐⭐             |
# | df.corr()             | Correlation matrix               | ⭐⭐⭐⭐             |
# | pd.to_datetime()      | String ko Date mein badalta hai  | ⭐⭐⭐⭐             |
# | df.to_csv()           | DataFrame save karta hai         | ⭐⭐⭐⭐⭐            |
# =====================================================================
