#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The first example is O[n] as it is a linear because of the way the while loop is structured.


b) The second example is O[n * log(n)] because there is a nested for loop inside of the while loop.


c) The last example is O[n] because of the recursive call.

## Exercise II

You could use a form of binary search to find the exact floor.
Take the middle of the total floors and check if the egg breaks,
if it doesnt, check the floor above it, if it breaks there, then
you found your answer. If the egg breaks on the the first floor then
you know it is already too high so you can remove all the floors 
above it, take the middle of your new array and repeat. It the egg
doesn't break on both of the floors then you know it can still go 
higher so you remove all the floors below it and repeat the process.
This solution would have a time complexity of O[log n].
