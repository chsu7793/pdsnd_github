import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter chicago, new york city, or washington for yoru query: ").lower().strip()
    while city not in CITY_DATA:
        city = input("Enter a valid city name: chicago, new york city, or washington: ").lower().strip()

    # get user input for month (all, january, february, ... , june)

    month = input("Enter an integer to select a month between January to June (e.g.,enter 1 = janurary), or all for all months for your query: ").strip().lower()
    while month not in ["1", "2", "3", "4", "5", "6", 'all']:
        month = input("Enter a valid integer from 1 to 6, or all to select all months: ").strip().lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a day of week from Monday to Sunday, or all:  ").strip().lower()
    while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", 'all']:
        day = input("Enter a valid day of week, or enter all:  ").strip().lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#    city, month, day = get_filters()
    df = pd.read_csv(CITY_DATA[city])
    #create a datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #create a month column from start time
    df['month'] = df['Start Time'].dt.month
    #create a day of week column from start time
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #create hour column from start time
    df['hour'] = df ['Start Time'].dt.hour
    #logical operation to select df with specific month and day data from input
    if month != 'all':
        df = df[df['month'] == int(month)]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
#    print(df.head())
    return df
#load_data()
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
#    df = load_data()
    # display the most common month
    common_month = df['month'].mode()[0]
    print("the most common month is: {}".format(common_month))
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("the most common day is: {}:".format(common_day))
    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("the most common start hour is: {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#time_stats()
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
#    df = load_data()
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(common_start_station))
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    #create a column that combine start and end stations, and return mode.
    df['Start End'] = df['Start Station'] + ' ' + df['End Station']
    common_start_end = df['Start End'].mode()[0]
    print("The most frequent combo for start and end station is: {}".format(common_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#station_stats()
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
#    df = load_data()
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is: {} mins".format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("total average travel time is: {} mins".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#trip_duration_stats()
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
#    df = load_data()
    user_types = df['User Type'].value_counts()
    print("The user types are as follows: \n{}".format(user_types))
    # Display counts of gender
    gender = df['Gender'].value_counts()
    print("The counts of each gender of users are as follows:\n{}".format(gender))
    # Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    print("The earliest birth year of user is: {}".format(earliest))
    recent = df['Birth Year'].max()
    print("The most recent birth year of users is: {}".format(recent))
    common_birthyear = df['Birth Year'].mode()[0]
    print("The most common birth year of users is: {}".format(common_birthyear))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#user_stats()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
