# SO-answer-1
Stack Overflow answer to question: https://stackoverflow.com/questions/64962006/literally-started-learning-coding-from-free-sources-and-already-ran-into-issues/64962232#64962232


```
price = 1000000

scores = {"good_credit":(10/100* price),"bad_credit":(10/100* price )}

awesome_credit = price - scores["good_credit"]
poor_credit = price - scores["bad_credit"]

if awesome_credit:
  print(f'Good Credit Final Price: ${price - scores["good_credit"]}')
elif poor_credit:
  print(f'Poor Credit Final Price: ${price - scores["bad_credit"]}') 
  ```
  
  
Personally this is how I would do it, you can't convert a string to a float, in your first variable declaration you have price = "1000000" , any value between double quotes or single quotes is a string, you don't actually need to force it to be a float at all, math preformed on numbers is allowed. You also don't need to round the credit values unless you wanted to.

There is one major flaw in your code and even in the code I sent over, There is no reason to define awesome_credit and poor_credit as true or false, in fact your overwriting the value. The issue is also that because they have values both of them are true. It will always be good credit. Now to fix this, you need to determine what defines good credit or bad credit. In the real world you would be dealing with 2 situations, 1) you are working with something like django and the credit scores would be fetched from a model, or 2) where you are calculating a value for good or bad credit and you have a baseline , above is good below is bad.

Hoped this helped cheers!
