# Binary Searchable elements
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Binary search is a search algorithm usually used on a sorted sequence to quickly find an element with a given value. In this problem we will evaluate how binary search performs on data that isn't necessarily sorted. An element is said to be binary searchable if, regardless of how the pivot is chosen the algorithm returns true.<br>
For example:</span></p>

<ul>
	<li><span style="font-size:18px"><code>[2, 1, 3, 4, 6, 5]</code>&nbsp;and&nbsp;<code>target = 5</code>, we cannot find 5. Because when the pivot is 4, we get element 6, then right pointer will move left, so we'll lose the opportunity to find target 5.</span></li>
	<li><span style="font-size:18px"><code>[2, 1, 3, 4, 5, 6]</code>&nbsp;and&nbsp;<code>target = 5</code>, we can find 5. Because wherever we choose the pivots, we'll find target at last.</span></li>
</ul>

<p><span style="font-size:18px">Given an unsorted array of&nbsp;<code>n</code>&nbsp;distinct integers, return the number of elements that are binary searchable.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3
arr[] = {1, 3, 2}
<strong>Output: </strong>1
<strong>Explanation: </strong></span><span style="font-size:18px"><code>However we choose the 
pivots, we will always find the 
number 1 when looking for it. 
This does not hold for 3 and 2.</code></span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
arr[] = {2, 1, 3, 5, 4, 6}
<strong>Output: </strong>2
<strong>Explanation: </strong></span><span style="font-size:18px"><code>3 and 6 are the numbers 
guaranteed to be found in the same way.</code></span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>binarySearchable()</strong>&nbsp;which takes an integer n&nbsp;and an array Arr of size n&nbsp;as input and return the number of elements that are binary searchable.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(n)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ arr[i] ≤ 10<sup>5</sup></span></p>
</div>