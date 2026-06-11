# Day 10 - Merge Two Sorted Linked Lists

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we are given two linked lists where the values are already sorted. The goal is to merge them into a single linked list while keeping the overall order sorted. Instead of creating a new sorted sequence from scratch, we need to combine the existing nodes efficiently.

---

## 🤔 My First Thought

My first instinct was to pull all values from both lists into an array, sort it, and then create a new linked list from the sorted values.

It felt straightforward because sorting is something I naturally reach for when I see two collections that need to be merged in order.

---

## 🐢 Brute Force Approach

### Idea

Store all nodes from both linked lists in an array, sort the array, and then build a new linked list using the sorted values.

### Complexity

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(N log N) |
| Space Complexity | O(N)       |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

```md
No meaningful intermediate optimization for this problem.
```

---

## 🚀 Optimal Approach

### Key Observation

Since both linked lists are already sorted, there is no need to sort again. We can compare the current nodes of both lists and always attach the smaller one to the merged list, just like the merge step of Merge Sort.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(N1+N2) |
| Space Complexity | O(1)     |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

### Linked List Pointer Manipulation

This problem is all about moving pointers carefully while maintaining sorted order. Instead of creating new nodes, we reuse existing nodes and connect them in the correct sequence.

The pattern appears frequently in linked list merge, partition, and reordering problems.

---

## 💡 What I Learned

* If the input lists are already sorted, sorting again is usually a red flag.
* A dummy node makes linked list construction much cleaner.
* The merge step from Merge Sort shows up surprisingly often in interviews.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space |
| ----------- | ---------- | ----- |
| Brute Force | O(N log N) | O(N)  |
| Better      | —          | —     |
| Optimal     | O(N1+N2)   | O(1)  |

---

## 📂 Files

```text
Day-10/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever you see phrases like "two sorted linked lists" or "merge sorted data", think about the merge step of Merge Sort.

A strong interview hint is that if the inputs are already sorted, the optimal solution often avoids sorting completely and uses pointers instead.

---

## 🔗 Challenge Progress

Day 10 / 45 ✅

#SDESheetChallenge
#takeUforward

---
