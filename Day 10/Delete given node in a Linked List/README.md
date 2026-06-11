# Day 10 - Delete Given Node in a Linked List

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

This problem gives direct access to a node that needs to be deleted from a singly linked list. The catch is that we are not given the head of the list, so we can't traverse to the previous node in the usual way. The goal is to delete the given node while keeping the list valid.

---

## 🤔 My First Thought

My first instinct was to find the previous node and update its next pointer.

Then I realized we aren't given the head at all 😅

For a few minutes I kept thinking in the normal linked list deletion mindset before noticing the constraint was actually the whole point of the problem.

---

## 🐢 Brute Force Approach

### Idea

If we had access to the head, we could traverse the linked list, find the node before the target node, and skip the target node by updating pointers.

However, this approach is not possible under the given constraints because the head is not available.

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

We cannot remove the current node directly because we don't know its previous node. Instead, we copy the value of the next node into the current node and bypass the next node. The given node effectively becomes the next node, making the deletion possible in constant time.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(1)  |
| Space Complexity | O(1)  |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Linked List Pointer Manipulation**

This problem is a classic example of thinking differently about linked lists. Instead of deleting the given node itself, we modify its contents and links to make it behave as if it was removed. The trick works because the node is guaranteed not to be the tail node.

---

## 💡 What I Learned

* Sometimes the constraint itself contains the solution clue.
* If the previous node isn't available, think about modifying the current node instead.
* This trick only works when the given node is not the last node.

---

## 🔍 Complexity Comparison

| Approach    | Time | Space |
| ----------- | ---- | ----- |
| Brute Force | O(N) | O(1)  |
| Better      | —    | —     |
| Optimal     | O(1) | O(1)  |

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

Whenever a linked list problem says "you are only given the node to delete" and "the node is not the tail", pause immediately.

Those two lines are the biggest hint. Think about changing the node itself instead of trying to reach its previous node.

---

## 🔗 Challenge Progress

Day 10 / 45 ✅

#SDESheetChallenge
#takeUforward
