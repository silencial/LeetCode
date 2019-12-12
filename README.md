## Two Sum

空间换时间，创建 HashTable，遍历同时简化问题。

==dict 是 HashTable==

## Add Two Numbers

加法器实现。因为只有两个数相加，进位最多为 1。注意最后的进位。

## Longest Substring Without Repeating Characters

使用 sliding window。在当前 window 为 [i, j) 且其中无重复字符时，考虑 j 位字符。如果与 [i, j) 中字符不同则最大长度 +1；如果重复位置发生在 i' (i' >= i)，则可以直接将 window head 位置更新为 i'+1。

查找字符通过 dict 实现。

注意 edge case，即字符串为空情况。

## Median of Two Sorted Arrays



## Longest Palindromic Substring

## ZigZag Conversion

## Reverse Integer

不断使用 `divmod` 反向读取数字，在累加前判断溢出情况。

由于 python 的整除和余数与 c++ 和 java 定义不同，在处理负数时会相对麻烦。

python 可以直接转为 str 后颠倒再转回 int，但并不是这题的本意。

==int32 的范围是 [-2^31, 2^31 -1]==

==实际操作中 divmod 要慢于直接取余和整除==

## String to Integer (atoi)

## Palindrome Number

和 [Reverse Integer](#reverse-integer) 类似，得到 reverse number 之后判断是否与原数相同即可。

不需要考虑负数和溢出。

## Regular Expression Matching

## Container With Most Water

## Integer to Roman

## Roman to Integer

先将罗马字母到数字的对应写为 dict。

一般写法：将所有条件通过 if else 列出。

找规律：如果罗马数字后一个数字比当前数字大，则需要减去当前数字。

## Longest Common Prefix

## 3Sum

## 3Sum Closest

## Letter Combinations of a Phone Number

## 4Sum

## Remove Nth Node From End of List

## Valid Parentheses

## Merge Two Sorted Lists

## Generate Parentheses

## Merge k Sorted Lists

## Swap Nodes in Pairs

## Reverse Nodes in k-Group

## Remove Duplicates from Sorted Array

## Remove Element

## Implement strStr()

## Divide Two Integers

## Substring with Concatenation of All Words

## Next Permutation

## Longest Valid Parentheses

## Search in Rotated Sorted Array

## Find First and Last Position of Element in Sorted Array

## Search Insert Position

## Valid Sudoku

## Sudoku Solver

## Count and Say

## Combination Sum

## Combination Sum II

## First Missing Positive

## Trapping Rain Water

## Multiply Strings

## Wildcard Matching

## Jump Game II

## Permutations

## Permutations II

## Rotate Image

## Group Anagrams

## Pow(x, n)

## N-Queens

## N-Queens II

## Maximum Subarray

## Spiral Matrix

## Jump Game

## Merge Intervals

## Insert Interval

## Length of Last Word

## Spiral Matrix II

## Permutation Sequence

## Rotate List

## Unique Paths

## Unique Paths II

## Minimum Path Sum

## Valid Number

## Plus One

## Add Binary

## Text Justification

## Sqrt(x)

## Climbing Stairs

## Simplify Path

## Edit Distance

## Set Matrix Zeroes

## Search a 2D Matrix

## Sort Colors

## Minimum Window Substring

## Combinations

## Subsets

## Word Search

## Remove Duplicates from Sorted Array II

## Search in Rotated Sorted Array II

## Remove Duplicates from Sorted List II

## Remove Duplicates from Sorted List

## Largest Rectangle in Histogram

## Maximal Rectangle

## Partition List

## Scramble String

## Merge Sorted Array

## Gray Code

## Subsets II

## Decode Ways

## Reverse Linked List II

## Restore IP Addresses

## Binary Tree Inorder Traversal

## Unique Binary Search Trees II

## Unique Binary Search Trees

## Interleaving String

## Validate Binary Search Tree

## Recover Binary Search Tree

## Same Tree

## Symmetric Tree

## Binary Tree Level Order Traversal

## Binary Tree Zigzag Level Order Traversal

## Maximum Depth of Binary Tree

## Construct Binary Tree from Preorder and Inorder Traversal

## Construct Binary Tree from Inorder and Postorder Traversal

## Binary Tree Level Order Traversal II

## Convert Sorted Array to Binary Search Tree

## Convert Sorted List to Binary Search Tree

## Balanced Binary Tree

## Minimum Depth of Binary Tree

## Path Sum

## Path Sum II

## Flatten Binary Tree to Linked List

## Distinct Subsequences

## Populating Next Right Pointers in Each Node

## Populating Next Right Pointers in Each Node II

## Pascal's Triangle

## Pascal's Triangle II

## Triangle

## Best Time to Buy and Sell Stock

## Best Time to Buy and Sell Stock II

## Best Time to Buy and Sell Stock III

## Binary Tree Maximum Path Sum

## Valid Palindrome

## Word Ladder II

## Word Ladder

## Longest Consecutive Sequence

## Sum Root to Leaf Numbers

## Surrounded Regions

## Palindrome Partitioning

## Palindrome Partitioning II

## Clone Graph

## Gas Station

## Candy

## Single Number

## Single Number II

## Copy List with Random Pointer

## Word Break

## Word Break II

## Linked List Cycle

## Linked List Cycle II

## Reorder List

## Binary Tree Preorder Traversal

## Binary Tree Postorder Traversal

## LRU Cache

## Insertion Sort List

## Sort List

## Max Points on a Line

## Evaluate Reverse Polish Notation

## Reverse Words in a String

## Maximum Product Subarray

## Find Minimum in Rotated Sorted Array

## Find Minimum in Rotated Sorted Array II

## Min Stack

## Binary Tree Upside Down

## Read N Characters Given Read4

## Read N Characters Given Read4 II - Call multiple times

## Longest Substring with At Most Two Distinct Characters

## Intersection of Two Linked Lists

## One Edit Distance

## Find Peak Element

## Missing Ranges

## Maximum Gap

## Compare Version Numbers

## Fraction to Recurring Decimal

## Two Sum II - Input array is sorted

## Excel Sheet Column Title

## Majority Element

## Two Sum III - Data structure design

## Excel Sheet Column Number

## Factorial Trailing Zeroes

## Binary Search Tree Iterator

## Dungeon Game

## Combine Two Tables

## Second Highest Salary

## Nth Highest Salary

## Rank Scores

## Largest Number

## Consecutive Numbers

## Employees Earning More Than Their Managers

## Duplicate Emails

## Customers Who Never Order

## Department Highest Salary

## Department Top Three Salaries

## Reverse Words in a String II

## Repeated DNA Sequences

## Best Time to Buy and Sell Stock IV

## Rotate Array

## Reverse Bits

## Number of 1 Bits

## Word Frequency

## Valid Phone Numbers

## Transpose File

## Tenth Line

## Delete Duplicate Emails

## Rising Temperature

## House Robber

## Binary Tree Right Side View

## Number of Islands    




