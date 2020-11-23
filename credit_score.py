price = 1000000

scores = {"good_credit":(10/100* price),"bad_credit":(10/100* price )}

awesome_credit = price - scores["good_credit"]
poor_credit = price - scores["bad_credit"]

if awesome_credit:
  print(f'Good Credit Final Price: ${price - scores["good_credit"]}')
elif poor_credit:
  print(f'Poor Credit Final Price: ${price - scores["bad_credit"]}')
