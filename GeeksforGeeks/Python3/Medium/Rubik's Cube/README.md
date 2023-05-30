# Rubik's Cube
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Representation of a Rubik's Cube:</span></p>

<p><span style="font-size:18px">Yellow face is&nbsp;<em>Up</em></span></p>

<p><span style="font-size:18px">Orange face is&nbsp;<em>Front</em></span></p>

<p><span style="font-size:18px">Green face is&nbsp;<em>Left</em></span></p>

<p><span style="font-size:18px">Blue face is&nbsp;<em>Right</em></span></p>

<p><span style="font-size:18px">Red face is&nbsp;<em>Back</em></span></p>

<p><span style="font-size:18px">White face is&nbsp;<em>Down</em></span></p>

<p><span style="font-size:18px"><img alt="" src="https://contribute.geeksforgeeks.org/wp-content/uploads/new__.png" style="height:334px; width:469px"></span></p>

<p><span style="font-size:18px">Since the center pieces are fixed, any face rotation wont changes the central pieces.</span></p>

<p><span style="font-size:18px">Now lets take a look at the nomenclature of Rubik's Cube moves:</span></p>

<p><span style="font-size:18px">R= clockwise&nbsp;90âˆ˜ rotation of right face.</span></p>

<p><span style="font-size:18px">Ri=anti-clockwise&nbsp;90âˆ˜&nbsp;rotation of right face.</span></p>

<p><span style="font-size:18px">Similarly rest of the moves are illustrated below:</span></p>

<p><span style="font-size:18px">Now you will be given the description of a scrambled Rubik's Cube, your task is to print the description of cube&nbsp;after <strong>N</strong> given moves.</span></p>

<p><span style="font-size:18px">For eg, if the given cube is:</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><img alt="" src="https://contribute.geeksforgeeks.org/wp-content/uploads/rubix-top.jpg"></span></p>

<p><span style="font-size:18px">It will be represented as following:</span></p>

<div><span style="font-size:18px">UP<br>
GWYWYYRWW<br>
FRONT<br>
GGRBORYYY<br>
LEFT<br>
YOWRGOOOB<br>
RIGHT<br>
BGRGBBBOO<br>
BACK<br>
GROWRBBRG<br>
DOWN<br>
RBOYWGWYW</span></div>

<p><span style="font-size:18px">Let's say we apply the following moves to the cube:</span></p>

<p><span style="font-size:18px">B B</span></p>

<p><span style="font-size:18px">The move will rotate back face&nbsp;180âˆ˜&nbsp;clockwise, now the cube is:</span></p>

<p><span style="font-size:18px"><img alt="" src="https://contribute.geeksforgeeks.org/wp-content/uploads/rubix-bottom.jpg" style="height:321px; width:400px"></span></p>

<p><span style="font-size:18px">And its description will be:</span></p>

<p><span style="font-size:18px">UP<br>
WYWWYYRWW<br>
FRONT<br>
GGRBORYYY<br>
LEFT<br>
OOWBGOROB<br>
RIGHT<br>
BGOGBRBOY<br>
BACK<br>
GRBBRWORG<br>
DOWN<br>
RBOYWGYWG</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
UP
GWYWYYRWW
FRONT
GGRBORYYY
LEFT
YOWRGOOOB
RIGHT
BGRGBBBOO
BACK
GROWRBBRG
DOWN
RBOYWGWYW
2
R R

<strong>Output:</strong>
UP
GWOWYGRWW
FRONT
GGBBOWYYG
LEFT
YOWRGOOOB
RIGHT
OOBBBGRGB
BACK
YRORRBRRG
DOWN
RBYYWYWYW</span></pre>

<p>&nbsp;</p>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>newFormation()</strong>&nbsp;which takes the string array <strong>present[]</strong>, which is of size <strong>12</strong> containing the faces and the face configurations, string array <strong>move[]</strong> and its size <strong>N</strong><strong> </strong>as inputs and returns the vector of strings containing 12 lines, showing the final configuration of the cube as shown in example.<br>
<strong>Note:</strong> faces must&nbsp;always come in the order shown in example above ie {"UP","FRONT","LEFT","RIGHT","BACK","DOWN"}.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> Constant</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ <strong>N</strong> ≤ 50</span></p>
</div>