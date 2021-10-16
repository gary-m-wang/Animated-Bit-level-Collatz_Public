# Animated-Bit-level-Collatz_Public

[//]: # (Video Image References)

[video1]: https://www.youtube.com/watch?v=094y1Z2wpJg "The Simplest Math Problem No One Can Solve - Collatz Conjecture"
[image1]: https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/Traditional-line-plot-sequence_odd_terms.png "Traditional line plot - sequence_odd_terms"
[image2]: https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/Binary-bits-static-image-sequence_odd_terms.png "Binary bits static image - sequence_odd_terms"
[image3]: https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/animated_image_start_n_at_27.gif "Animated image - start n at 27"

**README**

[Ref video1] (https://www.youtube.com/watch?v=094y1Z2wpJg) "The Simplest Math Problem No One Can Solve - Collatz Conjecture"

![Ref video1][video1]

 - 2021-08-11
Gary Wang posts comment

```
I would like to see a visualization using binary register representation.
Nice aspect is that all of the divide-by-2 become shifting or dropping zeros at the least-significant-bit end.
3n+1 operations will look something like bits 'evolving' in the game of life.
```

 - 2021-08-12
Ruinenlust replied to Gary Wang's comment

```Except cellular automata depend on local rules - factorisation of integers is, sadly, global```

 - 2021-08-14
Jason Jacoby replied to Gary Wang's comment

```This whole thing reminds me of backwards binary```

 - 2021-08-15 to 2021-08-31
Gary Wang replied to Gary Wang's comment

```
Thanks to feedback from my brother Mark, I realize I better clarify.
I missed conveying directly my distinct premise and perspective,
because my focus is not on the usual algorithm to calculate the numerical sequence.
If I should begin with the end in mind, then the objective is an image display
animating the 'motion' of 1 bits on beackground of 0 bits
(so as to ignore the 0's being non-interesting).
Python is good choice for coding because of readily available package to plot and show image.
Simulation is to illustrate at bit-level for visualization.
I can write a short program description.
```

```
Animation is in work, so should get to see soon.
Without watching it in action, may not make sense to share my Python code already done to calculate the numerical sequence.
I purposely rearranged an alternative in the math steps - I suppose I could open up for everyone to guess why in reading
my brief description of the program.

Implement by an inner loop nested inside an outer loop.
The inner loop is to repeat, while n is even, calculating (n /= 2) until n becomes odd.
Then with n being odd, execute four math steps:
1. (n -= 1)
2. (n /= 2)
3. (n *= 3)
4. (n += 2)
All of the above are inside the outer loop which can repeat indefinitely in principle.
For practicality, make it terminate after some finite number of iterations, or reaching (n == 1), whichever comes first.
```

 - 2021-09-11
Gary Wang posts comment

```
1 month ago, I posted my first comment.
This is a continuation, yet I will post as if new.
Reason is I want to share some code which I wrote in Python
(to be human readable and self-explanatory without much comments) - not sure
if allowed by this site or else I might be deleted.
Reason for code is that we must re-run for each unique starting value,
as the whole point of this problem is the resulting sequence appears erratic.
Reason for Python is the availability of packages to produce animated images.
My desire is to aid & inspire others in looking for patterns graphically.
We came to this YouTube video with the purpose of visualization,
so this is not about size or speed in massive number crunching.
```

 - 2021-09-18 to 2021-09-20
Gary Wang replied to Gary Wang's comment

```
Code fragment 1 looks somewhat standard like how others would implement looping to calculate the sequence.
I differ in putting all the focus on odd numbers.
Any even number gets the divide-by-2 treatment with an inner loop.
Intermediate results of the 4 math steps applied to each odd number are stored as well for producing the animated images
(that will be in code fragment 3).
```

 - 2021-09-25 to 2021-09-27
Gary Wang replied to Gary Wang's comment

```
Code fragment 2 is optional.
This is the reason I am separating it.
The output is a still image of the binary representation like that seen in the YouTube video at 17:34.

(Python has to work with the package matplotlib, so some users may have to modify the environment or the code.)
```

__ End of Posts __

[Ref image1] (https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/Traditional-line-plot-sequence_odd_terms.png) "Traditional line plot - sequence_odd_terms"

![Ref image1][image1]

[Ref image2] (https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/Binary-bits-static-image-sequence_odd_terms.png) "Binary bits static image - sequence_odd_terms"

![Ref image2][image2]

 - 2021-10-02 to 2021-10-04
### Code fragment 3
Code fragment 3 is long and too complicated to be for human readability.
This is no problem, because that is not necessary (and not the intent, unless you are into such programming).
The computer is the one that has the job of understanding the code to execute and thereby produce the animated image as output.
People are supposed to simply watch the resulting graphics and visualize.

Python syntax does care about indentations by space characters, which finally convinced me the difficulty with posting comments via YouTube.
Instead, let me use GitHub.

[Ref image3] (https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/animated_image_start_n_at_27.gif) "Animated image - start n at 27"

![Ref image3][image3]
