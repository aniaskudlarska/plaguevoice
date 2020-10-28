import pandas as pd

def main():
    #Create a dummy pandas dataframe
    dummy_df=pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    #Write the dataframe to a csv
    dummy_df.to_csv('sample_dummy_file.csv')
    print('Automating the boring work makes our lives so much better!')

if __name__ == "__main__":
        main()