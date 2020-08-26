import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new_york_city','washington']
months = ['all','january','february','march','april','may','june']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_inp = int(input("Enter the City to analyse about as: \n'1' for chicago,\n'2' for new york city,\n'3' for washington\n"))
            if city_inp not in (1, 2, 3):
                print("Not an appropriate choice of city.")
            else:
                break
        except ValueError as v :
            print("Please enter valid number",v)
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_inp = int(input("Enter the month of {} city to analyse about as: \n'1' for all,\n'2' for january,\n'3' for february,\n'4' for march,\n'5' for april,\n'6' for may,\n'7' for june,\n".format(cities[city_inp - 1])))
            if month_inp not in (1,2,3,4,5,6,7):
                print("Not an appropriate choice of month.")
            else:
                break
        except ValueError as v :
            print("Please enter valid number",v)
                             
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day_inp = int(input("Enter the day of {} of {} city to analyse about as: \n'1' for all,\n'2' for monday,\n'3' for tuesday,\n'4'for wednesday,\n'5' for thursday,\n'6' for friday,\n'7' for saturday,\n'8' for sunday\n".format(months[month_inp - 1],cities[city_inp - 1])))
            print(month_inp)
            if month_inp not in (1,2,3,4,5,6,7,8):
                print("Not an appropriate choice of day.")
            else:
                break
        except ValueError as v :
            print("Please enter valid number",v)
    print("You have enquired about {}'s {} for the month of {}".format(cities[city_inp - 1],days[day_inp - 1],months[month_inp - 1]))
    print('-'*40)
    return city_inp, month_inp, day_inp


def load_data(city, months, days):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file = "./{}.csv".format(cities[city - 1])
    df = pd.read_csv(file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['end_year'] = df['End Time'].dt.year
    df['end_month'] = df['End Time'].dt.month
    df['week_day'] = df['Start Time'].dt.dayofweek
    df['end_week_day'] = df['End Time'].dt.dayofweek
    df['start_hour'] = df['Start Time'].dt.hour
    #in this function ..till here we have manipulated the dataframe to include extra column with Year,Month,Weekday
    #now applying appropriate filter to the dataframe to bw done with this function
    if months != 1:
        df = df[df['month'] == months - 1]
    if days != 1:
        df = df[df['week_day'] == days - 2]
    df = df.fillna(0)
    return df
    #print(df[['Start Time','month','week_day']])
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mon = df['month'].value_counts()[:1].index.tolist()
    print("Most Common Month is {}".format(months[mon[0]]))


    # TO DO: display the most common day of week
    weday = df['week_day'].value_counts()[:1].index.tolist()
    print("Most Common Day is {}".format(days[weday[0]+1]))

    # TO DO: display the most common start hour
    hr = df['start_hour'].value_counts()[:1].index.tolist()
    print("Most Common start hour is {}".format(hr[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    st_st = df['Start Station'].value_counts()[:1].index.tolist()
    print("Most Common Start Station is {}".format(st_st[0]))

    # TO DO: display most commonly used end station
    end_st = df['End Station'].value_counts()[:1].index.tolist()
    print("Most Common End Station is {}".format(end_st[0]))

    # TO DO: display most frequent combination of start station and end station trip
    both_st = df[['Start Station','End Station']].value_counts()[:1].index.tolist()
    print("Most Common Start-End Station is {} and {}".format(both_st[0][0],both_st[0][1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_column = df['Trip Duration'].sum(axis=0)
    print("The Total Travel time is :",sum_column)

    # TO DO: display mean travel time
    mean_column = df['Trip Duration'].mean(axis=0)
    print("The Mean Travel time is :",mean_column)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usty = df['User Type'].value_counts()[:2].index.tolist()
    print("{} user types are there of:{}".format(usty[0],df['User Type'].value_counts()[usty[0]]))
    print("{} user types are there of:{}".format(usty[1],df['User Type'].value_counts()[usty[1]]))

    # TO DO: Display earliest, most recent, and most common year of birth

    #Evaluator i am not being able to find the earliest birth year without countering my NaN placeholder value of '0',
    #please do provide with the solution for this part only
    try:
        # TO DO: Display counts of gender
        gndr = df['Gender'].value_counts()[:2].index.tolist()
        print("{} gender are there of:{}".format(gndr[0],df['Gender'].value_counts()[gndr[0]]))
        print("{} gender types are there of:{}".format(gndr[1],df['Gender'].value_counts()[gndr[1]]))
        common_bday = df['Birth Year'].value_counts()[:].index.tolist()
        print("Most common birth Year is {}".format(common_bday[0]))
        #df_earl = df.sort('Birth Year')
        print("Most recent birth year is {}".format(df['Birth Year'].max()))
        df.sort_values("Birth Year", axis = 0, ascending = False,inplace = True, na_position ='last')
        print("Most earliest birth year is {}".format(df['Birth Year'][0]))
    except Exception as e:
        print('Dataset incomplete error ! ',e)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def disp_raw(df):
    start = -5
    end = 0
    while True:     
        start += 5
        end += 5
        restart = input('\nWould you like to see the data? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        else:
            print("Data below from index {} to {}:\n{}".format(start,end,df[start:end]))
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

