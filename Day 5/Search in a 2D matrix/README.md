# Day 5 - Search in a Sorted 2D Matrix

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

We are given a matrix where every row is sorted, and each row starts with a value greater than the last value of the previous row. The task is to determine whether a target value exists in the matrix.

---

## 🤔 My First Thought

My first instinct was to just scan every element one by one.

It felt straightforward because the matrix size isn't huge, and I'd definitely find the target if it existed. But after looking at the sorting conditions more carefully, it felt wasteful to ignore all that structure.

---

## 🐢 Brute Force Approach

### Idea

Traverse every row and every column in the matrix.

Compare each element with the target and return `True` as soon as a match is found.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(N × M) |
| Space Complexity | O(1)     |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

### Idea

Instead of searching every element, first identify the row that could contain the target.

If the target lies between the first and last element of a row, perform binary search only on that row.

### Complexity

| Metric           | Value        |
| ---------------- | ------------ |
| Time Complexity  | O(N × log M) |
| Space Complexity | O(1)         |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

The entire matrix behaves like one sorted 1D array.

Without actually flattening the matrix, we can perform binary search on indices and convert each virtual index back into row and column positions.

### Complexity

| Metric           | Value         |
| ---------------- | ------------- |
| Time Complexity  | O(log(N × M)) |
| Space Complexity | O(1)          |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

### Binary Search

The biggest clue was that the matrix is globally sorted, not just row-wise sorted.

Whenever a problem guarantees sorted order and asks for efficient searching, binary search should immediately come to mind. Here we simply extend the idea to a virtual 1D array.

---

## 💡 What I Learned

* The condition between rows is more important than the row sorting itself.
* I almost treated this like a normal matrix search problem and missed the global ordering clue.
* Flattening conceptually is useful even when we don't physically create a new array.

---

## 🔍 Complexity Comparison

| Approach    | Time          | Space |
| ----------- | ------------- | ----- |
| Brute Force | O(N × M)      | O(1)  |
| Better      | O(N × log M)  | O(1)  |
| Optimal     | O(log(N × M)) | O(1)  |

---

## 📂 Files

```text
Day-5/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever you see phrases like "rows sorted", "global ordering", or "search in a sorted matrix", pause and check if the matrix can be treated as a sorted 1D array.

If the matrix behaves like one continuous sorted sequence, a virtual binary search is usually the fastest solution.

---

## 🔗 Challenge Progress

Day 5 / 45 ✅

#SDESheetChallenge
#takeUforward

---
