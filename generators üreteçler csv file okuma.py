#generators üreteçler  csv file okuma 
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
firstline=next(list_line)
secondline=next(list_line)
thirthline=next(list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")


def fibonacci():
    x = 1
    y = 0
    z = 0
    while True:
        z = y; #print(z)
        y = x; #print(y)
        x = y + z; #print(x)
        print("--"*30)
        yield x
        if x > 10:
            return
for i in fibonacci():
      print(i)


def fibonacci():
    x = 1
    y = 0
    z = 0
    while not x>10:
        z = y; #print(z)
        y = x; #print(y)
        x = y + z; #print(x)
        print("-"*30)
        yield x
#for i in fibonacci():
#       print(i)       

def fcall():
    yield from fibonacci()

for i in fcall():
    print(i)

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

# an example of a generator that reverses a string.
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]
# For loop to reverse the string
for char in rev_str("hello"):
    print(char)


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
     print(char)

sum(i*i for i in range(10))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))

#unique_words = set(word for line in page  for word in line.split())

#valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))


list("golf"[i] for i in range(len(data)-1, -1, -1))