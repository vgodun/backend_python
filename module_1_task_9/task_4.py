list_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('First day:', list_day[0])
print('Last day:', list_day[-1])
print('Middle days: ',list_day[1:6])
list_day[list_day.index('Wednesday')] = 'Humpday'
print('Updated list: ', list_day)