# Day 8 - Count the Number of Subarrays with Given XOR K

> Part of my #SDESheetChallenge journey.

---

## 📌 Problem Summary

In this problem, we need to find how many subarrays have a bitwise XOR equal to a given value K. Instead of checking every possible subarray, the challenge is to identify a faster way to count them efficiently.

---

## 🤔 My First Thought

My first instinct was to generate every possible subarray and keep calculating its XOR. It felt straightforward because XOR can be updated while extending the subarray. I knew it would work, but I also had a feeling it wouldn't scale well for larger inputs.

---

## 🐢 Brute Force Approach

### Idea

Start every subarray from each index and keep extending it one element at a time. Maintain the running XOR for the current subarray and increase the count whenever the XOR becomes equal to K.

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

If two prefix XOR values differ by K, then the XOR of the subarray between them will be K. Storing previously seen prefix XOR values in a hashmap lets us count valid subarrays in a single traversal.

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

**Hashing + Prefix XOR**

This problem is very similar to prefix sum problems, but with XOR properties instead of addition. By storing frequencies of previous prefix XOR values in a hashmap, we can instantly determine how many subarrays ending at the current index satisfy the condition.

---

## 💡 What I Learned

* Prefix XOR plays the same role here that prefix sum does in sum-based problems.
* Forgetting to initialize the hashmap with XOR value `0` can miss valid subarrays.
* Whenever a problem asks for subarray XOR counts, hashing should be one of the first things to consider.

---

## 🔍 Complexity Comparison

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(N²) | O(1)  |
| Better      | —     | —     |
| Optimal     | O(N)  | O(N)  |

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

Keywords like **subarray count**, **XOR equals K**, **continuous segment**, and **count all occurrences** should immediately make me think about Prefix XOR and Hashing.

A useful interview hint is to ask: *"Can I represent this subarray operation using a prefix value?"* If yes, a hashmap is often involved.

---

## 🔗 Challenge Progress

Day 8 / 45 ✅

#SDESheetChallenge
#takeUforward
