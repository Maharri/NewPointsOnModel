# NewPointsOnModel
Experiment to 1) see if additional points on a model change the model and 2) see how easy it is to program using LLMs

I asked the first part on Cross Validated: <a href="https://stats.stackexchange.com/questions/646307/adding-a-point-on-the-ls-line-to-the-training-set">Adding a point on the LS line to the training set</a>

There are two parts to this. First the statistical question. I wondered naively if given a set of points in the plane, if an OLS regression line is computed (minimizing MSE), and you create a new point on that line, does that augmented set of points have a different model or is it the exact same model.
Intuitively it could go either way - Adding a point from the model shouldn't change the model at all - if you add a consequence of a logical theory to the assumptions, you don't change the theory. But, for OLS, the math (adding a row to a matrix and then expecting to manipulate it preserving the minimization of MSE to get the same model would seem quite a mess and therefore implausible.
To cut to the chase, there's no change in model - you can add as many points on the minimal surface and it doesn't change the minimal surface. The justification by whuber in their Cross Validation answer is that the MSE is the sum of errors for each point. Since the new point, by design, has zero error, then the new error would be the same as the error of the original set. Since the error is unique (as usual assuming general position of points), the model hasn't changed.
The python files just show this also works in practice.
The first file is for 2-d, the second for 3-d (with graphs!).
<p>
  <p></p>
</p>

The second question I wondered about is if I could get an LLM to help me do this. I am an awful Python programmer and I thought if instead of 'programming by Stack Overflow' or spending hours using man pages, that I'd see if ChatGPT could do it for me out of the box.
TLDR Yeah, no, sort of, but what it did do saved a lot of time.
Explanation. Here is the prompt I started with:
<code>
write some self-contained python code that 
1) generates 2-d point cloud of 20 points
2) does ordinary least squares on it
3) displays a graph of the data with the least squares line
4) creates a single point on the line
5) appends that point to the point cloud
6) Does ordinary least squares on this augmented set
7) displays a graph of this data with the new least squares line
</code>

It gave me a full piece of code. When I ran it in a jupyter notebook, nothing displayed. I asked ChatGPT why and it said to do something like it had already done. Throwing up my hands, I executed it again and it gave a syntax error. I asked ChatGPT to fix the error, it changed something and... it worked perfectly.
The code (modulo the tiny syntax error (missing a variable)) was nicely factored, nicely commented (not too much but just enough), had a number of things I didn't think of (setting the random seed to a constant, a reasonable random set of points (a given model wiht a tiny bit of noise), and everything a little function to make it easier to recombine.
3d is what gave me problems. I prompted "Now do this in 3d".
The code was not terribly different, looked like a reasonable generalization, handled plotting a fitting plane really well (I could never have come up with that).
And it 'worked'... it output some values and plotted things nice.
But the values didn't look right. The beta coefficients and the intercept sorta kinda didn't match the plotted graph, but maybe that's the randomness, or maybe the math didn't work out in 3d.
Another TLDR (or three hourse of messing around) the pieces of input didn't get made correctly for how the API for the python linreg function expected. All the matrices and vectors were of the right dimensions, but the columns were mixed up in order. Part of my misunderstanding was not knowing the functions, and always in doubt about whether python is zero based or not (it is!). Printing values is still my poor man's goto for debugging. 
So I'm super impressed with ChatGPT's ability to code. But I can't trust it out of the box and it may have problems with knowing which column does what. 
At one point I was super frustrated and I did try gemini just to see what an alternate LLM might produce. Gemini's code wasn't as cleanly factored, but was a lot shorter and easier to follow. But it didn't work immediately (which is more a problem with me than gemini), so I went back to ChatGPT.
