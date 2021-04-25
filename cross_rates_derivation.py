first_currency=str(input("What is the first currency against USD?\n").upper())


first_currency_rate=float(input("What is the rate of the 1st currency against USD?\n"))
print("The input first currency rate is " + str(first_currency_rate)+ " " + first_currency)


second_currency=str(input("What is the second currency against USD?\n").upper())


second_currency_rate=float(input("What is the rate of the 2nd currency against USD?"))
print("The input second currency rate is " + str(second_currency_rate) + " " + second_currency)


#to convert the base currencies to quote currencies (e.g. 1usd = ... first_currency)
first_currency_quote=1/first_currency_rate

second_currency_quote=1/second_currency_rate


cross_rate_1=second_currency_quote/first_currency_quote
cross_rate_2=first_currency_quote/second_currency_quote

print("1 " + first_currency + " = " + str(cross_rate_1) + " " +second_currency)
print("1 " + second_currency + " = " + str(cross_rate_2) + " " +first_currency)