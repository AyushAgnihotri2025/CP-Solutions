# Maximum point you can obtain from cards
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">There are several cards <strong>arranged in a row</strong>, and each has an associated number of points. The points are given in the integer array<strong> cardPoints </strong>of size <strong>N</strong>.<br>
In one step, you can take&nbsp;one card from beginning or from the end of the row. You have to take <strong>exactly k</strong> cards.<br>
Your score is the sum of the points of the cards you have taken.<br>
Given the integer array <strong>cardPoints</strong>,&nbsp;and its size <strong>N</strong> and the integer<strong> </strong><strong>k</strong>, return the maximum score you can obtain.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 7<br>
k = 3<br>
cardPoints[ ] = {1, 2, 3, 4, 5, 6, 1}<br>
<strong>Output:&nbsp;</strong>12<br>
<strong>Explanation:</strong>&nbsp;After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the cards on the right, giving a final score of 1 + 6 + 5 = 12.</span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 5<br>
k = 5<br>
arr[ ] = {8, 6, 2,&nbsp;4, 5}<br>
<strong>Output:&nbsp;</strong>25<br>
<strong>Explanation:</strong>&nbsp;You have to take all the cards. Your score is the sum of points of all cards.</span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>maxScore()</strong>&nbsp;which takes the&nbsp;array of&nbsp;integers <strong>cardPoints&nbsp;, </strong>an integer&nbsp;<strong>N </strong>and<strong> k&nbsp;</strong>as parameters and returns a maximum score.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><strong>Constraints:</strong><br>
<span style="font-size:18px">1 ≤ N ≤ 10</span><sup>5</sup><br>
<span style="font-size:18px">1 ≤ k&nbsp;≤ N</span><br>
<sup><span style="font-size:18px">1&nbsp;</span></sup><span style="font-size:18px">≤ cardPoints</span><sub>i&nbsp; </sub><span style="font-size:18px">≤ 10<sup>5</sup></span></p>
</div>