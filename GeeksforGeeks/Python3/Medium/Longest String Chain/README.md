# Longest String Chain
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array of&nbsp;<code>words</code>&nbsp;where each word consists of lowercase English letters.</span></p>

<p><span style="font-size:18px"><code>word<sub>A</sub></code>&nbsp;is a&nbsp;<strong>predecessor</strong>&nbsp;of&nbsp;<code>word<sub>B</sub></code>&nbsp;if and only if we can insert&nbsp;<strong>exactly one</strong>&nbsp;letter anywhere in&nbsp;<code>word<sub>A</sub></code>&nbsp;<strong>without changing the order of the other characters</strong>&nbsp;to make it equal to&nbsp;<code>word<sub>B</sub></code>.</span></p>

<ul>
	<li><span style="font-size:18px">For example,&nbsp;<code>"abc"</code>&nbsp;is a&nbsp;<strong>predecessor</strong>&nbsp;of&nbsp;<code>"ab<u>a</u>c"</code>, while&nbsp;<code>"cba"</code>&nbsp;is not a&nbsp;<strong>predecessor</strong>&nbsp;of&nbsp;<code>"bcad"</code>.</span></li>
</ul>

<p><span style="font-size:18px">A&nbsp;<strong>word chain</strong><em>&nbsp;</em>is a sequence of words&nbsp;<code>[word<sub>1</sub>, word<sub>2</sub>, ..., word<sub>k</sub>]</code>&nbsp;with&nbsp;<code>k &gt;= 1</code>, where&nbsp;<code>word<sub>1</sub></code>&nbsp;is a&nbsp;<strong>predecessor</strong>&nbsp;of&nbsp;<code>word<sub>2</sub></code>,&nbsp;<code>word<sub>2</sub></code>&nbsp;is a&nbsp;<strong>predecessor</strong>&nbsp;of&nbsp;<code>word<sub>3</sub></code>, and so on. A single word is trivially a&nbsp;<strong>word chain</strong>&nbsp;with&nbsp;<code>k == 1</code>.</span></p>

<p><span style="font-size:18px">Return&nbsp;the&nbsp;<strong>length</strong>&nbsp;of the&nbsp;<strong>longest possible word chain</strong>&nbsp;with words chosen from the given list of&nbsp;<code>words</code>.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 6
words = ["a","b","ba","bca","bda","bdca"]
<strong>Output:</strong>
4
<strong>Explanation:</strong>
One of the longest word chains is ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"].</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 2
words = ["abcd","dbqca"]
<strong>Output:
</strong>1
<strong>Explanation:</strong>
The trivial word chain ["abcd"] is one of the longest word chains.</span></pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function <strong>longestChain()&nbsp;</strong>which takes integer <strong>n </strong>and an<strong>&nbsp;</strong>array of<strong> words</strong>&nbsp;and returns the size of longest possible word chain.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O( n * n * L),where L&nbsp;is the length of the longest string in the words.</span><br>
<span style="font-size:18px"><strong>Expected Space Complexity</strong>: O(n)</span></p>

<p><strong><span style="font-size:18px">Constraint:</span></strong><br>
<span style="font-size:18px">1 &lt;= n &lt;= 1000<br>
1 &lt;= words[i].length &lt;= 16</span><br>
&nbsp;<span style="font-size:18px">words[i] only consists of lowercase English letters.</span></p>
</div>