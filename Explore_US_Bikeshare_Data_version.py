import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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

    while True:
        city = input('Would you like to see data for chicago, new york city, or washington?').lower()
        if not city in cities:
            print('Please choose from the options.')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Which month? all, january, february, march, april, may, or june?')
        if not month in months:
            print('Please choose from the options.')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Which day? all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday?')
        if not day in days:
            print('Please choose from the options.')
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == days.index(day) -1 ]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_and_end_station = df[['Start Station', 'End Station']].mode()
    print('Most frequent combination of start station and end station trip:\n', common_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time:', travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of gender:', gender)
    except KeyError:
        print('Gender is unknown.')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest year of birth:', earliest_birth_year)
    except KeyError:
        print('Earliest year of birth is unknown.')

    try:
        recent_birth_year = df['Birth Year'].max()
        print('Most recent year of birth:', recent_birth_year)
    except KeyError:
        print('Most recent year of birth is unknown.')

    try:
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common year of birth:', common_birth_year)
    except KeyError:
        print('Most common year of birth is unknown.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    index = 0
    user_input = input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index + 5 < df.shape[0]:
        print(df.iloc[index: index + 5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
