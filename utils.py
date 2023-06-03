import pandas as pd 

def unique_values(column_name):
    try:
        df = pd.read_csv('notebooks/data/eda_data.csv')
        columns = df.columns
        if column_name in columns:
           output = df[column_name].unique()
           return [val for val in output if val not in ('-1','Unknown','na')]
        
    except Exception as e:
        return "column does not exist, enter valid column"





if __name__ == "__main__":
    print(unique_values('Type of ownership'))