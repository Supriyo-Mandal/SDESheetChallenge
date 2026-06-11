# Day 7 - 4 Sum

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find all unique groups of four numbers whose sum equals a given target value. The tricky part is avoiding duplicate quadruplets while making sure all valid combinations are included.

---

## 🤔 My First Thought

My first instinct was to generate every possible group of four numbers and check their sum.

It felt like the safest way because it guarantees we won't miss any valid quadruplet. But looking at the number of nested loops, it was obvious this wouldn't scale well.

---

## 🐢 Brute Force Approach

### Idea

Use four nested loops to generate every possible quadruplet.

For each combination, check if the sum equals the target. Store valid quadruplets in a set after sorting them to avoid duplicates.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N⁴) |
| Space Complexity | O(K)  |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

### Idea

Fix the first two numbers using nested loops.

For the remaining part of the array, use a hash set to find the fourth required number while iterating for the third number. Store valid quadruplets in a set to avoid duplicates.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(N³)    |
| Space Complexity | O(N + K) |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

After sorting the array, fixing two numbers reduces the problem to finding a pair with a specific sum. A two-pointer approach can efficiently search the remaining elements while naturally handling duplicates.

### Complexity

| Metric           | Value                     |
| ---------------- | ------------------------- |
| Time Complexity  | O(N³)                     |
| Space Complexity | O(1) *(excluding output)* |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Two Pointers + Sorting**

Sorting the array creates an ordered structure that allows us to move pointers intelligently instead of checking every combination. Once two numbers are fixed, the remaining search behaves like a classic two-sum problem.

---

## 💡 What I Learned

* Whenever a problem asks for unique triplets or quadruplets, sorting is usually a strong clue.
* Forgetting to skip duplicates can easily create repeated answers.
* Reducing a 4-sum problem into a smaller 2-sum search makes the solution much cleaner.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space    |
| ----------- | ----- | -------- |
| Brute Force | O(N⁴) | O(K)     |
| Better      | O(N³) | O(N + K) |
| Optimal     | O(N³) | O(1)*    |

* Excluding output storage.

---

## 📂 Files

```text
Day-7/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **unique quadruplets**, **target sum**, **avoid duplicates**, or **k-sum problems** should immediately make me think about sorting and two pointers.

If the brute-force solution involves multiple nested loops, check whether fixing a few elements can reduce the remaining problem into a simpler sum-search pattern.

---

## 🔗 Challenge Progress

Day 7 / 45 ✅

#SDESheetChallenge
#takeUforward
