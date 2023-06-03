# Cows of FooLand
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Cows in the FooLand city are interesting animals. One of their specialities is related to producing offsprings. A cow in FooLand produces its first calve (female calf) at the age of <strong>two years</strong> and proceeds to produce other calves (one female calf a year).</span></p>

<p><span style="font-size:18px">Now the farmer Harold wants to know how many animals would he have at the end of <strong>N</strong> years, if we assume that none of the calves dies, given that initially, he has only one female calf?</span></p>

<p><span style="font-size:18px">Since the answer can be huge, print it modulo <strong>10<sup>9</sup>+7</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 2
<strong>Output: </strong>2
<strong>Explanation: </strong>At the end of 1 year, he will have 
only 1 cow, at the end of 2 years he will have 
2 animals (one parent cow C1 and other baby 
calf B1 which is the offspring of cow C1).</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 4
<strong>Output: </strong>5
<strong>Explanation: </strong></span><span style="font-size:18px">At the end of 1 year, he will have
only 1 cow, at the end of 2 years he will have
2 animals (one parent cow C1 and other baby
calf B1 which is the offspring of cow C1). At
the end of 3 years, he will have 3 animals (one
parent cow C1 and 2 female calves B1 and B2, C1
is the parent of B1 and B2).At the end of 4 
years,he will have 5 animals (one parent cow C1,
3 offsprings of C1 i.e. B1, B2, B3 and one 
offspring of B1).</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong></span><br>
<span style="font-size:18px">You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>TotalAnimal()</strong>&nbsp;which takes N as input parameter and returns the total number of animals at the end of <strong>N </strong>years modulo <strong>10<sup>9</sup>&nbsp;+ 7</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(log<sub>2</sub>N)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>18</sup></span></p>
</div>