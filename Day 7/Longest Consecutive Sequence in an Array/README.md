# Day 7 - Longest Consecutive Sequence

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find the length of the longest sequence of consecutive numbers present in an array. The numbers can appear in any order, and we only care about the longest chain of consecutive values.

---

## 🤔 My First Thought

My first instinct was to pick every number and keep checking if the next consecutive number existed in the array.

It felt natural because I could build the sequence one number at a time. I knew it would work, but I also had a feeling it would become slow once the array got bigger.

---

## 🐢 Brute Force Approach

### Idea

For every element, keep searching for the next consecutive number using a linear search. Continue until the sequence breaks and track the maximum length found.

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

Sort the array first so consecutive numbers come together. Then scan the sorted array while counting the current streak and updating the longest sequence length.

### Complexity

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | O(N log N) |
| Space Complexity | O(1)       |

### File

```text
better.py
```

---

## 🚀 Optimal Approach

### Key Observation

A number only needs to start building a sequence if the previous number doesn't exist. Using a set allows constant-time lookups, so we can grow sequences efficiently without repeatedly checking the same elements.

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

* Hashing

The set is the real game changer here. Instead of searching the array again and again, we store all elements in a hash set and quickly check whether consecutive numbers exist. The trick is to start counting only from the beginning of a sequence.

---

## 💡 What I Learned

* If a problem involves frequent existence checks, a set is usually worth considering.
* Starting from every element causes a lot of unnecessary work.
* The clue was realizing that only sequence starters actually matter.

---

## 🔍 Complexity Comparison

| Approach    | Time       | Space |
| ----------- | ---------- | ----- |
| Brute Force | O(N²)      | O(1)  |
| Better      | O(N log N) | O(1)  |
| Optimal     | O(N)       | O(N)  |

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

Whenever you see words like "longest consecutive", "sequence", or "find if a number exists", think about hashing before jumping into sorting.

A useful hint is asking: "Do I really need to start from every element?" If the answer is no, there's usually a smarter way.

---

## 🔗 Challenge Progress

Day 7 / 45 ✅

#SDESheetChallenge
#takeUforward
