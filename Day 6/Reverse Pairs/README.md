# Day 6 - Reverse Pairs

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

This problem asks us to count pairs of indices where the left element is more than twice the right element, while maintaining the order of indices.

At first it looks like a simple pair-counting problem, but the large constraints make the naive approach too slow.

---

## 🤔 My First Thought

My first instinct was to generate every possible pair and check the condition directly.

It felt safe because the logic is easy to verify. But seeing the input size, I knew an O(N²) solution wouldn't be enough.

---

## 🐢 Brute Force Approach

### Idea

Use two nested loops to generate all valid pairs `(i, j)` where `i < j`.

For every pair, check whether `nums[i] > 2 * nums[j]`. If the condition is true, increment the answer count.

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

The condition involves pairs across different parts of the array. While studying it, I noticed it feels very similar to the Inversion Count problem.

Using Merge Sort, both halves remain sorted, which allows us to efficiently count valid reverse pairs before merging them back together.

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

**Divide and Conquer (Merge Sort)**

The sorted halves created during Merge Sort make it possible to count reverse pairs without checking every combination individually.

Instead of comparing all pairs, we use the ordering property of sorted subarrays to count many pairs at once.

---

## 💡 What I Learned

* Reverse Pairs is very closely related to Inversion Count.
* If a pair-counting problem asks for index order and large constraints, Merge Sort is worth considering.
* The counting logic happens before merging, not during the usual merge comparison.

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
Day-6/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever you see phrases like **count pairs**, **i < j**, **array relationships**, or constraints that rule out O(N²), think about Merge Sort-based counting.

If the problem feels similar to Inversion Count but with a modified condition, there's a good chance the same Divide and Conquer idea can be adapted.

---

## 🔗 Challenge Progress

Day 6 / 45 ✅

#SDESheetChallenge
#takeUforward
