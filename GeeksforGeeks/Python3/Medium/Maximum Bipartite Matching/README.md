# Maximum Bipartite Matching
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">There are M job applicants and N jobs.&nbsp; Each applicant has a subset of jobs that he/she is interseted in. Each job opening can only accept one applicant and a job applicant can be appointed for only one job. Given a matrix <strong>G </strong>where G(i,j) denotes i<sup>th&nbsp;</sup>applicant is interested in j<sup>th&nbsp;</sup>job. Find an assignment of jobs to applicant in such that as many applicants as possible get jobs.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>G = {{1,1,0,1,1},{0,1,0,0,1},
{1,1,0,1,1}}
<strong>Output: </strong>3
<strong>Explanation: </strong>There is one of the possible
assignment-
First applicant gets the 1st job.
Second applicant gets the 2nd job.
Third applicant gets the 3rd job.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>G = {{1,1},{0,1},{0,1},{0,1},
{0,1},{1,0}}
<strong>Output: </strong>2
<strong>Explanation: </strong>There is one of the possible
assignment-
First applicant gets the 1st job.
Second applicant gets the 2nd job.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read to print anything. Your task is to complete the function&nbsp;<strong>maximumMatch()&nbsp;</strong>which takes matrix G as input parameter and returns the maximum number of applicants who can get the job.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N<sup>3</sup>)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(N)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N, M ≤ 100</span></p>
</div>