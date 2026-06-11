# Day 11 - Find Intersection of Two Linked Lists

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find the exact node where two singly linked lists intersect. If the lists never meet, we return `null`.

The important detail is that intersection is based on node reference, not node value.

---

## 🤔 My First Thought

My first instinct was to compare every node of one list with every node of the other list.

It felt straightforward because eventually the common node should show up. At first, I was focusing on matching values, but then I realized two nodes can have the same value and still be completely different nodes.

---

## 🐢 Brute Force Approach

### Idea

Traverse the second linked list node by node.

For every node, scan the entire first linked list and check whether both pointers are pointing to the exact same node. The first match found is the intersection point.

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

Store all node references of the first linked list inside a hash set.

Then traverse the second linked list and check whether the current node already exists in the set. The first match gives the intersection node.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(N + M) |
| Space Complexity | O(N)     |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

Instead of calculating lengths manually, let both pointers traverse both lists.

When a pointer reaches the end of one list, redirect it to the head of the other list. This equalizes the distance traveled by both pointers, causing them to meet exactly at the intersection node (or both become `null` if no intersection exists).

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(N + M) |
| Space Complexity | O(1)     |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Two Pointers**

This problem becomes much cleaner once you stop thinking about values and start thinking about node references.

The two-pointer switching technique helps both pointers cover the same total distance without explicitly calculating lengths.

---

## 💡 What I Learned

* Intersection means same node address, not same node value.
* Hashing gives an easy O(N + M) solution but uses extra memory.
* The pointer-switching trick is one of those linked list patterns worth remembering for interviews.

---

## 🔍 Complexity Comparison

| Approach    | Time     | Space |
| ----------- | -------- | ----- |
| Brute Force | O(N × M) | O(1)  |
| Better      | O(N + M) | O(N)  |
| Optimal     | O(N + M) | O(1)  |

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

If the question mentions **two linked lists sharing nodes**, immediately think about comparing node references instead of values.

Keywords like *intersection point*, *common node*, *shared tail*, or *meeting point* should make you consider the two-pointer switching technique.

---

## 🔗 Challenge Progress

Day 11 / 45 ✅

#SDESheetChallenge
#takeUforward
