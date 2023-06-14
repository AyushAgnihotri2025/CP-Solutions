# Sort a 2D vector diagonally
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an <strong>NxM</strong> 2D matrix, rearrange such that&nbsp;<br>
Each diagonal in the lower left triangle of the rectangular grid is sorted in ascending order.&nbsp;<br>
Each diagonal in the upper right triangle of the rectangular grid is sorted in descending order.&nbsp;<br>
The major diagonal in the grid starting from the top-left corner is not rearranged.&nbsp;</span></p>

<p><br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 4, M = 5 
matrix = {{3 6 3 8 2},
          {4 1 9 5 9},
          {5 7 2 4 8},
          {8 3 1 7 6}}
<strong>Output:</strong>
3 9 8 9 2
1 1 6 5 8
3 4 2 6 3
8 5 7 7 4
<strong>Explanation:</strong></span>
<span style="font-size:18px">Before:
<img alt="" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20201012182216/after1.png" style="height:139px; width:180px"></span>
<span style="font-size:18px">After:
<img alt="" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20201012182218/before.png" style="height:150px; width:185px"></span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>diagonalSort()</strong> which takes the matrix, n and m as input parameter and rearranges the elements of the matrix.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(NxM)<br>
<strong>Expected Auxiliary Space: </strong>O(N+M)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N,M &lt;= 10<sup>4&nbsp;</sup>,&nbsp;1&lt;=N*M&lt;=10<sup>5</sup><br>
1 &lt;= matrix[i] &lt;= 10<sup>3</sup></span></p>
</div>