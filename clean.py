import pandas as pd


def clean(input_file1,input_file2,output_file):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df3 = pd.merge(df1, df2, left_on="respondent_id", right_on="id").drop('respondent_id', axis=1)
    df3 = df3.dropna()
    insur_check = df3['job'].str.contains('insurance|Insurance')
    df3 = df3[~insur_check]
    print(df3.shape)
    return df3


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file (CSV)')
    parser.add_argument('input2', help='Data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1,args.input2,args.output)
    cleaned.to_csv(args.output, index=False)