# Missing Point of a Parallelogram
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given three coordinate points <strong>A</strong>, <strong>B</strong> and <strong>C</strong>, find the missing point <strong>D</strong> such that <strong>ABCD</strong> can be a parallelogram. If there are multiple such points, find the lexicographically smallest coordinate.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
A = (3, 2)
B = (3, 4)
c = (2, 2)
<strong>Output:
</strong>2.000000 0.000000
<strong>Explanation</strong>: There are two options for 
point D : (2, 4) and (2, 0) such that ABCD 
forms a parallelogram. Since (2, 0) is 
lexicographically smaller than (2, 4). Hence,
(2, 0) is the answer.</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findPoint()&nbsp;</strong>which takes three list of integers <strong>A[]</strong>, <strong>B[] </strong>and <strong>C[]</strong> and return <strong>D[]</strong> list of two numbers with a precision of 6 decimal places where first element of <strong>D[ ] </strong>denote x coordinate and second&nbsp;element of <strong>D[ ] </strong>denote y&nbsp;coordinate.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(1)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ x, y ≤ 1000 , where x and y denote coordinates of points A, B and C.</span></p>
</div>