# Trie | (Insert and Search)
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Trie is an efficient information retrieval data structure. Use this data structure to store Strings and search strings. Your task is to use TRIE data structure and search the given string A. If found print 1 else 0.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">N = 8
key[] = {the,a,there,answer,any,by,
&nbsp;        bye,their}
search = the
<strong>Output: </strong>1<strong>
Explanation: </strong>the is present in the given
string "the a there answer any by bye
their"</span>
</pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">N = 8
key[] = {the,a,there,answer,any,by,
&nbsp;        bye,their}
search = geeks
<strong>Output: </strong>0<strong>
Explanation: </strong>geeks is not present in the
given string "the a there answer any by
bye their"</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Complete <strong>insert</strong> and <strong>search</strong> function and return <strong>true</strong>&nbsp;if key is present in the formed trie else <strong>false</strong> in the search function. (In case of true, 1 is printed and false, 0 is printed by the driver's code.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(M+|search|).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(M).<br>
M = sum of the&nbsp;length of all strings which is&nbsp;present in the key[]&nbsp;</span></p>

<p><span style="font-size:18px">|search| denotes the length of the string search.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>4</sup><br>
1 &lt;= |input strings|, |A| &lt;= 100</span></p>
</div>