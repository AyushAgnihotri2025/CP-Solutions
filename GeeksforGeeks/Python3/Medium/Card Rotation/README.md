# Card Rotation
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a sorted deck of cards numbered 1 to N.</span></p>

<p><span style="font-size:18px">1) We pick up 1 card and put it on the back of the deck.</span></p>

<p><span style="font-size:18px">2) Now, we pick up another card, it turns out to be card number 1, we put it outside the deck.</span></p>

<p><span style="font-size:18px">3) Now we pick up 2 cards and put it on the back of the deck.</span></p>

<p><span style="font-size:18px">4) Now, we pick up another card and it turns out to be card numbered 2, we put it outside the deck. ...</span></p>

<p><span style="font-size:18px">We perform this step until the last card.<br>
<br>
If such an arrangement of decks is possible, output the arrangement, if it is not possible for a particular value of N&nbsp;then output -1.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
N = 4
<strong>Output:</strong>&nbsp;2 1 4 3
<strong>Explanation</strong>:
We initially have [2&nbsp;1&nbsp;4&nbsp;3]
In Step1, we move&nbsp;the first card to the end. 
Deck now is: [1 4 3 2]
In Step2, we get 1. Hence we remove it. Deck 
now is: [4 3 2]
In Step3, we move the 2 front cards ony by one&nbsp;
to the end  ([4 3 2] -&gt; [3 2 4] -&gt; [2 4 3]).
Deck now is: [2 4&nbsp;3]
In Step4, we get 2. Hence we remove it. Deck 
now is: [4&nbsp;3]
In Step5, the following sequence follows: 
[4 3] -&gt; [3 4] -&gt; [4 3] -&gt; [3 4]. Deck now 
is: [3 4]
In Step6, we get 3. Hence we remove it. Deck 
now is: [4] Finally, we're left with a single 
card and thus, we stop.&nbsp;</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 5
<strong>Output: </strong>3 1 4 5 2
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>rotation()</strong>&nbsp;which takes the integer N as input parameters and returns If such arrangement of decks is possible, return the arrangement, if it is not possible for a particular value of n then return -1.</span></p>

<p><br>
<br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N^2)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&nbsp;≤ N&nbsp;≤ 1000</span></p>
</div>