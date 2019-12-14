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

==写法很多。Horizontal/Vertical scanning, Recursion, Binary Search, Sorting==

Horizontal/Vertical scanning 较直观，前者遍历 list 并将每一个 string 与第一个对比找出 LCP；后者对于字母进行遍历，找到不相同的即终止。

python 中可以直接对列表进行 sort 操作，之后判断第一个与最后一个 string 的 LCP 即可。使用 `startswith`。

## 3Sum

## 3Sum Closest

## Letter Combinations of a Phone Number

## 4Sum

## Remove Nth Node From End of List

## Valid Parentheses

使用 stack (FILO)，注意在 python 中 list 即是 stack，有 `pop` 和 `append` 操作。

建立 dict 对应括号方便判断。

==在使用 HashTable 但不需要 key-value pair 时，用 `set`==

## Merge Two Sorted Lists

MergeSort 中的 Merge 操作。当其中一个为 None 时可以终止判断，并将 linklist 的下一节点设为 `l1 or l2`

## Generate Parentheses

## Merge k Sorted Lists

## Swap Nodes in Pairs

## Reverse Nodes in k-Group

## Remove Duplicates from Sorted Array

使用双指针，可以直接在原有 array 上进行修改而不改变长度，最后截取即可。

python 的 `pop` 改变了原有 array 长度，实际上做了 copy paste，慢且耗内存

## Remove Element

与 [Remove Duplicates from Sorted Array](#remove-duplicates-from-sorted-array) 类似，可使用双指针。

可以进一步优化，使用头尾双指针，将 array 需要删除的元素位置与尾部元素交换，省去大量赋值操作。

## Implement strStr()

对 haystack 的 index 进行遍历即可，注意遍历范围 max 为 `len(haystack) - len(needle) + 1`。

注意 edge case：当 needle 长度大于 haystack 时直接返回 -1

## Divide Two Integers

## Substring with Concatenation of All Words

## Next Permutation

## Longest Valid Parentheses

## Search in Rotated Sorted Array

## Find First and Last Position of Element in Sorted Array

## Search Insert Position

标准的 binary search。在更新是记得是 mid$\pm1$，循环条件为 `low <= mid` 

## Valid Sudoku

## Sudoku Solver

## Count and Say

recursion。使用一个 pointer 来保存当前 char 和个数。

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

需要保存 local_max 和 global_max。

对列表进行遍历：local_max 每次取 `max(local_max + x, x)`，global_max 每次取 `max(local_max, global_max)`。

遍历+判断条件：当 local_max 小于 0 且小于当前数字时，local_max 可以被重置为当前数字。其它情况 local_max 加上当前数字即可。

Divide and Conquer：每次二分 array，每个 array 返回四个数，l 为从第一个数开始的 MS，m 为 MS，r 为以最后一个数结尾的 MS，s 为整个 array 的和。整合两组数得到新的一组返回。

## Spiral Matrix

## Jump Game

## Merge Intervals

## Insert Interval

## Length of Last Word

使用 `s[::-1]` 即可，注意 trailing whitespace 的问题。

可以用 `rstrip()` 和 `rfind(' ')` 寻找 index

## Spiral Matrix II

## Permutation Sequence

## Rotate List

## Unique Paths

## Unique Paths II

## Minimum Path Sum

## Valid Number

## Plus One

倒序遍历，注意判断 edge case 即全部为 9 的情况。

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




