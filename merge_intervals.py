''' 
3. Merge Intervals
Problem:
Given a list of intervals, merge all overlapping intervals. For example:
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]


Solution:
First, I sort the intervals based on their start values.
Then, I iterate through the sorted intervals and add them to a merged list.
If the current interval's start time is less than or equal to the end time of the last interval in the merged list, 
an overlap exists, and I update the end time of the last interval. 
Otherwise, I append the current interval as a new distinct interval.
'''

def mergeIntervals(intervals):
    if not intervals:
        return []
        
    # Sort intervals based on the starting value
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check for overlap
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
            
    return merged

# Test
print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))