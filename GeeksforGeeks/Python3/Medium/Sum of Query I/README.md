# Sum of Query I
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You need to calculate the following sum over Q queries.:</span></p>

<p><span style="font-size:18px"><img src="https://latex.codecogs.com/gif.latex?\sum_{i=l}^{r}(i-l+1)*(i-l+1)*arr[i]" title="\sum_{i=l}^{r}(i-l+1)*(i-l+1)*arr[i]"></span></p>

<p><strong><span style="font-size:18px">Assume array to be 1-indexed.</span></strong><br>
&nbsp;</p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input: </span></strong><span style="font-size:18px">nums = {2, 3, 4, 5, 1, 6, 7},
Query = {{2, 4}, {2, 6}}
<strong>Output: </strong>{64, 230}
<strong>Explanation: </strong>For the 1st query,
(1<sup>2</sup>&nbsp;* 3 + 2<sup>2</sup>&nbsp;* 4 + 3<sup>2</sup>&nbsp;* 5) = 64.
For the second query
(1<sup>2</sup>&nbsp;* 3 + 2<sup>2</sup>&nbsp;* 4 + 3<sup>2</sup>&nbsp;* 5 + 4<sup>2</sup>&nbsp;* 1 + 5<sup>2</sup>&nbsp;* 6) = 
230</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>FindQuery()&nbsp;</strong>which takes nums and&nbsp;Query as input parameter and returns a list containg the answer modulo&nbsp;<strong>10<sup>9</sup>&nbsp;+ 7</strong>&nbsp;for each query.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 10<sup>5</sup><br>
1 &lt;= nums[i] &lt;= 10<sup>5</sup><br>
1 &lt;= no. of queries &lt;= 10<sup>4</sup></span></p>
</div>