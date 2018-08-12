#conditions..

amt = 1000;

#if a customer is making a bill of morethan 7000 rs.. i should give 1000 discount..
#> - Greateer than 
#< -less than 
#>= greater than or equal
#<= less than or equal 
# != not equal to..
# == equality check

#if

#else

if amt > 7000:
	print "I made more than 7000 and i am eligible for discount"
	amt = amt - 1000
elif amt > 5000:
	print "Amt is not greater than 7000, so u will get 500/- discount"
	amt = amt - 500
elif amt >= 1000:
	print "Amt is not greater than 7000, so u will get 500/- discount"
	amt = amt - 200

print "You need to pay {}".format(amt)







