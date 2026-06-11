# Day 9 - Reverse a Linked List

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to reverse a singly linked list and return the new head of the reversed list. The challenge is to change the order of the nodes without losing track of the connections between them.

---

## 🤔 My First Thought

My first instinct was to use extra space and store all node values somewhere.
A stack felt like the easiest way because it naturally gives elements back in reverse order.
It worked, but I knew using extra memory for such a common linked list problem probably wasn't the best answer.

---

## 🐢 Brute Force Approach

### Idea

Traverse the linked list and push all node values into a stack. Then traverse the list again and replace each node's value by popping from the stack. This reverses the values stored in the nodes without changing the actual links.

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

No meaningful intermediate optimization for this problem.

---

## 🚀 Optimal Approach

### Key Observation

Instead of reversing the values, reverse the links themselves. While traversing the list, keep track of the previous, current, and next nodes so the connections can be flipped safely without losing access to the remaining list.

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

**Linked List Pointer Manipulation**

This problem is all about carefully updating pointers. By maintaining references to the previous and next nodes, we can reverse the direction of every link in a single traversal without using extra space.

---

## 💡 What I Learned

* Reversing node values and reversing node links are two very different things.
* Forgetting to store the next node before changing pointers can break the entire list.
* If an interview asks for an in-place reversal, extra data structures are usually a hint that there's a better solution.

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
Day-9/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever you see keywords like **reverse linked list**, **in-place modification**, or **change node connections**, think about pointer manipulation.

A useful interview hint is to ask yourself: *Can I solve this by changing links instead of moving data?* That question usually leads to the optimal solution faster.

---

## 🔗 Challenge Progress

Day 9 / 45 ✅

#SDESheetChallenge
#takeUforward

---
