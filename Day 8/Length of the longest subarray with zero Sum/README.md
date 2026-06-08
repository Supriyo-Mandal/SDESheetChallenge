# Day 8 - Longest Subarray with Zero Sum

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find the length of the longest contiguous subarray whose total sum becomes zero. The array can contain both positive and negative numbers, which makes simple observations a bit tricky. The goal is to return only the maximum length.

---

## 🤔 My First Thought

My first instinct was to generate every possible subarray and calculate its sum.

It felt like the safest way because I'd definitely find all zero-sum subarrays and then just keep track of the longest one.

Not efficient, but it was the first thing that came to mind.

---

## 🐢 Brute Force Approach

### Idea

Start from every index and keep extending the subarray while maintaining its sum.

Whenever the running sum becomes zero, update the maximum length found so far.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N²) |
| Space Complexity | O(1)  |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

No meaningful intermediate optimization for this problem.

---

## 🚀 Optimal Approach

### Key Observation

If the same prefix sum appears again at a later index, the elements between those two indices must sum to zero.

By storing the first occurrence of every prefix sum in a hash map, we can instantly calculate the length of a zero-sum subarray whenever that sum reappears.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Hashing + Prefix Sum**

The key idea is to track cumulative sums while traversing the array. If a prefix sum repeats, it means the subarray between those occurrences has a sum of zero.

Hashing helps store and retrieve prefix sums in constant time, making the solution linear.

---

## 💡 What I Learned

* Repeating prefix sums are a strong clue for zero-sum subarray problems.
* Storing the first occurrence of a prefix sum is important for getting the longest length.
* Whenever a problem involves subarray sums, prefix sums should be one of the first things I consider.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(1)  |
| Better      | —     | —     |
| Optimal     | O(N)  | O(N)  |

---

## 📂 Files

```text
Day-8/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **longest subarray**, **sum equals zero**, **positive and negative numbers**, and **subarray sum** should immediately make me think about prefix sums.

If the problem asks for a subarray property and the array contains negative numbers, a hash map with prefix sums is often the first thing worth trying.

---

## 🔗 Challenge Progress

Day 8 / 45 ✅

#SDESheetChallenge
#takeUforward
