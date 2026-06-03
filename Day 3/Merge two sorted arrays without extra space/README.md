# Day 3 - Merge Two Sorted Arrays Without Extra Space

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

This problem asks us to merge two already sorted arrays into one sorted array. The catch is that we need to do it in-place by using the extra space available at the end of `nums1` instead of creating a new array.

---

## 🤔 My First Thought

My first thought was to use the merge step from Merge Sort and create a separate array.

It felt like the most straightforward solution since both arrays were already sorted. Then I noticed the in-place requirement and knew I had to find a way to avoid extra space.

---

## 🐢 Brute Force Approach

### Idea

Create a new array and merge both sorted arrays into it using two pointers. Once merged, copy the result back into `nums1`.

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

No meaningful intermediate optimization for this problem.

---

## 🚀 Optimal Approach

### Key Observation

Since both arrays are sorted, the largest elements will always be towards the end. Filling `nums1` from the back prevents overwriting useful values and eliminates the need for extra space.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(m + n) |
| Space Complexity | O(1)     |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Two Pointers**

This problem uses two pointers starting from the ends of both arrays. By comparing the largest remaining elements and placing them at the end of `nums1`, we can complete the merge in a single pass without extra memory.

---

## 💡 What I Learned

* The phrase "in-place merge" is a strong hint that extra arrays should be avoided.
* Sometimes processing from the end is much simpler than processing from the beginning.
* If one array has unused space at the back, it's usually there for a reason.

---

## 🔍 Complexity Comparison

| Approach    | Time     | Space    |
| ----------- | -------- | -------- |
| Brute Force | O(m + n) | O(m + n) |
| Better      | —        | —        |
| Optimal     | O(m + n) | O(1)     |

---

## 📂 Files

```text
Day-3/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Look for keywords like **sorted arrays**, **merge**, and **in-place**.

If one array already has extra space available, try thinking from the back instead of the front. That hint usually leads to the optimal two-pointer solution.

---

## 🔗 Challenge Progress

Day 3 / 45 ✅

#SDESheetChallenge
#takeUforward
