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

    while True:
        try:
            city = str(input('Would you like to see data for Chicago, New York or Washington ?'))
            if city.lower() == "new york" or city.lower() == "washington" or city.lower() == "chicago":
                break
        except ValueError:
             print("Please, give a valid city input. Write Chicago or New York or Washington")


    print("You select to see data for city: {}".format(city))

    # get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = str(input('Which Month ? January, February, March, April, May, June or all ?'))
            if month.lower() == "january" or month.lower() == "february" or month.lower() == "march" or month.lower() == "april" or month.lower() == "may" or month.lower() == "june" or month.lower() == "all":
                break
        except ValueError:
            print( "Please, give a valid month input. Write January, February, March, April, May, June or all.")

    print("You select to see data for month: {}".format(month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Which Day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all ?'))
            if day.lower() == "sunday" or day.lower() == "monday" or day.lower() == "tuesday" or day.lower() == "wednesday" or day.lower() == "thursday" or day.lower() == "friday" or day.lower() == "saturday" or day.lower() == "sunday" or day.lower() == "all":
                break
        except ValueError:
             return "Please, give a valid day input."

    print("You select to see data for day: {}".format(day))
    # print(city.lower())

    if city == "chicago":
        city = 'chicago'
    elif city == "new york":
        city = 'new york city'
    elif city == "washington":
        city = 'washington'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day """

    # load data file into a dataframe


    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['week_day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['week_day'] == day.title()]

    return df



def time_statistics(df):
    """Displays statistics on the most frequent times of travel. """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month is: " + most_common_month)

    # display the most common day of week
    most_common_day = df['week_day'].mode()[0]
    print("Most common Day of Week is: " + most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common hour is: " + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station is : {}".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("Most Commonly used end station: {}".format(end_station))

    # display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print("Most frequent used combination of start station and end station trip is: " + start_station + " & ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel duration is: {}".format(total_travel_time))


    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time is: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user type are: {}".format(user_types))

    # Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('Counts of Gender Types are : {}\n'.format(gender_types))
    except:
        print("No available data for Gender Types")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print("Earliest year of birth is: {}\n".format(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print("The most recent year of birth is: {}\n".format(most_recent_year))

        most_common_year = df['Birth Year'].mode()[0]
        print("The most common year of birth is: {}\n".format(most_common_year))
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        start_loc = start_loc + 5
        print(df.iloc[start_loc:start_loc+5])



def main():
    while True:
        city, month, day = get_filters()
        #print(city + month + day)
        df = load_data(city, month, day)

        time_statistics(df)
        station_statistics(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
