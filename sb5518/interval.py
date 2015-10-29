
""" Class interval is used to create and operate with intervals. It has a constructor that takes a String that is a representation of an Interval and
convert it into an interval object with the proper attributes (lower bound, upper bound, real lower bound, real upper bound, lower bound inclusive or
exclusive, upper bound inclusive or exclusive.

Examples of intervals

        [1,4] represents the numbers 1 through 4
		(2,5] represents the numbers 3 through 5
		[4,8) represents the numbers 4 through 7
		(3,9) represents the numbers 4 through 8.

It is important to notice that any string that starts with a valid interval will be considered valid input. It is assumed that if something is introduced
by the user after the interval, it is a typo.

The class has as well a __str__ function to print valid representations of the intervals.

Apart from these, the interval class contains some static methods to operate with intervals:

- mergeIntervals(int1, int2) that takes two intervals. If the intervals overlap or are adjacent, returns a merged interval.
It is important to clarify that all merged intervals will be valid inclusive bounds intervals.

- mergeOverlapping(intervals) that takes a list of intervals and merges all overlapping and adjacent intervals
(I assume that the homework required adjacent intervals as well like in the previous point). It uses the mergeIntervals method

- insert(intervals, newint) that takes two arguments: a list of non-overlapping intervals; and a single interval and try to insert this interval intro the rest.
It uses the previous methods.

Class MyError is used to raise errors along the class.

"""

import re


class MyError(Exception):  #This class is used to raise errors in the interval class
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)


class interval:

    def __init__(self,string_interval):
        pattern = '(\(|\[)(-?\d+),(-?\d+)(\)|\])' # This is the pattern that will try to match a valid interval at the beggining of a string
        self.is_interval_valid = False
        matched_string=re.match(pattern,string_interval)

        if matched_string == None:
            raise MyError("Invalid Interval String Format") #This error is raised when the patter does not match the beggining of the string

        else:
            self.lower_bound = matched_string.group(2)
            self.upper_bound = matched_string.group(3)
            self.lower_bound = int(self.lower_bound)
            self.upper_bound = int(self.upper_bound)
            if (matched_string.group(1)=='['):
                self.is_lower_bound_inclusive = True
                self.real_lower_bound = self.lower_bound
            if (matched_string.group(1)=='('):
                self.is_lower_bound_inclusive = False
                self.real_lower_bound = self.lower_bound + 1
            if (matched_string.group(4)==']'):
                self.is_upper_bound_inclusive = True
                self.real_upper_bound = self.upper_bound
            if (matched_string.group(4)==')'):
                self.is_upper_bound_inclusive = False
                self.real_upper_bound = self.upper_bound - 1



        if ((self.is_lower_bound_inclusive == True and self.is_upper_bound_inclusive == True) and (self.lower_bound<=self.upper_bound)):
            self.is_interval_valid = True
        elif ((self.is_lower_bound_inclusive == True and self.is_upper_bound_inclusive == False) or (self.is_lower_bound_inclusive == False and self.is_upper_bound_inclusive == True)) and self.lower_bound<=self.upper_bound:
            self.is_interval_valid = True
        elif ((self.is_lower_bound_inclusive == True) and (self.is_upper_bound_inclusive == True)) and self.lower_bound < self.upper_bound:
            self.is_interval_valid = True
        elif ((self.is_lower_bound_inclusive == False) and (self.is_upper_bound_inclusive == False)) and (self.lower_bound<((self.upper_bound)-1)):
            self.is_interval_valid = True
        elif self.is_interval_valid == False:
            raise MyError("Order of the numbers in the interval not correct")  #This error is raised when the format of the interval string is valid, but it is not a valid interval. For example if the lower bound is bigger than the upper bound


    def __str__(self):  # This function is used to print a valid representation of the interval.
        if self.is_interval_valid == True:
            string = ''
            if self.is_lower_bound_inclusive == True:
                string += '['
            if self.is_lower_bound_inclusive == False:
                string += '('
            string += str(self.lower_bound)
            string += ','
            string +=str(self.upper_bound)
            if self.is_upper_bound_inclusive == True:
                string += ']'
            if self.is_upper_bound_inclusive == False:
                string += ')'
        return string



