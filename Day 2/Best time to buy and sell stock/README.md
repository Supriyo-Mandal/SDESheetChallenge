# Day 2 - Best Time to Buy and Sell Stock

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

Given stock prices for different days, the goal is to find the maximum profit possible by buying once and selling once in the future.

The challenge is making sure the buy happens before the sell while finding the best profit efficiently.

---

## 🤔 My First Thought

My first instinct was to check every possible buy day and every possible sell day after it.

It felt safe because I'd never miss the best transaction. But pretty quickly, it felt like I was comparing way more pairs than necessary.

---

## 🐢 Brute Force Approach

### Idea

Try every valid buy-sell pair. For each buy day, check all future days as possible selling days and keep track of the maximum profit found.

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

No meaningful intermediate optimization for this problem.

---

## 🚀 Optimal Approach

### Key Observation

Instead of checking every pair, I only need to remember the lowest stock price seen so far.

For each day, I can calculate the profit if I sell today and update the maximum profit. This removes the need for nested loops completely.

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

**Greedy**

At every step, we maintain the minimum price seen so far and use it to calculate the best possible profit for the current day.

The decision is local, but it guarantees the global maximum profit, which makes this a classic Greedy problem.

---

## 💡 What I Learned

* "Buy before sell" is more important than just finding the minimum and maximum values.
* Tracking the minimum value seen so far can eliminate a lot of unnecessary comparisons.
* A single pass is often enough when the answer depends on previous information only.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(1)  |
| Better      | —     | —     |
| Optimal     | O(N)  | O(1)  |

---

## 📂 Files

```text
Day-2/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **maximum profit**, **buy before sell**, **single transaction**, and **best difference** should immediately make me think about maintaining a running minimum.

If the problem asks for the best future gain while scanning an array, tracking the smallest value seen so far is usually a strong hint.

---

## 🔗 Challenge Progress

Day 2 / 45 ✅

#SDESheetChallenge
#takeUforward
