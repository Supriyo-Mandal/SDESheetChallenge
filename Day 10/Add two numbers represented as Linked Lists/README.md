# Day 10 - Add Two Numbers Represented as Linked Lists

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

Two numbers are represented using linked lists where each node stores a single digit in reverse order. The task is to add these numbers and return the result as a new linked list in the same format.

---

## 🤔 My First Thought

My first instinct was to convert both linked lists into actual numbers, add them, and then build a new linked list from the result.

It felt straightforward at first, but I quickly realized it could run into issues with very large numbers and wasn't really using the linked list structure effectively.

---

## 🐢 Brute Force Approach

### Idea

Traverse both linked lists, convert them into numbers, add them together, and then create a new linked list from the resulting sum.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(m + n) |
| Space Complexity | O(m + n) |

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

The digits are already stored in reverse order, which means we can directly simulate elementary school addition from left to right in the linked list. We only need to keep track of the carry while traversing both lists.

### Complexity

| Metric           | Value        |
| ---------------- | ------------ |
| Time Complexity  | O(max(m, n)) |
| Space Complexity | O(max(m, n)) |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Linked List Traversal + Carry Simulation**

This problem is less about complex linked list manipulation and more about processing two linked lists simultaneously. The carry value behaves exactly like normal digit-by-digit addition, making the solution clean and intuitive once that connection clicks.

---

## 💡 What I Learned

* The reverse-order storage of digits is actually a hint, not a complication.
* It's easy to forget the final carry after both lists end.
* A dummy node makes building the result list much simpler.

---

## 🔍 Complexity Comparison

| Approach    | Time         | Space        |
| ----------- | ------------ | ------------ |
| Brute Force | O(m + n)     | O(m + n)     |
| Better      | —            | —            |
| Optimal     | O(max(m, n)) | O(max(m, n)) |

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

If a linked list stores digits of a number, don't rush to convert it into an integer.

Look at how the digits are arranged first. If they're already in reverse order, think about simulating addition directly with a carry variable.

---

## 🔗 Challenge Progress

Day 10 / 45 ✅

#SDESheetChallenge
#takeUforward

---
