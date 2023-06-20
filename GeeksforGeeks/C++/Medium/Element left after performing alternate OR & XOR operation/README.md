# Element left after performing alternate OR & XOR operation
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array A of N integers and a 2D matrix denoting q queries. Each query consists of two elements, index and value. Update value at index in A for each query and then perform the following operations to get the result for that query.<br>
1. Perform bitwise OR on each pair&nbsp;<br>
2. Perform bitwise XOR on each pair&nbsp;<br>
Do this alternately till you are left with only a single element in A.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
N = 4
A = {1, 4, 5, 6}
q = 2
query = {{0, 2}, {3, 5}}

<strong>Output:</strong> 1 3

<strong>Explaination: </strong>
<strong>1st query: </strong>
Update the value of A[0] to 2 as given in 
the query pair.The array becomes {2, 4, 5, 6}.
<u>1st iteration:</u> Perform bitwise OR on pairs 
{2,4} and {5,6}. The array becomes {6,7}.
<u>2nd iteration:</u> Perform bitwise XOR on pairs 
{6,7}. The array becomes {1}.


<strong>2nd query: </strong>
Update the value of A[3] to 5 as given in 
the query pair. The array becomes {2, 4, 5, 5}.
<u>1st iteration:</u> Perform bitwise OR on pairs 
{2,4} and {5,5}. The array becomes {6,5}.
<u>2nd iteration:</u> 6^5=3. The array becomes {3}.

</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function&nbsp;<strong>left()&nbsp;</strong>which takes N, A[], q and query as input parameters and returns a list of integers denoting the result for each query.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>O(q*logN)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(N)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ A[i] ≤ 10<sup>5</sup><br>
1 ≤ q ≤ 10<sup>4</sup></span></p>
</div>