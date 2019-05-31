class Time:
    """ Represents the time of the day"""
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute,self.second)

    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes*60 + self.second
        return seconds

    def int_to_time(self,seconds):
        time = Time()
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes,60)
        return time

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)    

    def increment(self, seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)

if __name__ == '__main__':
    start = Time(9,45)
    duration = Time(1,35)
    print(start+duration)


    # def time_to_int(time):
    # minutes = time.hour * 60 + time.minute
    # seconds = minutes*60 + time.second
    # return seconds

    # def int_to_time(seconds):
    # time = Time()
    # minutes, time.second = divmod(seconds, 60)
    # time.hour, time.minute = divmod(minutes,60)
    
    # return time
    # def add_time(t1,t2):
    # seconds = time_to_int(t1) + time_to_int(t2)
    # return int_to_time(seconds)


# if __name__ == '__main__':
#     start = Time()
#     start.hour  = 10
#     start.minute = 45
#     start.second = 30
#     print_time(start)

'''
class Time:
    """
    Represents the time of day
    attributes: hour, minute, second
    """

    def __str__(self):
        return '%2d:%2d:%2d' %(self.hour, self.minute, self.second)
if __name__ == '__main__':
    # t1 = Time() # call the Time class
    # t2 = Time() # call the Time class


    start = Time()
    start.hour = 9
    start.minute = 25
    start.second = 40

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes*60 + time.second
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes,60)
        return time
    def add_time(t1,t2):
        seconds = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

    seconds = time_to_int(start)
    print(int_to_time(seconds))

    '''

    # duration = Time()
    # duration.hour = 8
    # duration.minute = 25
    # duration.second = 20

    # done = add_time(start, duration)
    # print(done)

    # def add_time(t1, t2):
    #     sum = Time()
    #     sum.hour = t1.hour + t2.hour
    #     sum.minute = t1.minute + t2.minute
    #     sum.second = t1.second + t2.second
        
    #     if sum.second >= 60:
    #         sum.second -= 60
    #         sum.minute += 1
        
    #     if sum.minute >= 60:
    #         sum.minute -= 60
    #         sum.hour += 1

    #     return sum
    

# import time, sys
# force = list if sys.version_info[0] == 3 else (lambda X:X)





# class Timer:
#     def __init__(self):
#         self.start = time.clock()
#         self.elapsed = time.clock() - self.start

# if __name__ == '__main__':
#     timer = Timer()
#     print('Start Time:',timer.start)
#     print('Elapsed:',timer.elapsed)



# # class timer:
# #     def __init__(self, func):
# #         self.func = func
# #         self.alltime = 0
    
# #     def __call__(self, *args, **kwargs):
# #         start = time.clock()
# #         result = self.func(*args, **kwargs)
# #         elapsed = time.clock() - start
# #         self.alltime += elapsed
# #         print("%s: %.5f, %.5f" % (self.func.__name__, elapsed, self.alltime))
# #         return result

# # @timer
# # def listcomp(N):
# #     return [x * 2 for x in range(N)]


# # @timer
# # def mapcall(N):
# #     return force(map((lambda x: x* 2), range(N)))



# # result = listcomp(5)
# # listcomp(500000)
# # listcomp(500000)
# # listcomp(1000000)
# # print(result)
# # print("alltime = %s" % listcomp.alltime)


# # print('')
# # result = mapcall(5)
# # mapcall(500000)
# # mapcall(500000)
# # mapcall(1000000)
# # print(result)
# # print("allTime = %s "% mapcall.alltime)

# # print("\n**map/comp = %s" % round(mapcall.alltime / listcomp.alltime,3))
