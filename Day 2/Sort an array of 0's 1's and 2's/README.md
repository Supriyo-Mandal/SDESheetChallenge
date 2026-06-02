# Day 2 - Sort an Array of 0s, 1s and 2s

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

This problem gives an array containing only 0s, 1s, and 2s and asks us to sort it in-place.

The interesting part is that the array contains only three distinct values, which opens the door for solutions better than general-purpose sorting.

---

## 🤔 My First Thought

My first instinct was to simply count how many 0s, 1s, and 2s are present.

Once I know the counts, I can overwrite the array with those values in order. It felt straightforward because the range of values is fixed and very small.

---

## 🐢 Brute Force Approach

### Idea

Count the frequency of 0s, 1s, and 2s in the array. Then overwrite the original array by placing all 0s first, followed by 1s, and then 2s.

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

### Idea

Use the same counting observation but rewrite the array using index ranges instead of separate filling loops. It slightly improves implementation clarity while keeping the same complexity.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(1)  |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

Since there are only three possible values, we can maintain three regions in the array:

* Left side for 0s
* Middle for 1s
* Right side for 2s

By moving elements into their correct regions during a single traversal, the array gets sorted in-place without counting.

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

**Three Pointers (Dutch National Flag Algorithm)**

The array is partitioned into three sections using `low`, `mid`, and `high` pointers. Each element is placed directly into its correct region while scanning the array once.

This pattern is useful whenever an array contains a small fixed number of categories that need to be grouped efficiently.

---

## 💡 What I Learned

* Seeing only `0, 1, 2` is a big clue that a specialized solution may exist.
* When swapping with the `high` pointer, I shouldn't move `mid` immediately.
* "Sort in-place" is often a hint that interviewers want the Dutch National Flag approach.

---

## 🔍 Complexity Comparison

| Approach    | Time | Space |
| ----------- | ---- | ----- |
| Brute Force | O(N) | O(1)  |
| Better      | O(N) | O(1)  |
| Optimal     | O(N) | O(1)  |

---

## 📂 Files

```text
Day-2/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **0s, 1s, 2s**, **three categories**, **in-place sorting**, or **single traversal** should immediately make me think about the Dutch National Flag Algorithm.

If the array contains only a few distinct values and extra space is restricted, a pointer-based partitioning solution is usually worth considering.

---

## 🔗 Challenge Progress

Day 2 / 45 ✅

#SDESheetChallenge
#takeUforward
