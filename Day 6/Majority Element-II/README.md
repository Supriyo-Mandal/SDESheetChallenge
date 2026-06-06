# Day 6 - Majority Element-II

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find all elements that appear more than ⌊n/3⌋ times in an array. Unlike the majority element (> n/2), there can be at most two valid answers here. The goal is to return all such elements efficiently.

---

## 🤔 My First Thought

My first instinct was to count the frequency of every number and then check which ones cross the n/3 mark.

It felt straightforward because frequency-based problems usually become easy once counts are available. I wasn't thinking about the space constraint at first.

---

## 🐢 Brute Force Approach

### Idea

Pick each element and count how many times it appears by traversing the entire array again.

If its frequency is greater than n/3, add it to the answer list. Since there can be at most two valid elements, stop once two are found.

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

### Idea

Use a hashmap to store the frequency of every element while traversing the array.

After building the frequency map, check which elements occur more than n/3 times and add them to the result.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

If an element appears more than n/3 times, there can be at most two such elements in the entire array.

That observation allows us to track only two potential candidates and their counts instead of storing frequencies for every number. A final validation pass confirms the answer.

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

**Boyer-Moore Voting Algorithm**

This problem is an extension of the classic Majority Element problem. Instead of tracking one candidate, we track two possible candidates because there can be at most two elements occurring more than n/3 times.

The pattern works by canceling out different elements and keeping only the strongest candidates for verification later.

---

## 💡 What I Learned

* The "more than n/3 times" condition immediately limits the answer count to at most two elements.
* I almost forgot the final verification step after finding the candidates.
* Boyer-Moore is not just for n/2 majority problems; it can be extended to other frequency thresholds.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(1)  |
| Better      | O(N)  | O(N)  |
| Optimal     | O(N)  | O(1)  |

---

## 📂 Files

```text
Day-6/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever a problem says an element appears more than a fraction of the array size (n/2, n/3, etc.), think about candidate elimination techniques.

A good interview clue is: "Can we solve this without storing frequencies of every element?" That usually points toward Boyer-Moore Voting.

---

## 🔗 Challenge Progress

Day 6 / 45 ✅

#SDESheetChallenge
#takeUforward

---
