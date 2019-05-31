# from .models import Quiz

class Time:
    def __init__(self, hour=0, minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second= second
    
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def int_to_time(self, seconds):
        '''
        Takes an argument
            - Seconds
        '''
        minutes,self.second = divmod(seconds,60)
        self.hour, self.minute = divmod(minutes,60)
        return '%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes*60 + self.second
        return seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_sec() + other.time_to_sec()
#         return self.int_to_time(seconds)

# class Timer:
#     def __init__(self, start, duration):
#         pass


# if __name__ == '__main__':
#     start = Time(3,40,34)
#     duration = Time(0,0,2400)
#     duration.int_to_time(2400)
    
#     start_seconds = start.time_to_sec()
#     print("Start Time:", start)
#     print("Duration:", duration)
    
#     # print("Start Time In Seconds:",start_seconds+' seconds')
#     print("Start Seconds in Time:", start.int_to_time(start_seconds))

#     print("End:", start + duration)
