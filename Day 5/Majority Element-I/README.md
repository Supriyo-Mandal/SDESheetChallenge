# Day 5 - Majority Element-I

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find the element that appears more than half the size of the array. The problem guarantees that such an element always exists, so the goal is to identify it as efficiently as possible.

---

## 🤔 My First Thought

My first instinct was to count how many times each number appears and then return the one with the highest frequency.

It felt straightforward because majority means "appears the most", and counting frequencies is usually the first thing that comes to mind.

---

## 🐢 Brute Force Approach

### Idea

For every element, scan the entire array again and count how many times it appears.

If its frequency becomes greater than `n/2`, return it as the majority element.

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

Use a hashmap to store the frequency of each element while traversing the array.

After counting frequencies, find the element whose count exceeds `n/2`.

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

If one element appears more than half the time, every other element combined cannot completely cancel it out.

This observation leads to the Boyer-Moore Voting Algorithm, which keeps track of a candidate and eliminates competing elements.

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

**Boyer-Moore Voting Algorithm**

The majority element appears more than `n/2` times, which means it survives every possible cancellation against other elements.

Instead of storing frequencies, we use a running candidate and count to identify the majority element in constant space.

---

## 💡 What I Learned

* The condition "appears more than n/2 times" is a huge clue.
* I initially focused on counting frequencies instead of thinking about cancellation.
* Boyer-Moore is one of those algorithms that's easy to forget but very useful in interviews.

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
Day-5/
│
├── README.md
├── brute_force.py
├── better.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Whenever you see phrases like **"appears more than n/2 times"**, think beyond frequency counting.

If the problem guarantees the existence of a majority element, Boyer-Moore Voting Algorithm should immediately come to mind.

---

## 🔗 Challenge Progress

Day 5 / 45 ✅

#SDESheetChallenge
#takeUforward
