A = [{
    "Coffee" : "Americano",
    "Price" : 2500
}, {
    "Coffee" : "Latte",
    "Price" : 3800
}, {
    "Coffee" : "Cappuccino",
    "Price" : 4500
}, {
    "Coffee" : "Espresso",
    "Price" : 2000
}]

def price(coffee):
    return coffee["Price"]

print(min(A, key=price))
print(min(A, key = lambda coffee: coffee["Price"]))

print(max(A ,key=price))
print(max(A, key = lambda coffee: coffee["Price"]))

A.sort(key = lambda coffee : coffee['Price'])
print(A)