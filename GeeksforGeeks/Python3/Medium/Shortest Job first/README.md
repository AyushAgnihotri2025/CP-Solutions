# Shortest Job first
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek is a software engineer. He is assigned with a task of calculating <strong>average waiting time</strong> of all the processes by following <strong>shortest job first</strong> policy.</span></p>

<p><span style="font-size:18px">The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next.</span></p>

<p><span style="font-size:18px">Given an arrays of integers <strong>bt</strong> of size <strong>n</strong>. Array <strong>bt</strong> denotes <strong>burst time</strong> of each process. Calculate <strong>average waiting time</strong> of all the processes and return the&nbsp;nearest integer which is smaller or equal to the output.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> Consider all process are availiable at time 0.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 5
bt = [4,3,7,1,2]
<strong>Output: </strong>4
<strong>Explanation:</strong> After sorting burst times by shortest job policy, calculated average waiting time is 4.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 4
arr = [1,2,3,4]
<strong>Output: </strong>2
Explanation: After sorting burst times by shortest job policy, calculated average waiting time is 2.</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>solve()</strong> which takes <strong>bt</strong><strong>[]</strong>&nbsp;as input parameter&nbsp;and returns the <strong>average waiting time</strong>&nbsp;of all the processes.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(n<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(n)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 100</span><br>
<span style="font-size:18px">1 &lt;= arr[i] &lt;= 100</span></p>
</div>