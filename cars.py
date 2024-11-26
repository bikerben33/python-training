cars = ['audi', 'vw', 'bmw', 'ford']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    
car = 'subaru'
print("Is car == 'subaru'? I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false.")
print(car == 'audi')