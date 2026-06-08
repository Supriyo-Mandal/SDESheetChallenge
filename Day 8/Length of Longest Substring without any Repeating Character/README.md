# Day 8 - Length of Longest Substring Without Repeating Characters

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find the length of the longest substring that contains only unique characters. The substring must be continuous, and as soon as a character repeats, we need to adjust our window and continue searching for a longer valid substring.

---

## 🤔 My First Thought

My first instinct was to generate every possible substring and keep checking if all characters were unique.

It felt straightforward because I could easily track seen characters using a set. It worked on small examples, but I quickly realized I was rechecking the same characters again and again.

---

## 🐢 Brute Force Approach

### Idea

Start from every index and extend the substring one character at a time.

Use a hash structure to track characters already seen in the current substring. If a duplicate character appears, stop extending and move to the next starting position.

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

The moment a character repeats, everything before its previous occurrence becomes irrelevant for the current window.

Instead of rebuilding substrings, we can maintain a sliding window and jump the left pointer whenever a duplicate character is found.

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

**Sliding Window**

The problem asks for the longest valid continuous segment while maintaining a condition (all characters must be unique).

Sliding Window helps efficiently expand and shrink the current substring without repeatedly processing the same characters.

---

## 💡 What I Learned

* If the question asks for the longest valid substring, Sliding Window should be one of the first patterns I consider.
* Storing the last occurrence of a character is much better than restarting the search.
* The left pointer should never move backward, even when duplicates appear.

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
Day-8/
│
├── README.md
├── brute_force.py
└── optimal.py
```

---

## 🎯 Interview Reminder

Keywords like **longest substring**, **distinct characters**, **unique elements**, or **continuous segment** should immediately make me think about Sliding Window.

A strong interview hint is when the problem asks for an optimal solution while processing a string only once.

---

## 🔗 Challenge Progress

Day 8 / 45 ✅

#SDESheetChallenge
#takeUforward

---
