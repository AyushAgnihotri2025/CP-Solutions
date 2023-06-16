# Minimum Time
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You&nbsp;are given time for insertion, deletion and copying, the task is to calculate the minimum time to write N characters on the screen using these operations. Each time you&nbsp;can insert a character, delete the last character and copy and paste all written characters i.e. after copy operation count of total written character will become twice.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 9</span><span style="font-size:18px">, I = 1, D = 2, C = 1  
<strong>Output:</strong> 5
<strong>Explanation</strong>: N characters can be written
on screen in 5 time units as shown below,
insert a character    
characters = 1,  total time = 1
again insert character      
characters = 2,  total time = 2
copy characters             
characters = 4,  total time = 3
copy characters             
characters = 8,  total time = 4
insert character           
characters = 9,  total time = 5</span></pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 1, I = 10, D = 1, C = 5
<strong>Output: </strong>10
<strong>Explanation</strong>: Insert one character</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>minTimeForWritingChars</code>()&nbsp;</strong>which takes <strong>N, I, D </strong>and<strong> C </strong>as input parameters and returns the integer value<br>
<br>
<strong>Expected Time Complexity:</strong> O(<strong>N</strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>N</strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤&nbsp;<strong>N</strong> ≤ 10<sup>6</sup></span></p>
</div>