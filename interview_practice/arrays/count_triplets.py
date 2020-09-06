#code
# https://practice.geeksforgeeks.org/problems/count-the-triplets/0
# to count triplets

import sys
from typing import List

from numpy import sort, searchsorted

from interview_practice.utils import TextFileOrStdInOut
from interview_practice.utils import read_integer_from_text_file
from interview_practice.utils import read_integer_list_from_text_file


def count_triplets_from_array(arr: List[int], N: int):
    # two ways we can do this
    # 1. N choose 2 combination --> check if the sum is in the list
    # 2. for each item in the list --> check if two other items can be summed up to get it
    # we assume the array will contain both positive and negative numbers
    
    sorted_arr = sort(arr, kind="quicksort")
    count = 0
    for i in range(0, N-2):
        # i and i+1 can be -/-, -/+ or +/+
        possible_max_sum = sorted_arr[i] + sorted_arr[N-1]
        possible_min_sum = sorted_arr[i] + sorted_arr[i + 1]
        start_idx = searchsorted(sorted_arr, possible_min_sum, side="left")
        end_idx = searchsorted(sorted_arr, possible_max_sum, side="right")
        for j in range(i + 1, N-1):
            sum = sorted_arr[i] + sorted_arr[j]
            if sum > sorted_arr[N-1]:
                continue
                start = sorted_arr[j+1]
            idx = searchsorted(sorted_arr, sum, side="right") - 1
            if (idx >= N):
                continue
            if sum == sorted_arr[idx]:
                count = count + 1
    return count


def count_triplets(filename: str):
    with TextFileOrStdInOut (filename, "rt") as f:
        T = read_integer_from_text_file(f)
        for t in range(1, T+1):
            N = read_integer_from_text_file(f)
            count = count_triplets_from_array(read_integer_list_from_text_file(f), N)
            yield count if count > 0 else -1

if __name__ == "__main__":
    args = sys.argv
    input_file_name = args[1] if len(args) >= 2 else None
    output_file_name = args[2] if len(args) >= 3 else None
    with TextFileOrStdInOut (output_file_name, "wt") as f:
        for output in count_triplets(input_file_name):
            print (output, file=f)