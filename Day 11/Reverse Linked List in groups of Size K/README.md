# Day 11 - Reverse Linked List in Groups of Size K

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to reverse nodes of a linked list in groups of size `k`. If the remaining nodes are fewer than `k`, they should stay in their original order. The challenge is to reverse only the links, not the node values.

---

## 🤔 My First Thought

At first, I thought of extracting nodes into an array, reversing every group there, and rebuilding the linked list.

It felt straightforward because group reversal is easier to visualize in an array. But rebuilding the list felt unnecessary, and I knew there had to be a cleaner linked-list-only solution.

---

## 🐢 Brute Force Approach

### Idea

Store all node values in an array, reverse every valid group of size `k`, and then create the linked list again using the modified order.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

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

Instead of using extra space, reverse each valid group directly inside the linked list. Find the k-th node, reverse that segment, reconnect it, and continue with the next group.

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

**Linked List Reversal**

This problem is an extension of the classic linked list reversal pattern. The main challenge is handling reversal in fixed-size chunks while maintaining proper connections between groups.

---

## 💡 What I Learned

* Reversing a linked list segment becomes much easier when isolated first.
* Dummy nodes save a lot of headache when reconnecting groups.
* Always check if `k` nodes exist before attempting a reversal.

---

## 🔍 Complexity Comparison

| Approach    | Time | Space |
| ----------- | ---- | ----- |
| Brute Force | O(N) | O(N)  |
| Better      | —    | —     |
| Optimal     | O(N) | O(1)  |

---

## 📂 Files

```text
Day-11/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever a linked list problem mentions reversing nodes in chunks, groups, or blocks, think about segment-based reversal.

A strong hint is when the problem explicitly says "do not modify node values" — that's usually pushing you toward pointer manipulation.

---

## 🔗 Challenge Progress

Day 11 / 45 ✅

#SDESheetChallenge
#takeUforward
