# Day 6 - Grid Unique Paths

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find how many different ways exist to move from the top-left corner of a grid to the bottom-right corner. The only allowed moves are right and down, so the challenge is counting all valid paths without missing any combinations.

---

## 🤔 My First Thought

My first instinct was to try every possible path using recursion.

It felt natural because from any cell I only had two choices: move right or move down.

But after drawing a few grids, I noticed I was solving the same positions again and again.

---

## 🐢 Brute Force Approach

### Idea

Use recursion to explore every possible path from the current cell.

At each position, try moving right and down until the destination is reached. Count all valid paths and return the total.

### Complexity

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(2^(m+n)) |
| Space Complexity | O(m+n)     |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

### Idea

Use memoization to store answers for already solved cells.

If a cell's path count has been calculated before, reuse it instead of solving the same subproblem again.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(m × n) |
| Space Complexity | O(m × n) |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

To calculate paths for a cell, we only need values from the current row and the previous row. There is no need to store the entire DP table.

Using two 1D arrays (or even one), we can reduce the space significantly while keeping the same time complexity.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(m × n) |
| Space Complexity | O(n)     |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Dynamic Programming (DP on Grids)**

The problem contains overlapping subproblems because the number of paths to a cell gets calculated multiple times through different routes.

DP helps store those results and reuse them, turning an exponential solution into a polynomial one.

---

## 💡 What I Learned

* If recursion revisits the same grid cells repeatedly, DP is probably hiding somewhere.
* In grid problems, always think about what information is needed from neighboring cells.
* Space optimization usually comes after understanding the DP transition clearly.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space    |
| ----------- | ---------- | -------- |
| Brute Force | O(2^(m+n)) | O(m+n)   |
| Better      | O(m × n)   | O(m × n) |
| Optimal     | O(m × n)   | O(n)     |

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

Whenever you see a grid and the question asks for the number of ways, paths, or minimum/maximum values, think about Dynamic Programming.

A useful hint is to ask: "Can the answer for this cell be built using answers from neighboring cells?"

---

## 🔗 Challenge Progress

Day 6 / 45 ✅

#SDESheetChallenge
#takeUforward
