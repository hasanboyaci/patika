# Insertion Sort
www.patika.dev 
## Soru 1
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2]<br>
Dizinin en başındaki sayı rootdur. Bu dizide root 7'dir.<br>
5 rootun solundadır.<br>
<pre>
                    7
                /
            5
</pre>
1 rootun ve 5'in solundadır.<br>
<pre>
                    7
                /
            5
        /
    1
</pre>

8 rootun sağındadır.
<pre>
                    7
                /       \
            5               8
        /                       
    1
</pre>

3 rootun ve 5'in solunda , 1'in sağındadır
<pre>
                    7
                /       \
            5               8
        /                       
    1
        \
            3
</pre>
6 rootun solunda ve 5'in sağındadır
<pre>
                    7
                /       \
            5               8
        /       \                    
      1          6
        \
          3
</pre>
0 rootun ve 5'in solunda ,1'in  de solundadır
<pre>
                    7
                /       \
            5              8
        /       \                    
      1          6
    /    \
   0       3
</pre>
9 rootun sağında ve 8'in sağındadır
<pre>
                    7
                /       \
            5              8
        /       \             \       
      1          6             9
    /    \
   0      3
</pre>
4 rootun ve 5'in solunda , 1'in ve 3'ün sağındadır
<pre>
                    7
                /       \
            5              8
        /       \             \       
      1          6             9
    /    \
   0      3
            \
             4
</pre>
2 rootun solunda 5'in solunda 1'in sağında ve 3'ün solundadır
<pre>
                    7
                /       \
            5              8
        /       \             \       
      1          6             9
    /    \
   0      3
        /   \
       2     4
</pre>



