LeetCode 前 200 题

- Easy: 55 - 9
- Medium: 99 - 6
- Hard: 38 - 1
- **Lock**: 156, 157, 158, 159, 161, 163, 170, 186

Other:

- Database：175-178，180-185，196-197
- Shell: 192-195

# 建议

刷题顺序：Top 100 Liked Questions -> Top Interview Questions -> 各个大公司的题目，Amazon -> Zenefits -> Google -> Facebook。从简到难。

总结：知识点（tag）总结，做到看到题目快速反应。总结没见过的用法。

# 盲区

1. `itertools` 对 iterables 操作
2. `reduce` 对 list 操作
3. `collection` high-performance container datatypes:
   1. `Counter`: dict 子类，用来计数
   2. `OrderDict`: dict 子类，保留元素加入顺序
   3. `defaultdict`: dict 子类，元素可以是 list, dict, set, ...
4. bit manipulation：`<< k` 左移 k 位，即乘 $2^k$；`>>` 右移，即整除 $2^k$
5. `zip(*List[List])`：将 “matrix” 转置
6. 对 string 使用 `sorted()` 会输出 list
7. list 无法被 hashed，需要转换为 tuple

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

Expand around center：遍历 index，分别检查奇偶 palindrome，比较长度

Trick：在上述基础上统一奇偶性，即将重复字符全部跳过后比较。且重复字符可以看作整体只需要检查一次。同时可以检查长度，若字符串剩余长度小于目前最大 palindrome 的一半则不需要考虑剩下部分。

