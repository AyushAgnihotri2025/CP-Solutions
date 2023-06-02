# Construct list using given q XOR queries
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a list <strong>S</strong> that initially contains a single value <strong>0</strong>. Below are the <strong>Q</strong> queries of the following types:</span></p>

<ul>
	<li><span style="font-size:18px"><strong>0 X</strong>: Insert X in the list</span></li>
	<li><span style="font-size:18px"><strong>1 X</strong>: For every element A in S, replace it by A XOR X.</span></li>
</ul>

<p><span style="font-size:18px">Print all the element in the list in increasing order after performing the given <strong>Q</strong> queries.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 5
Q[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
<strong>Output:
</strong>1 2 3 7
<strong>Explanation:</strong>
[0] (initial value)
[0 6] (add 6 to list)
[0 6 3] (add 3 to list)
[0 6 3 2] (add 2 to list)
[4 2 7 6] (XOR each element by 4)
[1 7 2 3] (XOR each element by 5)
Thus sorted order after performing
queries is [1 2 3 7] </span>
</pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3<strong>
</strong>Q[] = {{0, 2}, {1, 3}, {0, 5}}</span> <span style="font-size:18px">
<strong>Output :</strong>
1 3 5</span>
<span style="font-size:18px"><strong>Explanation:</strong>
[0] (initial value)
[0 2] (add 2 to list)
[3 1] (XOR each element by 3)
[3 1 5] (add 5 to list)
Thus sorted order after performing
queries is [1 3 5].</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>constructList()</strong>&nbsp;which takes an integer <strong>N</strong> the number of queries and <strong>Q</strong> a list of lists of length 2 denoting the queries as input and returns the final constructed list.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N*log(N))<br>
<strong>Expected Auxiliary Space:</strong> O(L), where L is only used for output specific requirements.</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ Length of Q ≤ 10<sup>5</sup></span></p>
</div>