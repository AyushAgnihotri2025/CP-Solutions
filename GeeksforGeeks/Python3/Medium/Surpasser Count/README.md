# Surpasser Count
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">An element Y is said to be the surpasser of element X if it is a greater element on the right of X. ie, if X = arr[i] and Y = arr[j], i&lt;j and Arr[i] &lt; Arr[j].&nbsp;<br>
Given an array of size N containing distinct integers, find the number of surpassers for each of its elements.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 5
Arr[] = {4, 5, 1, 2, 3}</span>

<span style="font-size:18px"><strong>Output:</strong> 1 0 2 1 0</span>

<span style="font-size:18px"><strong>Explanation:</strong> There are no elements greater 
than 3 at the right of 3. There is one 
element at right of 2 and greater than 2. 
There are 2 elements greater than 1 at the 
right of 1. And so on.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 6
Arr[] = {2, 7, 5, 3, 8, 1}</span>

<span style="font-size:18px"><strong>Output:</strong> 4 1 1 1 0 0</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>findSurpasser()</strong> which takes the array of integers arr and n as input parameters and returns an array of integers of size N denoting the surpasser count of each element of arr.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(N*logN)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ Arr[i] ≤ 10<sup>6</sup></span></p>
</div>