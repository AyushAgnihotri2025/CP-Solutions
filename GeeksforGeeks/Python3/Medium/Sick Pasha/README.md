# Sick Pasha
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Pasha has been very sick. His platelets went way down. Being a paranoid person, he consulted N doctors about the optimal range in which Platelet Count should lie. The </span><span style="font-size:18px">i-th</span><span style="font-size:18px"> doctor suggested that the Platelet count should be between li and </span><span style="font-size:18px">ri, inclusive, to be called normal.<br>
Now, Pasha thinks that a Platelet count is Safe to have if at least K&nbsp;Doctors recommend it. Pasha now asks Q Queries. In each query- he will give an integer P (the platelet count). Pasha wants to know if the entered Platelet count is safe to have or not.</span><br>
<br>
&nbsp;</p>

<p><span style="font-size:20px"><strong>Example 1:</strong></span><br>
&nbsp;</p>

<pre><span style="font-size:20px"><strong>Input :</strong> 
V[] = {[1, 10], [5, 7], [7, 12], 
    [15, 25], [20, 25]}, K = 3, 
queries[] = {7, 5, 10, 16}
<strong>Output :</strong> 
Yes
No
Yes
No
<strong>Explanation:
The first query :</strong> 7 is in [1,10] , 
[5,10] , [7,12] So recommended by 3 
Doctors-YES
<strong>The second query :</strong> 5 is in [1,10] , 
[5,10] recommended by 2 doctors- "No"
<strong>The third query :</strong> 10 is in [1,10] , 
[5,10] , [7,12] recommended by 3 
doctors- "Yes"
<strong>The Fourth query :</strong> 16 is in [15,25]
recommended by 1 doctors- "No"</span><span style="font-size:20px">
</span></pre>

<p><br>
<span style="font-size:20px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>QueryComputation()</strong> that takes the size of an array <strong>(N)</strong>, a 2-d&nbsp;array <strong>(arr)</strong>, integer <strong>K</strong>,&nbsp; no. of queries <strong>q, </strong>an<strong>&nbsp;</strong>array of queries <strong>(queries)</strong>, and return the boolean array that has true if the query is true else false. The driver code takes care of the printing.</span></p>

<p><span style="font-size:20px"><strong>Expected Time Complexity:</strong>&nbsp;O(N + Q).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N,Q ≤ 2*10<sup>5</sup><br>
1 ≤ Z ≤ N<br>
1 ≤ Li ≤ Ri ≤ 2*10<sup>5</sup><br>
1 ≤ P ≤ 2*10<sup>5</sup></span></p>
</div>