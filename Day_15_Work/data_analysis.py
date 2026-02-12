import pandas as pd


def main():
    # 1. Load CSV dataset into Pandas DataFrame

    filepath = "StudentPerformanceFactors.csv"

    df = pd.read_csv(filepath)

    # 2. Display the first few rows of the DataFrame

    print("First 5 rows of the DataFrame:")
    print(df.head())
    
    # 3.Explore dataset using head, info, describe.

    print("Dataset info : ")
    print(df.info())

    print("Summary statistics : ")
    print(df.describe(include='all'))

    # 4. Handle missing values 
    print("Missing values in each column:")
    print(df.isnull().sum())
    df = df.dropna()
    print("Missing values after dropping rows with missing data:")

    # 5.Filter and sort data.
    print("Students with Exam_Score above 70:")
    high_scores = df[df['Exam_Score'] > 70]
    print(high_scores)

    print("Students sorted by Exam_Score:")
    sorted_by_reading = df.sort_values(by='Exam_Score', ascending=False)
    print(sorted_by_reading)
    
    # 6. Group data and calculate aggregate statistics.
    grouped = df.groupby('Parental_Education_Level')
    print("Aggregate statistics by parent education:")
    print(grouped.agg({'Exam_Score': ['mean', 'count'], 'Previous_Scores': ['mean', 'count']}))

    # 7.Add new calculated columns.
    df['average_score'] = df[['Exam_Score', 'Previous_Scores']].mean(axis=1)
    print("DataFrame with new average score column:")
    print(df.head())

    # 8. Save the modified DataFrame to a new CSV file.
    output_filepath = "Modified_StudentPerformanceFactors.csv"
    df.to_csv(output_filepath, index=True)

    # 9.Interpret insights.
    print("Insights:") 
    print("1. The average score of students is calculated based on their exam score and previous scores.") 
    print("2. Students with higher parental education levels tend to have higher average scores.") 
    
if __name__ == "__main__":
    main()
    
   
    

