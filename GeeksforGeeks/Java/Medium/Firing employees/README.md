# Firing employees
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek is the founder of Geek Constructions. He always maintains a black-list&nbsp;of potential employees which can be fired at any moment.</span></p>

<p><span style="font-size:18px">The company has N employees (including Geek), and each employee is assigned a distinct rank (1 &lt;= rank &lt;= N) at the time of joining. The company has a hierarchical &nbsp;management such that each employee always has one immediate senior.&nbsp;</span></p>

<p><span style="font-size:18px">Geek has a strange and unfair way of evaluating an employees performance. He sums the employee's rank and the number of seniors the employee has. If it is a prime number, the employee is put up on the black-list.</span></p>

<p><span style="font-size:18px">Given an&nbsp;array arr[] in order of the rank of company employees. For rank i, arr[i] represents the rank of the immediate senior of the employee with the ith rank. If geek's rank is i, then arr[i] is always equal to 0 as there is no one senior to him. Find out the number of Black-Listed employees.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> The black-list can not&nbsp;contain Geeks name as he is the founder of the company and he is the one that makes the list.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 4
arr[] = {0, 1, 1, 2}</span>

<strong><span style="font-size:18px">Output: 1</span></strong>

<span style="font-size:18px"><strong>Explanation:</strong>
The hierarchy is as follows</span>

<span style="font-size:18px">       (Geek)
       Rank 1
        /   \
  Rank 2     Rank 3  
      /
Rank 4</span>

<span style="font-size:18px">Performance = rank + number of seniors
Performance for rank 1 = not considered.
Performance for rank 2 = 2+1 = 3 (prime)
Performance for rank 3 = 3+1 = 4 (not prime)
Performance for rank 4 = 4+2 = 6 (not prime)
Therefore, only employee 1 is black-listed.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 3
arr[] = {2, 3, 0}</span>

<span style="font-size:18px"><strong>Output:</strong> 2</span>

<span style="font-size:18px"><strong>Explanation: </strong>
The hierarchy is as follows</span>

<span style="font-size:18px">       (Geek)
       Rank 3
        /   
  Rank 2     
      /
Rank 1
</span>
<span style="font-size:18px">Performance for rank 3 = not considered. 
Performance for rank 2 = 2+1 = 3 (prime) 
Performance for rank 1 = 1+2 = 3 (prime)</span>
<span style="font-size:18px">Rank 1 and 2 are both black-listed.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task: &nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function<strong> firingEmployees()</strong> which takes the array arr[] and its size N as input parameters. It returns the number of black-listed employees.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= i &lt;= N<br>
1 &lt;= arr[i] &lt;= 10<sup>5</sup></span></p>
</div>