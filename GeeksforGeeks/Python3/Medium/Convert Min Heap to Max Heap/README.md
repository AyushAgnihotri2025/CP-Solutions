# Convert Min Heap to Max Heap
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array <strong>arr</strong> of <strong>N</strong> integers representing&nbsp;a min Heap. The task is to convert it to max Heap.</span></p>

<p><span style="font-size:18px">A max-heap&nbsp;is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1</strong>:</span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
N = 4
arr = [1, 2, 3, 4]
<strong>Output</strong>:
</span><span style="font-size:18px">[4, 2, 3, 1]<strong>
Explanation</strong>:</span>

<span style="font-size:18px">The given min Heap:</span>

<span style="font-size:18px">          1
        /   \
      2       3
     /
   4</span>

<span style="font-size:18px">Max Heap after conversion:</span>

<span style="font-size:18px">         4
       /   \
      3     2
    /
   1</span></pre>

<p><span style="font-size:18px"><strong>Example 2</strong>:</span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
N = 5
arr = [3, 4, 8, 11, 13]
<strong>Output</strong>:
<strong>[</strong>13, 11, 8, 4, 3]</span><span style="font-size:18px"><strong>
Explanation</strong>:</span>

<span style="font-size:18px">The given min Heap:</span>

<span style="font-size:18px">          3
        /   \
      4      8
    /   \ 
  11     13</span>

<span style="font-size:18px">Max Heap after conversion:</span>

<span style="font-size:18px">          13
        /    \
      11      8
    /   \ 
   4     3</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Complete the function int <strong>convertMinToMaxHeap</strong>(), which takes integer N and array represented minheap as input and converts it to the array representing maxheap. You don't need to return or print anything, modify the original array itself.</span></p>

<p><span style="font-size:18px"><strong>Note</strong>: Only an unique solution is possible under the expected time complexity.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity</strong>: O(N * log N)<br>
<strong>Expected Auxiliary Space</strong>: O(N)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong></span></p>

<p><span style="font-size:18px">1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= arr[i] &lt;= 10<sup>9</sup></span></p>
</div>