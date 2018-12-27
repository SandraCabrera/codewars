
def loose_change(cents):
    if cents >= 25:
        quarters= cents / 25
        cents= cents % 25
    else:
        quarters = 0
    if cents >= 10:
        dimes= cents / 10
        cents= cents % 10
    else:
        dimes = 0
    if cents >= 5:
        nickels= cents / 5
        cents= cents % 5
    else:
        nickles = 0
    return quarters, dimes, nickels, cents













#casos test

test.assert_equals(loose_change(29), {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
test.assert_equals(loose_change(91), {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
test.assert_equals(loose_change(0), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(-2), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
