# Day 4 - Count Inversions in an Array

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to count how many inversion pairs exist in an array. An inversion occurs when a larger element appears before a smaller element. The inversion count helps measure how far an array is from being sorted.

---

## 🤔 My First Thought

My first instinct was to check every possible pair and count whenever the left element was greater than the right one.

It felt straightforward because the inversion definition itself is based on pairs. It worked immediately, but I knew it wouldn't survive larger inputs.

---

## 🐢 Brute Force Approach

### Idea

Check every pair `(i, j)` where `i < j`.

If `nums[i] > nums[j]`, increase the inversion count.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N²) |
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

While merging two sorted halves in Merge Sort, if an element from the right half is smaller than an element from the left half, then all remaining elements in the left half will also form inversions with it.

This allows counting multiple inversions at once instead of checking every pair.

### Complexity

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(N log N) |
| Space Complexity | O(N)       |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Merge Sort**

This problem hides the inversion counting inside the merge step of Merge Sort.

Since both halves are already sorted, we can efficiently count how many elements remain on the left whenever we pick a smaller element from the right half.

---

## 💡 What I Learned

* If a problem asks for counting pair relationships efficiently, Merge Sort is worth considering.
* The real trick is not sorting the array, but using the merge step to gather information.
* I initially focused too much on the inversion definition and ignored the constraints.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space |
| ----------- | ---------- | ----- |
| Brute Force | O(N²)      | O(1)  |
| Better      | —          | —     |
| Optimal     | O(N log N) | O(N)  |

---

## 📂 Files

```text
Day-4/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **count pairs**, **inversions**, **reverse pairs**, or **pair relationships with constraints** should immediately make me think beyond nested loops.

If the problem involves counting while maintaining sorted order, there's a good chance Merge Sort can be used to optimize it.

---

## 🔗 Challenge Progress

Day 4 / 45 ✅

#SDESheetChallenge
#takeUforward

---
