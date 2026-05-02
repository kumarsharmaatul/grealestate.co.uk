# grealestate.co.uk
Qutions - Group Anagrams, Longest Substring Without Repeating Characters, Merge Intervals

# 2G Real Estate - Technical Screening Solutions

This repository contains my solutions to the technical screening test for the Software Engineer position. Each solution is implemented in Python with optimized time and space complexity.

## 🚀 Problem Solutions

### 1. Group Anagrams
- **File:** `group_anagrams.py`
- **Approach:** Used a Hash Map (dictionary) where the key is a sorted tuple of characters. This ensures that all anagrams share the same key.
- **Time Complexity:** $O(N \cdot K \log K)$ where $N$ is the number of strings and $K$ is the max length of a string.
- **Space Complexity:** $O(N \cdot K)$ to store the grouped strings.

### 2. Longest Substring Without Repeating Characters
- **File:** `long_sub_without_rep_charc.py`
- **Approach:** Implemented the Sliding Window technique with a hash map to track the last seen index of each character, allowing for a single-pass solution.
- **Time Complexity:** $O(N)$ where $N$ is the length of the string.
- **Space Complexity:** $O(M)$ where $M$ is the size of the character set.

### 3. Merge Intervals
- **File:** `merge_intervals.py`
- **Approach:** Sorted the intervals by their start times and then iterated through them to merge any overlapping segments into a single interval.
- **Time Complexity:** $O(N \log N)$ due to sorting.
- **Space Complexity:** $O(N)$ for storing the merged output.

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kumarsharmaatul/grealestate.co.uk.git](https://github.com/kumarsharmaatul/grealestate.co.uk.git)

   cd grealestate.co.uk


   3. **Run the individual scripts:**
   ```bash
   # Execute Group Anagrams
   python3 group_anagrams.py

   # Execute Longest Substring solution
   python3 long_sub_without_rep_charc.py

   # Execute Merge Intervals
   python3 merge_intervals.py