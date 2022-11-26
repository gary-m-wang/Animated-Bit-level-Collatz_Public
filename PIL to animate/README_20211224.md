# Animated-Bit-level-Collatz_Public

[//]: # (Video Image References)

[video1]: https://www.youtube.com/watch?v=094y1Z2wpJg "The Simplest Math Problem No One Can Solve - Collatz Conjecture"
[image1]: https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/pil_image_odd_terms_x100.PNG "Static image - sequence_odd_terms start n at 7"
[image2]: https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/pil_text_on_image_odd_terms_x100.PNG "Static text on image - sequence_odd_terms start n at 7"
[image3]: https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/text_off_animated_image_start_n_at_7.gif "Animated image - math steps start n at 7"

**README**

[Ref video1] (https://www.youtube.com/watch?v=094y1Z2wpJg) "The Simplest Math Problem No One Can Solve - Collatz Conjecture"

![Ref video1][video1]

Implement by an inner loop nested inside an outer loop.
The inner loop is to repeat, while n is even, calculating (n /= 2) until n becomes odd.
Then with n being odd, execute four math steps:
```
1. (n -= 1)
2. (n /= 2)
3. (n *= 3)
4. (n += 2)
```
All of the above are inside the outer loop which can repeat indefinitely in principle.
For practicality, make it terminate after some finite number of iterations, or reaching (n == 1), whichever comes first.

[Ref image1] (https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/pil_image_odd_terms_x100.PNG) "Static image - sequence_odd_terms start n at 7"

![Ref image1][image1]

[Ref image2] (https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/pil_text_on_image_odd_terms_x100.PNG) "Static text on image - sequence_odd_terms start n at 7"

![Ref image2][image2]

[Ref image3] (https://github.com/gary-m-wang/Animated-Bit-level-Collatz_Public/blob/main/text_off_animated_image_start_n_at_7.gif) "Animated image - math steps start n at 7"

![Ref image3][image3]
