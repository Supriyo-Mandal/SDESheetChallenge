# Day 10 - Remove N-th Node From End of Linked List

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to remove the N-th node from the end of a linked list and return the updated list. The challenge is to handle edge cases correctly, especially when the node to be removed is the head itself.

---

## 🤔 My First Thought

My first instinct was to count the total number of nodes first.

Once I had the length, finding the target node felt simple because I could convert the position from the end into a position from the beginning.

It worked, but traversing the list twice felt unnecessary.

---

## 🐢 Brute Force Approach

### Idea

Traverse the linked list once to find its length.

Then calculate the position of the node from the start and traverse again to delete it by adjusting the links.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

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

Instead of calculating the length, maintain a gap of N nodes between two pointers.

When the fast pointer reaches the end, the slow pointer automatically reaches the node just before the one that needs to be removed.

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

### Two Pointers (Fast & Slow Pointer)

The problem becomes much cleaner when two pointers move with a fixed gap between them.

This allows us to locate the N-th node from the end in a single traversal without explicitly finding the length of the linked list.

---

## 💡 What I Learned

* Using a dummy node makes deleting the head node much easier.
* A fixed-gap fast and slow pointer setup can eliminate an entire traversal.
* Whenever I see "N-th node from the end", I should immediately think about two pointers.

---

## 🔍 Complexity Comparison

| Approach    | Time | Space |
| ----------- | ---- | ----- |
| Brute Force | O(N) | O(1)  |
| Better      | —    | —     |
| Optimal     | O(N) | O(1)  |

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

Keywords like **N-th node from end**, **single pass**, **one traversal**, and **linked list deletion** are strong hints toward the fast and slow pointer technique.

If the interviewer asks whether the solution can be done without calculating the length first, it's usually a signal to think about maintaining a fixed gap between two pointers.

---

## 🔗 Challenge Progress

Day 10 / 45 ✅

#SDESheetChallenge
#takeUforward
