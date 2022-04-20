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
            # Ask the user to input the city name. lower() mehod is used to math the text style in CITY-DATA 
            # dictionary and to handle case senstivity like (ex. ChiCAGO)
            city_sel = str(input('Would you like to see data for Chicago, New York City or Washington?\n').lower())
            # check if the user input the correct city name and generate message to re-input the city name if 
            # it's not correct, in addition to handle exception
            if city_sel in CITY_DATA.keys():
                # Display a message confirming the user selection
                print('you want hear about the data of {} !'.format(city_sel))
                city = city_sel
               
                # break the loop if the user enter a correct city name out of the three cities provided
                break 
            else:
                # Display an error if the user did not enter a correct city name 
                print('\n That\'s not a valid city name')
        except KeyboardInterrupt:
            #display an error if the user did not enter any input , or enter( ctrl+c) or del
            print('\n KeyboardInterrupt Error: No Input Taken')
  
    # get user input for month (all, january, february, ... , june) or
    # day of the week (all, monday, tuesday, ... sunday) or both or None for no time filters

    month = 'a'
    day = 0 
    while True:
        try:
            # get user input for month (all, january, february, ... , june) or 
            # both or none
            X = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter\n').lower()
            
            # create 3 lists for months, days, 'all' string. 
            # these lists are utilized for reference in the following IF conditions
            # in accord to user selection
            months =['January','February','March','April','May', 'June']
            days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            all_st = ['all', 'ALL', 'All','ALl','AlL','aLL','alL','aLl']
            
            # conditions if the user selects filter by month
            if X == 'month':
                #Ask the user which month data need to be displayed
                month_sel = str(input('Which month? All, January, February, March, April, May,June? please enter a full month name\n').title())
                # check if the user enter 'all', all-st list contains all the cases of 'all' that the user
                # may input, to make it Case insenstive
                if month_sel in all_st:
                    print('All the data from january to June will be displayed')
                    month = month_sel.lower()
                    day = 'all'
                    #break is used to break the loop
                    break
                # check if the user enters specific month and refer to it in months list
                elif month_sel in months:
                    month = month_sel
                    print('The data will be filtered by month\n')
                    day = 'all'
                    break                
                else: 
                  # Display an error if the user did not enter a correct input  
                  print('That\'s not a valid input')      
                  
            # conditions if the user selects filter by day    
            elif X == 'day':
                # Ask the user which day data need to be displayed
                day_sel = str(input('Which day? All, Sunday, Monday, Tuesday, Wednesday, Thursday ,Friday, Saturday? please enter a full day name\n').title())
                # check if the user enter 'all', all-st list contains all the cases of 'all' that the user
                # may input, to make it Case insenstive                
                if day_sel in all_st:
                    print('The data for all days will be displayed')
                    day = day_sel.lower()
                    month = 'all'
                    break
                # check if the user enters specific day and refer to it in days list
                elif day_sel in days:
                    day = day_sel
                    print('The data will be filtered by day\n')
                    month = 'all'
                    break                    
                else: 
                    # Display an error if the user did not enter a correct input
                    print('That\'s not a valid input')
                                     
            # conditions if the user selects filtering Both by month and day  
            elif X == 'both':
                #Ask the user which month data need to be displayed
                month_sel = str(input('Which month? All, January, February, March, April, May,June? please enter a full month name\n').title())
                # check if the user enter 'all', all-st list contains all the cases of 'all' that the user
                # may input, to make it Case insenstive                
                if month_sel in all_st:
                    print('All the data from january to June will be displayed')
                    month = month_sel.lower()
                # check if the user enters specific month and refer to it in months list
                elif month_sel in months:
                    month = month_sel
                    print('The data will be filtered by month\n') 
                    
                # Ask the user which day data need to be displayed
                day_sel = str(input('Which day? All, Sunday, Monday, Tuesday, Wednesday, Thursday ,Friday, Saturday? please enter a full day name\n').title())
                # check if the user enter 'all', all-st list contains all the cases of 'all' that the user
                # may input, to make it Case insenstive                
                if day_sel in all_st:
                    print('The data for all days will be displayed')
                    day = day_sel.lower()
                    break
                # check if the user enters specific day and refer to it in days list
                elif day_sel in days:
                    day = day_sel
                    print('The data will be filtered by day\n')
                    break
                # display a message if the user enter incorrect input either in month or day                  
                if (month_sel not in all_st) or (month_sel not in months) or (day_sel not in all_st) or (day_sel not in days):
                    print('That\'s not a valid input')
                    
            # display a message if no time filter required
            elif X == 'none':
                # No time filter required
                print('No time filter required')
                break
            else:
                # Display an error if the user did not enter a correct input
                print('\n That\'s not a valid input\n')
                
        except KeyboardInterrupt:
                    #display an error if the user did not enter any input , or enter( ctrl+c) or del
                    print('\n KeyboardInterrupt Error: No Input Taken')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January','February','March','April','May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
  
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    popular_month = df['month'].mode()[0]
    
    # calculate the count of the most common month
    count_popular_month = (df.month.values == popular_month).sum()
  
    
    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
 
    
    # calculate the count of the most common day of the week
    count_pop_day_of_week = (df.day_of_week.values == popular_day_of_week).sum()
 
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour    
    
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    
    # calculate the count of the most populr hour
    count_popular_hour = (df.hour.values == popular_hour).sum()
    
    print('The Most Popular hour: {} , count : {}'.format(popular_hour,count_popular_hour))
    print('The Most Popular month: {} , count : {}'.format(popular_month,count_popular_month))
    print('The Most Popular day of the week: {} , count : {}'.format(popular_day_of_week,count_pop_day_of_week)) 
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    # calculate the count of the most commonly used start station
    count_start_stations = df['Start Station'].value_counts()
    count_pop_start_station = count_start_stations[popular_start_station]
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    # Calculate the count of the most popular End Station
    count_end_stations = df['End Station'].value_counts()
    count_pop_end_station = count_end_stations[popular_end_station]
    
    # display most frequent combination of start station and end station trip
    stations_combination= df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False)
    frequent_stations =df.groupby(['Start Station','End Station']).size().idxmax()
    count_freq_station = stations_combination.max()
    
    print('The Most Popular Start Station: {} , count : {}'.format(popular_start_station,count_pop_start_station))
    print('The Most Popular End Station: {} , count : {}'.format(popular_end_station,count_pop_end_station))
    print('The Most frequent combination of start and end stations: {} , count : {}'.format(frequent_stations,count_freq_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    
    print('The Total travel time: {}, The Average travel time: {}'.format(total_travel_time,average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()    
    gender = 'Gender'
    birth = 'Birth Year'
    gender_types = 'NA'
    recent_birth_year = 0

    if (gender in df.columns) or (birth in df.columns):
        # Display counts of gender
        gender_types = df['Gender'].value_counts()
        
        # Display earliest, most recent, and most common year of birth
        recent_birth_year = df['Birth Year'].max()
        print(gender_types)
        print('The most recent birth year: {}'.format(int(recent_birth_year)))
    else:
        print('Gender and Birth year data are not available for Washington city')
        
  
    print(user_types)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
