# Day 4 - Find the Repeating and Missing Number

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, one number from the range `1 to n` is missing, and another number appears twice. The task is to find both numbers without modifying the original array. The challenge is to do it efficiently while keeping space usage low.

---

## 🤔 My First Thought

My first instinct was to count how many times every number appears.

It felt straightforward because once a number appears twice and another doesn't appear at all, the answer is right there.

Not the most efficient idea, but it was the easiest place to start.

---

## 🐢 Brute Force Approach

### Idea

For every number from `1` to `n`, scan the entire array and count its occurrences.

If a number appears twice, it's the repeating number. If it never appears, it's the missing number.

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

### Idea

Use a frequency array to track how many times each number appears.

After counting frequencies, the number with frequency `2` is repeating and the number with frequency `0` is missing.

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

The array contains numbers from `1` to `n`, which means the expected sum and expected sum of squares are already known.

Comparing expected values with actual values gives two equations that can directly reveal the repeating and missing numbers without extra space.

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

**Math / Equation-Based Analysis**

Instead of storing frequencies, we use mathematical properties of the numbers from `1` to `n`.

The difference in sums and sum of squares helps form equations that directly identify the repeating and missing values while using constant extra space.

---

## 💡 What I Learned

* Seeing numbers restricted to `1...n` is often a clue that math tricks might work.
* It's easy to forget about integer overflow when using sum-of-squares formulas in some languages.
* Not every O(N) solution is optimal if it still uses extra memory.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(1)  |
| Better      | O(N)  | O(N)  |
| Optimal     | O(N)  | O(1)  |

---

## 📂 Files

```text
Day-4/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever a problem says numbers are from `1 to n` and exactly one value is missing or repeated, pause before using hashing.

Check if sum, sum of squares, XOR, or cycle-detection properties can help reduce space complexity.

---

## 🔗 Challenge Progress

Day 4 / 45 ✅

#SDESheetChallenge
#takeUforward

---
