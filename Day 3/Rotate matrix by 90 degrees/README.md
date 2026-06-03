# Day 3 - Rotate Matrix by 90 Degrees

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

Given an N × N matrix, the task is to rotate it 90 degrees clockwise without using extra space for another matrix.

The challenge isn't the rotation itself—it's doing it in-place while modifying the original matrix directly.

---

## 🤔 My First Thought

My first instinct was to create a new matrix and place every element in its rotated position.

It felt straightforward because I could directly map where each element should go. The only problem was that it used extra space, which the question specifically wanted to avoid.

---

## 🐢 Brute Force Approach

### Idea

Create a separate matrix of the same size.

For every element in the original matrix, calculate its new rotated position and place it there. Return the newly formed matrix.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N²) |
| Space Complexity | O(N²) |

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

A 90° clockwise rotation can be broken into two simple operations:

1. Transpose the matrix (rows become columns)
2. Reverse every row

Doing these operations in-place gives the required rotation without needing another matrix.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N²) |
| Space Complexity | O(1)  |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

**Matrix Manipulation / Transpose + Reverse**

This problem becomes much simpler once you stop thinking about moving every element individually.

The key is recognizing a matrix transformation pattern where a transpose followed by reversing each row produces a 90° clockwise rotation.

---

## 💡 What I Learned

* "In-place" is usually a strong hint that extra matrices shouldn't be used.
* Transpose is one of those matrix operations worth remembering for interviews.
* I almost started tracking individual element movements before noticing the simpler transformation.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(N²) |
| Better      | —     | —     |
| Optimal     | O(N²) | O(1)  |

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

Keywords like **rotate matrix**, **in-place**, **90 degree rotation**, and **square matrix** should immediately make me think about matrix transformations.

If an interviewer stresses "without extra space", check whether transpose, reverse, or swapping patterns can help before creating another matrix.

---

## 🔗 Challenge Progress

Day 3 / 45 ✅

#SDESheetChallenge
#takeUforward
