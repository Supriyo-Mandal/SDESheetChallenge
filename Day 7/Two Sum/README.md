# Day 7 - Two Sum

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

Given an array and a target value, the goal is to find whether any two numbers add up to the target. Depending on the variant, we either return YES/NO or the indices of the two numbers.

---

## 🤔 My First Thought

My first instinct was to check every possible pair. It felt natural because if a valid pair exists, comparing all combinations would definitely find it. Not efficient, but a good starting point to understand the problem.

---

## 🐢 Brute Force Approach

### Idea

Pick one element and compare it with every element after it. If any pair adds up to the target, return the answer immediately.

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

Use a hashmap to store numbers already seen. For every element, check whether its required complement (target - current number) already exists in the hashmap.

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

Instead of checking every pair, keep track of previously seen values. The moment the required complement appears, we have our answer. This avoids unnecessary comparisons completely.

### Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(N)  |
| Space Complexity | O(N)  |

### File

```text
optimal.py
```

---

## 🧠 Pattern Used

### Hashing

This problem is a classic example of using hashing for fast lookups. Instead of searching the array repeatedly, we store elements in a hashmap and check for complements in constant time.

---

## 💡 What I Learned

* Whenever I hear "find a pair with a given sum", hashing should be one of my first thoughts.
* It's easy to forget that the complement must be checked before inserting the current element.
* Sometimes the simplest optimization comes from avoiding repeated searches.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(1)  |
| Better      | O(N)  | O(N)  |
| Optimal     | O(N)  | O(N)  |

---

## 📂 Files

```text
Day-7/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like "pair sum", "target sum", "find two numbers", or "return indices" should immediately make me think about hashing.

If the problem asks for quick lookups while traversing an array only once, a hashmap is usually worth considering first.

---

## 🔗 Challenge Progress

Day 7 / 45 ✅

#SDESheetChallenge
#takeUforward
