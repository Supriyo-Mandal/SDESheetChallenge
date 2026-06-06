# Day 3 - Merge Overlapping Sub-intervals

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

Given a list of intervals, the goal is to merge all intervals that overlap and return only the final non-overlapping intervals. The challenge is identifying overlaps efficiently and combining them without unnecessary comparisons.

---

## 🤔 My First Thought

My first instinct was to compare every interval with the intervals that come after it and merge whenever I found an overlap.

It felt straightforward because I could directly check all possibilities and wouldn't miss any merge. But it also felt like I was doing a lot of repeated checking.

---

## 🐢 Brute Force Approach

### Idea

Sort the intervals first. For every interval, keep checking the following intervals and keep extending the current interval as long as overlaps exist. Once a non-overlapping interval is found, start the process again.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N²) |
| Space Complexity | O(N)  |

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

After sorting, all overlapping intervals naturally appear next to each other. Instead of checking every future interval repeatedly, we only need to compare the current interval with the last merged interval.

### Complexity

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(N log N) |
| Space Complexity | O(N)       |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Sorting + Greedy (Interval Merging)**

Sorting brings overlapping intervals together. Once sorted, a greedy decision works because merging the current interval with the last valid merged interval is always sufficient to maintain the correct answer.

---

## 💡 What I Learned

* If intervals are involved, sorting is usually the first thing worth considering.
* I almost overcomplicated overlap detection before realizing adjacent intervals after sorting are enough.
* Remembering the "last merged interval" removes a lot of unnecessary comparisons.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space |
| ----------- | ---------- | ----- |
| Brute Force | O(N²)      | O(N)  |
| Better      | —          | —     |
| Optimal     | O(N log N) | O(N)  |

---

## 📂 Files

```text
Day-3/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **intervals**, **merge ranges**, **overlapping segments**, and **calendar scheduling** should immediately make you think about sorting first.

A useful interview hint: if intervals can overlap, ask yourself whether sorting by start time makes the relationships easier to process.

---

## 🔗 Challenge Progress

Day 3 / 45 ✅

#SDESheetChallenge
#takeUforward
