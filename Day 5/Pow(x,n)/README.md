# Day 5 - Pow(x, n)

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

The goal is to calculate x raised to the power n. The tricky part is handling very large exponents and negative powers efficiently instead of multiplying the number repeatedly.

---

## 🤔 My First Thought

My first instinct was to multiply x by itself n times and keep updating the answer. It felt straightforward because that's how we normally calculate powers manually. But once I noticed the exponent could be huge, I knew that approach wouldn't survive the constraints.

---

## 🐢 Brute Force Approach

### Idea

Start with an answer of 1 and multiply it by x exactly n times. For negative powers, convert the exponent to positive and take the reciprocal at the end.

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

No meaningful intermediate optimization for this problem.

---

## 🚀 Optimal Approach

### Key Observation

Instead of multiplying x repeatedly, we can reduce the exponent by half whenever it's even. By squaring the base and halving the exponent, we eliminate a large amount of work in each step.

### Complexity

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | O(log N) |
| Space Complexity | O(log N) |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

* Binary Exponentiation

This problem is a classic application of Binary Exponentiation. The idea is to use the binary representation of the exponent and repeatedly square the base, reducing the number of operations drastically compared to naive multiplication.

---

## 💡 What I Learned

* Seeing a very large exponent is usually a hint that repeated multiplication won't work.
* I almost forgot to handle negative powers separately.
* Squaring the base while halving the exponent is a pattern worth remembering for interviews.

---

## 🔍 Complexity Comparison

| Approach    | Time     | Space    |
| ----------- | -------- | -------- |
| Brute Force | O(N)     | O(1)     |
| Better      | —        | —        |
| Optimal     | O(log N) | O(log N) |

---

## 📂 Files

```text
Day-5/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever a problem involves powers, exponents, or repeated multiplication with large values of n, think about Binary Exponentiation.

A good interview clue is when the brute-force solution is O(N) and the constraints clearly demand something much faster.

---

## 🔗 Challenge Progress

Day 5 / 45 ✅

#SDESheetChallenge
#takeUforward
