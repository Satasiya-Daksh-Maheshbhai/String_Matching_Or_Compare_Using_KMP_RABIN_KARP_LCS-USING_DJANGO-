# PlagiSure 🔍
# String Matching & Similarity Analyzer using KMP, Rabin–Karp & LCS
# 📌 Project Overview

PlagiSure is a string analysis project that implements three important string algorithms:

## KMP (Knuth–Morris–Pratt)

## Rabin–Karp

## LCS (Longest Common Subsequence)

The project helps in detecting pattern matching and measuring similarity between strings, which can be useful for plagiarism detection and text comparison.

# 🎯 Objective

The main objective of PlagiSure is:

To compare strings efficiently

To detect pattern occurrences inside text

To analyze similarity between two strings

To demonstrate differences in algorithm performance

# ⚙️ Algorithms Implemented
## 1️⃣ KMP (Knuth–Morris–Pratt)

Uses LPS (Longest Prefix Suffix) table

Avoids re-checking characters

Efficient linear time pattern searching

Time Complexity:
O(n + m) in Best, Average, and Worst case

## 2️⃣ Rabin–Karp

Uses hashing technique

Compares hash values instead of characters

Fast in average case

Time Complexity:

Best: O(n + m)

Average: O(n + m)

Worst: O(n × m) (due to hash collisions)

## 3️⃣ LCS (Longest Common Subsequence)

Uses Dynamic Programming

Measures similarity between two strings

Builds DP table of size m × n

Time Complexity:
O(m × n) in all cases

# 📊 Time Complexity Comparison
## 🔹 KMP (Knuth–Morris–Pratt)

Best Case: O(n + m)

Average Case: O(n + m)

Worst Case: O(n + m)

## 🔹 Rabin–Karp

Best Case: O(n + m)

Average Case: O(n + m)

Worst Case: O(n × m)

## 🔹 LCS (Longest Common Subsequence)

Best Case: O(m × n)

Average Case: O(m × n)

Worst Case: O(m × n)
Where:

n = length of text

m = length of pattern / second string

# 💡 Features

User input for text and pattern

Displays pattern matching result

Shows LPS table (KMP)

Displays DP table (LCS)

Compares algorithm performance

Educational visualization of algorithms

# 🖥️ Applications

Plagiarism detection systems

DNA sequence matching

Search engines

Text editors (find feature)

Data comparison tools

# 🚀 Future Improvements

Add percentage similarity score

Add GUI interface

Support file upload comparison

Improve hashing to reduce collisions

Add performance graph comparison

#   🏁 Conclusion

PlagiSure demonstrates how different string matching algorithms work and compares their efficiency.
While KMP ensures consistent linear performance, Rabin–Karp provides fast average results, and LCS helps measure overall similarity between strings.

This project strengthens understanding of string algorithms, dynamic programming, and hashing techniques.

# Sample Output :
<img width="1011" height="657" alt="image" src="https://github.com/user-attachments/assets/154a6ccc-049f-4eef-ab0b-7bac9c09df17" />
<img width="1000" height="878" alt="image" src="https://github.com/user-attachments/assets/4296f4fe-4302-45f8-9e78-efa93932174f" />
<img width="963" height="910" alt="image" src="https://github.com/user-attachments/assets/9777f5cc-b135-4179-b585-347b9acfabbd" />
<img width="947" height="842" alt="image" src="https://github.com/user-attachments/assets/3fc45f0e-74b1-460d-a450-b4732cf5eb3a" />
<img width="945" height="857" alt="image" src="https://github.com/user-attachments/assets/6aa8918a-5d12-4207-929f-bf632d27e03c" />
<img width="943" height="727" alt="image" src="https://github.com/user-attachments/assets/2f6a1840-7d89-4641-b799-4c910baccff1" />