#The next function takes to intervals and merge them if they overlap or are adjacent. If they are merged, the resulting interval will be a valid interval with inclusive bounds.

#What it does in order to verify that two intervals are mergable, is to create a list with all the numbers of both intervals. If this list has spaces in between that are greater
#than 1 or 0 (is a list of non-consecutive numbers), then the intervals are not mergable and an error is raised.




    @staticmethod
    def mergeIntervals(int1, int2):
        """ mergeIntervals(int1, int2) that takes two intervals. If the intervals overlap or are adjacent, returns a merged interval.
      It is important to clarify that all merged intervals will be valid inclusive bounds intervals."""

        if isinstance(int1, interval) and isinstance(int2, interval):
            interval1 = range(int1.real_lower_bound, int1.real_upper_bound+1)
            interval2 = range(int2.real_lower_bound, int2.real_upper_bound+1)
            merged_list = interval1 + interval2
            merged_list = sorted(merged_list)
            if (max(merged_list)-min(merged_list)+1) > len(merged_list):
                 raise MyError("Intervals are not Mergable. Check that they are at least, adjacent")  #This error is raised if the intervals are not mergable
            else:
                new_interval_string = '[' + str(min(merged_list)) + ',' + str(max(merged_list)) + ']'
                return interval(new_interval_string)
        else:
            raise MyError("At least one of the intervals is not of the class intervals") #This error is raised if the input of the method are not two intervals

    @staticmethod
    def mergeOverlapping(intervals): # This function takes s list of intervals and merge them if they overlap or are adjacent
        """ mergeOverlapping(intervals) that takes a list of intervals and merges all overlapping and adjacent intervals
            (I assume that the homework required adjacent intervals as well like in the previous point). It uses the mergeIntervals method"""

        if isinstance(intervals, list) <> True:
            raise MyError("The object is not a list, please introduce a list of intervals") # This error if the input is not a list
        for a in intervals:
            if isinstance(a, interval) == False:
                ind = intervals.index(a)
                raise MyError("Please check, element " + str(ind) + " of the list is not an interval") #This error is raised if at least one element of the list is not an interval


        original_length = len(intervals)
        current_length = len(intervals) -1

        while current_length < original_length:
            original_length = len(intervals)
            for i in range(len(intervals)):
                for n in range(i+1, len(intervals)):
                    try:
                        merged = interval.mergeIntervals(intervals[i], intervals[n])
                        intervals.append(merged)
                        intervals.remove(intervals[i])
                        intervals.remove(intervals[n-1])
                        break
                    except:
                        continue
            current_length = len(intervals)
        return intervals


    @staticmethod
    def insert(intervals, newint): # This function takes s list of intervals and a new interval and after trying to merge, return a list of intervals.
        """ insert(intervals, newint) that takes two arguments: a list of non-overlapping intervals; and a single interval and try to insert this interval intro the rest.
        It uses the previous methods."""

        if isinstance(intervals, list) <> True:
            raise MyError("The object is not a list, please introduce a list of non-overlapping intervals") #This error is raised if the first input is not a list
        if interval.mergeOverlapping(intervals) <> intervals:
            raise MyError("The list of intervals introduced is not a list of non-overlapping intervals")  #This error is raised if the list of intervals contain mergable intervals
        if isinstance(newint, interval) <> True:
            raise MyError("The object you want to insert is not an interval") #This error is raised if the second input is not an interval
        else:
            new_list = intervals
            new_list.append(newint)
            new_list = interval.mergeOverlapping(new_list)
            new_list.sort(key=lambda x: x.real_lower_bound, reverse=False)
        return new_list

