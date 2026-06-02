# Day 2 - Kadane's Algorithm

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

Given an array of integers, the goal is to find the contiguous subarray with the maximum possible sum.

Instead of checking every possible subarray, the challenge is to identify the maximum sum efficiently, even when the array contains negative numbers.

---

## 🤔 My First Thought

My first instinct was to generate every possible subarray and calculate its sum.

It felt like the safest way because I'd definitely cover all cases. The only issue was that the number of subarrays grows quickly, and recalculating sums again and again seemed wasteful.

---

## 🐢 Brute Force Approach

### Idea

Generate every possible subarray using a start and end index. For each subarray, calculate its sum from scratch and keep track of the maximum sum seen so far.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N³) |
| Space Complexity | O(1)  |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

### Idea

Instead of recalculating the sum for every subarray, keep a running sum while expanding the ending index. This avoids the third loop and reduces repeated work.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N²) |
| Space Complexity | O(1)  |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

A negative running sum will only hurt future subarrays. If the current sum becomes negative, it's better to start fresh from the next element.

This simple observation leads to Kadane's Algorithm, which finds the answer in a single pass.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Greedy + Dynamic Programming**

At every index, we decide whether to continue the current subarray or start a new one. The decision is made using information from the previous step, which gives it a DP flavor, while always choosing the locally best option makes it greedy.

---

## 💡 What I Learned

* A negative running sum is usually a sign to reset and start fresh.
* The phrase "maximum subarray" should immediately remind me of Kadane's Algorithm.
* It's easy to forget that the answer can be negative when all elements are negative.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N³) | O(1)  |
| Better      | O(N²) | O(1)  |
| Optimal     | O(N)  | O(1)  |

---

## 📂 Files

```text
Day-2/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **maximum subarray**, **largest contiguous sum**, or **best continuous segment** should make me think about Kadane's Algorithm.

If the interviewer asks for an O(N) solution and the problem involves a running sum, checking whether a negative contribution should be discarded is usually a strong hint.

---

## 🔗 Challenge Progress

Day 2 / 45 ✅

#SDESheetChallenge
#takeUforward
