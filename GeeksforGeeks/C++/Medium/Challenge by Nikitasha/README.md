# Challenge by Nikitasha
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string <strong>S</strong>&nbsp;of length <strong>L&nbsp;</strong>consisting of lower case alphabets only, and two integers <strong>Z</strong> and <strong>K</strong>. Find&nbsp;the maximum value of function <strong>F</strong>&nbsp;of&nbsp;all the substrings of <strong>S</strong>&nbsp;of length <strong>Z</strong>.&nbsp;<br>
Function <strong>F</strong> is calculated in this way:<br>
F= S[0] * K<sup>0</sup>&nbsp;+ S[1] * K<sup>1</sup>&nbsp;+ S[2] * K<sup>2</sup>&nbsp;+ ...... S[Z-1] * K<sup>(Z-1)</sup>.<br>
Consider the Ascii Values of alphabets while computing F:&nbsp;<br>
'a'- 'z'= 97 to 122.<br>
Since value of F may be very large, take its modulo by 1e9+7.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 9 
Z = 6 
K = 10
S = nikitasha</span>
<span style="font-size:18px"><strong>Output:</strong>
12597675</span>
<span style="font-size:18px"><strong>Explanation:</strong>
F(<strong>"nikita"</strong>):
'n'*10<sup>0</sup>+'i'*10<sup>1</sup>+'k'*10<sup>2</sup>+'i'*10<sup>3</sup>+
't'*10<sup>4</sup>+'a'*10<sup>5 </sup>= 10976860
F(<strong>"ikitas"</strong>): 
'i'*10<sup>0</sup>+'k'*10<sup>1</sup>+'i'*10<sup>2</sup>+'t'*10<sup>3</sup>+
'a'*10<sup>4</sup>+'s'*10<sup>5 </sup>= 12597675
F(<strong>"kitash"</strong>):
'k'*10<sup>0</sup>+'i'*10<sup>1</sup>+'t'*10<sup>2</sup>+'a'*10<sup>3</sup> +
's'*10<sup>4</sup>+'h'*10<sup>5</sup> = 11659757
F(<strong>"itasha"</strong>):
'i'*10<sup>0</sup>+'t'*10<sup>1</sup>+'a'*10<sup>2</sup>+'s'*10<sup>3</sup>+
'h'*10<sup>4</sup>+'a'*10<sup>5</sup> = 10865965
12597675 being the maximum.</span>
</pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">N = 5 
Z = 3 
K = 9
S = ecdrh</span>
<strong><span style="font-size:18px">Output:
</span></strong><span style="font-size:18px">10233</span>
<strong><span style="font-size:18px">Explanation:
</span></strong><span style="font-size:18px">F("ecd"): 
'e'*9<sup>0</sup>+'c'*9<sup>1</sup>+'d'*9<sup>2</sup><sup> </sup>= 9092
F("cdr"): 
'c'*9<sup>0</sup>+'d'*9<sup>1</sup>+'r'*9<sup>2</sup><sup> </sup>= 10233 
F("drh"):
'd'*9<sup>0</sup>+'r'*9<sup>1</sup>+'h'*9<sup>2</sup> = 9550
So, the maximum is 10233</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>findMaximum()</strong>&nbsp;which takes the string S, its size N, sub-string length Z and an integer K<strong>&nbsp;</strong>as input parameters&nbsp;and returns the maximum value of function F.<br>
<br>
<strong>Expected Time Complexity: </strong>O(NLog K)<br>
<strong>Expected Space Complexity: </strong>O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=T&lt;=100<br>
1&lt;=N&lt;=1000000<br>
1&lt;=Z&lt;=N<br>
1&lt;=K&lt;=2018</span></p>
</div>