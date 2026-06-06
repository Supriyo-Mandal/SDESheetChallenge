# Day 4 - Find the Duplicate Number

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

We are given an array containing `n + 1` numbers where every value lies between `1` and `n`. Since one number appears more than once, the task is to find that duplicate while keeping the array unchanged and using very little extra space.

---

## 🤔 My First Thought

My first instinct was to sort the array and look for two equal adjacent elements.

It felt like the quickest way to spot a duplicate.

Then I noticed the constraints about not modifying the array, and that immediately ruled out my first idea.

---

## 🐢 Brute Force Approach

### Idea

Sort the array first and then scan through it. If two neighboring elements are the same, that element is the duplicate.

### Complexity

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(N log N) |
| Space Complexity | O(1)       |

### File

```text
brute_force.py
```

---

## ⚡ Better Approach

### Idea

Use a frequency array to keep track of numbers that have already appeared.

As soon as a number is seen again, return it as the duplicate.

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

The values in the array can be treated like pointers to other indices. Since one value repeats, a cycle is formed. Finding the starting point of that cycle gives the duplicate number.

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

* Fast & Slow Pointers (Floyd's Cycle Detection)

The constraints are the real hint here. We can't modify the array and we need constant extra space. By treating each value as a pointer, the array behaves like a linked list with a cycle, making Floyd's algorithm a perfect fit.

---

## 💡 What I Learned

* The phrase "read-only array" should immediately make me question sorting.
* Sometimes the hardest part is changing how I visualize the problem.
* Floyd's Cycle Detection can appear outside traditional linked list questions.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space |
| ----------- | ---------- | ----- |
| Brute Force | O(N log N) | O(1)  |
| Better      | O(N)       | O(N)  |
| Optimal     | O(N)       | O(1)  |

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

Whenever you see constraints like "don't modify the array", "constant extra space", and "one duplicate guaranteed", pause before reaching for hashing.

If the values naturally point to valid indices, try checking whether the problem can be modeled as a cycle.

---

## 🔗 Challenge Progress

Day 4 / 45 ✅

#SDESheetChallenge
#takeUforward
    
