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
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = [ 'chicago', 'new york city', 'washington']
    while True:
        city = input('What is the city are you looking for? ').lower()
        if city in cities:
            break
        else:
            print('Please insert a valid input (chicago, new york city or washington)')


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Name the month to filter by, or type all for a year: ').lower()
        if month in months:
            break
        else:
            print('Please insert a valid input (january, february, march, april, may, june)')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input ('name of the day of week to filter by, or "all": ').lower()
        if day in days:
            break
        else:
            print('Please insert a valid input')

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

   # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
#should i write here load_data('city', 'month', 'day')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most popular month is ",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most popular day of week is ", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most popular start hour is ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df["Start Station"].mode()[0]
    print("\nThe most commonly used start station is: ", most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df["End Station"].mode()[0]
    print("\nThe most commonly used end station is: ", most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["most_frequent_combination"] = df["Start Station"] + df["End Station"]
    most_frequent_combination = df['most_frequent_combination'].value_counts().head(1)
    print("\nMost frequent combinations is: ", most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    #df['End Time'] = df['End Time'].dt.hour
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if city == "chicago" or city == "new york city":

        user_type_counts = df['User Type'].value_counts()
        print("Count of user type: ", user_type_counts)
    # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("Counts of genders: ", gender_counts)


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = df['Birth Year'].min()
        print("Earlist year birth: ", earliest_year_birth)
        most_common_birth = df['Birth Year'].sum().max()
        print("Most common birth", most_common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print('-'*40)

    #view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    #start_loc = 0
    #start_loc += 5
    #while view_data == 'yes':
        #print(df.iloc[:6])
        #if view_data == 'no':
            #break

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[:6])
        start_loc += 5
        view_data = input("Do you wish to continue?: type yes or no").lower()

        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nThank you!\n")
            break



if __name__ == "__main__":
	main()
