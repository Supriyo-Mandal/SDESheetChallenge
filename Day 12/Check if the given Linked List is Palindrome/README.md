# Day 11 - Detect a Cycle in a Linked List

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to determine whether a linked list contains a loop. Instead of reaching a `null` node at the end, some linked lists may point back to a previous node, creating a cycle. The goal is to return whether such a cycle exists.

---

## 🤔 My First Thought

My first instinct was to keep track of every node I visited. If I ever reached the same node again, that would clearly mean I was stuck in a loop.

It felt straightforward because I didn't need to think about pointer tricks initially—just remember what I'd already seen.

---

## 🐢 Brute Force Approach

### Idea

Traverse the linked list and store every visited node in a hash set or map.

If a node appears again during traversal, a cycle exists. If we reach `null`, the list is cycle-free.

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

### Idea

Use a hash set instead of a map to store visited node references.

Lookup becomes faster while the overall idea remains the same—check whether the current node has already been visited.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

If a cycle exists, a fast-moving pointer will eventually catch a slow-moving pointer inside the loop.

By moving one pointer one step and another pointer two steps at a time, we can detect a cycle without storing any nodes.

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

**Two Pointers (Tortoise and Hare Algorithm)**

This pattern works because two pointers moving at different speeds must eventually meet if a loop exists. If there's no cycle, the faster pointer simply reaches the end of the list.

It's one of those classic linked list patterns that saves space while keeping the solution efficient.

---

## 💡 What I Learned

* The clue was realizing we need to detect repeated nodes, not repeated values.
* It's easy to mistakenly compare node values instead of node references.
* Floyd's Cycle Detection is a pattern worth remembering because it shows up often in linked list interviews.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space |
| ----------- | ---------- | ----- |
| Brute Force | O(N log N) | O(N)  |
| Better      | O(N)       | O(N)  |
| Optimal     | O(N)       | O(1)  |

---

## 📂 Files

```text
Day-11/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever a linked list problem mentions **cycle**, **loop**, **revisiting nodes**, or asks for **constant extra space**, think about the Two Pointers pattern.

A strong interview hint is: "Can you solve it without storing visited nodes?" That's usually a signal toward Floyd's Cycle Detection.

---

## 🔗 Challenge Progress

Day 11 / 45 ✅

#SDESheetChallenge
#takeUforward

---
