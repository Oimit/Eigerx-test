
# Question 1:
def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0 # Total errors.
    products_dict = dict(zip(products, productPrices)) # Mapping the products to the real prices.
    for i in range(len(productSold)): # iterating over the productSold.
        expected_price = products_dict[productSold[i]] # The expected price od each product.
        if soldPrice[i] != expected_price: # Check if the soldPrice of a product has been sold with the expected price.
            errors += 1 # if not, its an error.
    return errors

print(priceCheck(
    products=['rice', 'sugar', 'wheat', 'cheese'],
    productPrices=[16.89, 56.92, 20.89, 345.99],
    productSold=['rice', 'cheese'],
    soldPrice=[18.99, 400.89]
))



# Question 3:
def sum_of_digits(n):
    if n == 0: # Base case.
        return 0
    return n % 10 + sum_of_digits(n // 10) # adding the last digit of n to the sum of the remaining digits.


print(sum_of_digits(2347623))

# Question 4:
def count_max_elements(stream, maximum=None, count=0):
    if stream: # check if the stream isn't empty.
        current = stream.pop(0) # takes the first element from the stream.
        if current == 0: # end of the stream.
            print(f"({maximum}; {count})")
        elif maximum is None or current > maximum: # check if current > maximum
            maximum = current # the new maximum.
            count = 1
        elif current == maximum:
            count += 1 # increase the count.
        count_max_elements(stream, maximum, count) # passing the remaining stream.

count_max_elements([1, 5, 42, -376, 5, 19, 5, 3, 42, 2, 0])
