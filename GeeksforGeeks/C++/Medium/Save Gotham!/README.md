# Save Gotham!
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Gotham has been attacked by Joker . Bruce Wayne has deployed an automatic machine gun at each tower of Gotham.<br>
All the towers in Gotham are in a straight line.<br>
You are given no of towers 'n' followed by the height of 'n' towers.<br>
For every tower(p), find the height of the closest tower (towards the right), greater than the height of the tower(p).<br>
Now, the Print sum of all such heights (mod 1000000001).</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> If for a tower(k), no such tower exists then take its height as 0.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>â€‹Input :</strong> arr[]= {112, 133, 161, 311, 122, 
                    512, 1212, 0, 19212}
<strong>Output :</strong> 41265
<strong>Explanation:</strong>
nextgreater(112) : 133
nextgreater(133) : 161
nextgreater(161) : 311
nextgreater(311) : 512
nextgreater(122) : 512
nextgreater(512) : 1212
nextgreater(1212) : 19212
nextgreater(0) : 19212
nextgreater(19212) : 0
add = 133+161+311+512+512+1212+19212+19212+0 
add = 41265.</span></pre>

<p><br>
<span style="font-size:18px"><strong>â€‹Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[] = {5, 9, 7, 6} <strong>
Output :</strong>  9

</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>save_gotham()</strong> that takes an array <strong>(arr)</strong>, sizeOfArray <strong>(n)</strong>, and return the sum of next greater element of every element. The driver code takes care of the printing.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
0 ≤ A[i] ≤ 10<sup>4</sup></span></p>
</div>