[Manacher's Algorithm](https://www.hackerrank.com/topics/manachers-algorithm)：双指针保存 palindrome 中心和右端点位置，利用对称性。

## ZigZag Conversion

创建长度为 rows 的数组，对原字符串遍历并将字符连接至对应的 row 上。==注意 row 的变换只有上下两个方向==。考虑特殊情况即 `rows=1` 或 `rows>=len(s)` 的情况。

## Reverse Integer

不断使用 `divmod` 反向读取数字，在累加前判断溢出情况。

由于 python 的整除和余数与 c++ 和 java 定义不同，在处理负数时会相对麻烦。

python 可以直接转为 str 后颠倒再转回 int，但并不是这题的本意。

==int32 的范围是 [-2^31, 2^31 -1]==

==实际操作中 divmod 要慢于直接取余和整除==

## String to Integer (atoi)

去除 leading whitespace

若第一个 char 不是 '+', '-' 或 数字，则 return

记录下正负性，不断读取数字并判断是否溢出

## Palindrome Number

和 [Reverse Integer](#reverse-integer) 类似，得到 reverse number 之后判断是否与原数相同即可。

不需要考虑负数和溢出。

## Regular Expression Matching

## Container With Most Water

==头尾双指针，只有当更新较小高度的一头才有可能增大面积。==

## Integer to Roman

[Roman to Integer](#roman-to-integer) 的反问题，更难一些。注意需要考虑的数字为 1,4,5,9。

## Roman to Integer

先将罗马字母到数字的对应写为 dict。

一般写法：将所有条件通过 if else 列出。

找规律：如果罗马数字后一个数字比当前数字大，则需要减去当前数字。

## Longest Common Prefix

==写法很多。Horizontal/Vertical scanning, Recursion, Binary Search, Sorting==

Horizontal/Vertical scanning 较直观，前者遍历 list 并将每一个 string 与第一个对比找出 LCP；后者对于字母进行遍历，找到不相同的即终止。

python 中可以直接对列表进行 sort 操作，之后判断第一个与最后一个 string 的 LCP 即可。使用 `startswith`。

## 3Sum

使用 [Two Sum](#two-sum)：遍历数组，对剩余数组寻找 twosum，注意在原有函数上增加 start index。另外需要对得到的结果进行排序并加入 HashTable 防止重复。

双指针：对数组排序，遍历同时对剩下的数组使用双指针。为防止重复，当元素与前一个元素相同时 continue。注意当遍历的元素大于 0 时可以 break。且可以保存每次 right 指针，下一次循环则不需要从尾部开始。

## 3Sum Closest

和 [3Sum](#3sum) 类似

## Letter Combinations of a Phone Number

BackTracking：使用 recursion，将当前数字对应字符串的每一个字母加上下一个数字...

==使用内置函数：`itertools.product` 输出 iterabl 的 Cartesian product。因此将每个 digit 对应 string 存入 list 后调用该函数，再遍历结果合并字符即可。==

==一行代码：`functools.reduce` 对 list 的操作==

## 4Sum

[2Sum](#two-sum) 和 [3Sum](#3sum) 推广版。

==使用 recursion：可以直接推广至 NSum==

使用双重 for 循环 + two pointers

==使用 dict 和 set：三重 for 循环 + dict 查找，set 添加防止重复元素==

## Remove Nth Node From End of List

单次遍历：双指针间隔 N，当第二个位空时改变第一个的 next 到 next.next。==为处理 N 为 List 长度的特殊情况，可以在头部添加一个新 Node==

## Valid Parentheses

使用 stack (FILO)，注意在 python 中 list 即是 stack，有 `pop` 和 `append` 操作。

建立 dict 对应括号方便判断。

==在使用 HashTable 但不需要 key-value pair 时，用 `set`==

## Merge Two Sorted Lists

MergeSort 中的 Merge 操作。当其中一个为 None 时可以终止判断，并将 linklist 的下一节点设为 `l1 or l2`

## Generate Parentheses

使用 backtracking (dfs + pruning)：保存当前左右括号的个数

## Merge k Sorted Lists

## Swap Nodes in Pairs

Recursion：每次选两个 Node 进行调转

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

Bit 左移右移：从大到小计算 dividend 被 2 的指数整除的 quotient，若比 divisor 大，则将结果 + 2 的指数，同时 dividend - divisor * 2 的指数

注意 edge case 和 flow 情况

## Substring with Concatenation of All Words

## Next Permutation

1. 需要更换的数为 从后往前遍历第一个非单调增的数 $a$，该点之后的点为单调减。
2. 寻找更换的数，从后向前遍历找到第一个比 $a$ 大的数，与 a 调换，注意调换后剩余部分仍为单调减。
3. 将剩下的数变为单调增，即使用头尾双指针遍历 swap。

## Longest Valid Parentheses

## Search in Rotated Sorted Array

将判断条件总结清楚即可。

## Find First and Last Position of Element in Sorted Array

左右各用二分法搜索，注意各种区别：`r=len(nums)` 或 `r=len(nums)-1`；`mid=(l+r)//2` 或 `mid=(l+r)//2+1 `；与 `nums[mid]` 相比是否带等于号...

## Search Insert Position

标准的 binary search。在更新是记得是 mid$\pm1$，循环条件为 `low <= mid` 

## Valid Sudoku

row, col, sub-square 可以在双重 for 循环中一起检查，注意 index 的变换

使用 set：双重 for 循环将 value 对应的 row，col，sub-square 作为 tuple 加入 list 中，再使用 set 判断是否有重复。注意 row 和 col 重复问题。

## Sudoku Solver

## Count and Say

recursion。使用一个 pointer 来保存当前 char 和个数。

## Combination Sum

使用 backtracking：

先 sorting 再进行 backtracking，利用排序数组可以提前终止搜索

## Combination Sum II

和 [Combination Sum](#combination-sum) 类似，加避免重复条件的判断即可

## First Missing Positive

## Trapping Rain Water

## Multiply Strings

使用手算乘法的计算方法，创建 list 储存每一位的数字。

## Wildcard Matching

## Jump Game II

## Permutations

Backtracking：对 list 中元素遍历，对剩下元素继续 permutation

Iterative：保存 list[list]，包含当前所有可能的 permutation，对 list 遍历并将新元素插入每个 list 中从 0 到 len(list) 的位置得到下一步的 permutation

## Permutations II

与 [Permutations](#permutations) 类似，有两种方法，需要加入判断防止重复。

Backtracking：对数组排序，若遍历到的元素和前一位相同，则跳过

==Iterative：若当前插入元素和插入断点的元素相同，则跳出插入循环==

## Rotate Image

判断条件：跳位赋值

内置函数：使用 zip(*matrix) 可以对“矩阵”进行转置

转置：顺时针旋转九十度 = 将行排列倒置+转置

## Group Anagrams

排序：对 string 排序后判断是否在 dict 中

26 字母：对每一个 string 创建长度为 26 的 list，计算每一个字母在 string 中出现的次数，将该 list 作为 key。

==质数：利用质数性质，将 26 个字母对应到不同的质数，对于每一个 string 计算对应质数的乘积，并作为 key。存在一一对应关系==

## Pow(x, n)

因 n 为整数，可以通过二进制将 pow 转换为乘法，可以通过 n 的移位实现；或 recursion。注意当 n<0 时需要转化。

## N-Queens

## N-Queens II

## Maximum Subarray

需要保存 local_max 和 global_max。

对列表进行遍历：local_max 每次取 `max(local_max + x, x)`，global_max 每次取 `max(local_max, global_max)`。

遍历+判断条件：当 local_max 小于 0 且小于当前数字时，local_max 可以被重置为当前数字。其它情况 local_max 加上当前数字即可。

Divide and Conquer：每次二分 array，每个 array 返回四个数，l 为从第一个数开始的 MS，m 为 MS，r 为以最后一个数结尾的 MS，s 为整个 array 的和。整合两组数得到新的一组返回。

## Spiral Matrix

Recursion：左右下上 + 剩下的 matrix，注意 edge case 即剩下的 matrix　为空或一行或一列的情况。

Loop：保存 top, bot, left, right 指标并对上右下左遍历，对下左遍历时需要先判断是否和上右重合。

## Jump Game

初始化 `step=0`，从倒数第二位元素向前遍历，若当前元素 <= step 则说明从该元素出发无法到达底端，``step++``，否则重置 `step=0`。最后判断 `step==0` 即可。

## Merge Intervals

排序后，对原 intervals 遍历，比较两个 interval 是否可以 merge，否则 append。

## Insert Interval

## Length of Last Word

使用 `s[::-1]` 即可，注意 trailing whitespace 的问题。

可以用 `rstrip()` 和 `rfind(' ')` 寻找 index

## Spiral Matrix II

和 [Spiral Matrix](#spiral-matrix) 类似

Loop：遍历不断插入数字

U-turn：遍历不断插入数字，若当后一步插入位置元素不为 0 时，则需要做顺时针 90 度转弯。使用 `i, j, di, dj` 实现。

## Permutation Sequence

使用 $m!$ 做基底可将 $k$ 分解为 $k = \sum_{m=0}^{n - 1} k_m m!$，$0\le k_m \le m$. 而 $k_m$ 则对应 $[1,2,\dots, n]$ 的 index。==注意要先将 k 减一==

## Rotate List

和 [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list) 类似。需要先计算 list 长度后用 k 对其取余，若为 0 则不需要 rotate。

## Unique Paths

经典游戏，找到规律 `path[i][j]=path[i-1][j]+path[i][j-1]` 即可。

==更近一步，只保存 `min(m, n)` 的 list，每次循环 `path[i] += path[i-1]` 即可。注意结果关于 m，n 对称==

## Unique Paths II

和 [Unique Paths](#unique-paths) 类似，先对第一行和第一列遍历，遇到 1 后将后面都设置为 0。再从 (1,1) 处遍历，遇 1 则变 0 continue。

## Minimum Path Sum

和 [Unique Paths](#unique-paths)，[Unique Paths II](#unique-paths-ii) 类似，`path[i][j]=min(path[i-1][j], path[i][j-1])`

## Valid Number

## Plus One

倒序遍历，注意判断 edge case 即全部为 9 的情况。

## Add Binary

倒序遍历，将 char 转为 int 后相加，判断进位。注意位数不同的情况。

python 快速解法：`int(n, base=2)` 可以直接将任意进制 string/integer 转为十进制。`bin()` 将 integer 转为二进制 string，注意有 prefix `0b` 因此需要从第二位开始截取。

## Text Justification

## Sqrt(x)

二分法。

牛顿法：转化为求 $x^2 - a$ 的零点问题，牛顿法更加快速。

内置函数：`int(x**0.5)`

## Climbing Stairs

斐波那契数列。

递归：`a(n) = a(n-1) + a(n-2)`，再给出 `a(1), a(2)` 即可。==但做了大量重复计算==

从 `a(1)` 开始计算。

数列求和：求通项公式

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

注意 `next` 和 `next.next`

## Largest Rectangle in Histogram

## Maximal Rectangle

## Partition List

## Scramble String

## Merge Sorted Array

in-place MergeSort。应从大到小排列，`nums1` 使用双指针判断读取位置和插入位置。注意读取位置变为 0 时的特殊情况

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

recursion：自上而下，找到不同的条件即可，recursion 可以简写为 `isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`

iteration：使用 `deque`

## Symmetric Tree

和 [Same Tree](#same-tree) 类似，发现对称条件 `p.left == q.right and p.right == q.left` 即可。

## Binary Tree Level Order Traversal

## Binary Tree Zigzag Level Order Traversal

## Maximum Depth of Binary Tree

recursion 一行 + 终止条件。

## Construct Binary Tree from Preorder and Inorder Traversal

## Construct Binary Tree from Inorder and Postorder Traversal

## Binary Tree Level Order Traversal II

BFS

## Convert Sorted Array to Binary Search Tree

recursion + 二分法

## Convert Sorted List to Binary Search Tree

## Balanced Binary Tree

Tree 计算 depth 的递归算法，注意 recursion 里的终止条件。

## Minimum Depth of Binary Tree

BFS + list

## Path Sum

recursion

## Path Sum II

## Flatten Binary Tree to Linked List

## Distinct Subsequences

## Populating Next Right Pointers in Each Node

## Populating Next Right Pointers in Each Node II

## Pascal's Triangle

只需要在上一个 list 前添 0 再逐位相加即可。

## Pascal's Triangle II

用 pascal 三角与排列数的关系，同时考虑对称性。

## Triangle

## Best Time to Buy and Sell Stock

单次遍历，储存最小值并比较差值。

## Best Time to Buy and Sell Stock II

累加 `max(prices[i] - prices[i-1], 0)`

## Best Time to Buy and Sell Stock III

## Binary Tree Maximum Path Sum

## Valid Palindrome

头尾双指针遍历：判断是否 alphanumeric

遍历构建新字符串：只包含 alphanumeric 的字符，判断 `str == str[::-1]`

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

使用 HashTable：`pop`

使用 Set：`set(list)` 创建一个不包含重复元素的集合

==使用 xor：二进制中 `a xor a = 0`，`a xor 0 = a`==

## Single Number II

## Copy List with Random Pointer

## Word Break

## Word Break II

## Linked List Cycle

HashTable：创建 set 后遍历

==使用双指针：slow & fast runner，一个每次更新一步，一个每次更新两步，在一次遍历内必会相遇。==

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

==使用第二个 stack 来储存最小值，可将 `getMin()` 变为 $O(1)$==

## Binary Tree Upside Down

## Read N Characters Given Read4

## Read N Characters Given Read4 II - Call multiple times

## Longest Substring with At Most Two Distinct Characters

## Intersection of Two Linked Lists

==若两个 linklist 长度相等，则必会在第一个 intersected node 上相遇==

==若长度不同，则一次遍历后跳入对方的 head 重新遍历，必会在第一个 intersected node 上相遇==

## One Edit Distance

## Find Peak Element

## Missing Ranges

## Maximum Gap

## Compare Version Numbers

## Fraction to Recurring Decimal

## Two Sum II - Input array is sorted

可以使用 [Two Sum](#two-sum) 相同的方法。

利用 sorted array 的特点，使用头尾双指针。

## Excel Sheet Column Title

26 进制，注意数字从 0 开始但字母从 1 开始。

## Majority Element

==利用 majority element 个数大于 $\lfloor n / 2 \rfloor$ 的性质==

使用 `collections` 中的 `Counter`：自动计数后使用 `max(c.keys(), key=c.get)`。检查 val 够大时返回。

计数：遇到相同元素 +1，不同 -1，数字为 0 时替换元素为当前元素。到最后返回

sort：排序后返回中间值即可

## Two Sum III - Data structure design

## Excel Sheet Column Number

[Excel Sheet Column Title](#excel-sheet-column-title) 的反问题，简单很多。

## Factorial Trailing Zeroes

trailing zeros 只可能由 2*5 得到，包含 2 为因数的数有 $2, 4, 6, \dots$，包含 5 为因数的数有 $5, 10, 15, \dots$，因此只需要考虑包含 5 为因数的数。

计算被 $5, 5^2, \dots$ 整除得到的数并求和即可。

## Binary Search Tree Iterator

## Dungeon Game

## ~~Combine Two Tables~~

## ~~Second Highest Salary~~

## ~~Nth Highest Salary~~

## ~~Rank Scores~~

## Largest Number

## ~~Consecutive Numbers~~

## ~~Employees Earning More Than Their Managers~~

## ~~Duplicate Emails~~

## ~~Customers Who Never Order~~

## ~~Department Highest Salary~~

## ~~Department Top Three Salaries~~

## Reverse Words in a String II

## Repeated DNA Sequences

## Best Time to Buy and Sell Stock IV

## Rotate Array

直接拼接：`nums[:] = nums[:-k] + nusm[-k:]`

Reverse ($\mathcal{O}(1)$ 空间)：首先将 List 反转，之后将头部至 k-1 元素反转，再将 k 至尾部元素反转 

## Reverse Bits

使用 [Add Binary](add-binary) 中进制相互转化方法，注意由于是 32bit 整数需要加 trailing zeros

使用 2 不断除并将结果 *2 后 + 除 2 的余数

==Bit manipulation：左移右移和且操作==

## Number of 1 Bits

和 [Reverse Bits](reverse-bits) 相似但更简单

==Trick：将 n 与 n-1 进行 & 操作会将最后一位 1 改为 0==

## Word Frequency

## Valid Phone Numbers

## Transpose File

## Tenth Line

## ~~Delete Duplicate Emails~~

## ~~Rising Temperature~~

## House Robber

寻找递推式 $f(0) = a_i,$ $f(1) = \max(a_0, a_1)$, $f(i) = \max(f(i-2) + a_i, f(i - 1))$

## Binary Tree Right Side View

## Number of Islands    




