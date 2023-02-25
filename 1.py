def purchase_product(product_type,price,mobile_brand):
    if product_type == 'mobile':
        if mobile_brand == 'apple':
            discount=10
            price=price - 0.10*price
            return(price)
        else:
            discount = 5
            price=price - 0.05*price
            return(price)
    else:
        price = price + 0.02 * price
        return(price)


x=purchase_product('mobile',98000,'apple')
print(x)
