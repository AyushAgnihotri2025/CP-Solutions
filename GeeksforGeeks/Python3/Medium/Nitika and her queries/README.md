# Nitika and her queries
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Nitika recently read about XOR operation and she got </span><span style="font-size:18px">obssessed</span><span style="font-size:18px"> with it. She has an array <strong>a</strong> containing <strong>N</strong> Positive integers.She wants to perform <strong>Q</strong> queries on the array.In a&nbsp;</span><span style="font-size:18px">query</span><span style="font-size:18px"> She gives two integers <strong>L</strong> and <strong>R</strong>.(1 based indexing).Now, she asks what is the xor of all the elements of the array after not including the subarray ranging from L to R (both inclusive).Nitika guarantees that in each query, The resulting array is&nbsp;</span><span style="font-size:18px">non empty</span><span style="font-size:18px">. The queries are given in a 2D matrix <strong>query</strong> having L and R for each entry.&nbsp;</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 10, Q = 3
a = {4, 7, 8, 5, 9, 6, 1, 0, 20, 10}
query = {{3, 8},{1, 6},{2, 3}}
<strong>Output:</strong> 
29
31
17
<strong>Explaination:</strong> For the first query: 
The resulting array is: (4 ,7 ,20, 10).
Their Xor will be: 29. 
For the Second query: The resulting 
array is: (1, 0, 20, 10). Their Xor 
will be: 31. 
For the Third query:  The resulting 
array is: (4, 5, 9, 6, 1,</span><span style="font-size:18px">0 ,</span><span style="font-size:18px">20, 10). 
Their Xor will be: 17.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
you do not need to read input or print anything. Your task is to complete the function <strong>specialXor()</strong> which takes N, Q, a[] and query as input parameters and returns a list containing answer for each query.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N+Q*logN)<br>
<strong>Expected Auxiliary Space:</strong> O(N+Q)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N, Q ≤ 10<sup>5</sup><br>
1 ≤ A[i] ≤ 10<sup>9</sup><br>
1 ≤ L, R ≤ N&nbsp;&nbsp;</span></p>
</div>