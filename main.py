#Function_1




#Function_2



#Function_3



#Function_4



#Function_5
### START FUNCTION
""""This code serves to calculate the number of tweets per day, 
    taking in a pandas dataframe as input and returning a new dataframe grouped by day and number of tweets """
def number_of_tweets_per_day(df):
    # your code here
    # We slice the portion of the code needed.
    df['Date'] = [date[0:10] for date in df['Date']]
    # Drop the duplicated column.
    new_df = df.drop(columns=['Date'],axis=1)
    # Group the contents of the column by the sliced date.
    new_df = new_df.groupby(df['Date']).count() 
    return new_df

### END FUNCTION




#Function_6




#Function_7