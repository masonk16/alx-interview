# 0x01. Lockboxes

## Task

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

<ul>
<li>Prototype: ```def canUnlockAll(boxes)```</li>
<li>```boxes``` is a list of lists</li>
<li>A key with the same number as a box opens that box</li>
<li>You can assume all keys will be positive integers</li>
<ul>
<li>There can be keys that do not have boxes</li>
</ul>
<li>The first box ```boxes[0]``` is unlocked</li>
<li>Return ```True``` if all boxes can be opened, else return ```False```</li>
</ul>
