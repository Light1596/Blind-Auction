import subprocess

print("Welcome to the silent auction")


bidders : dict = {}

available_options : list = ['yes','no']


while True:
        
    name : str = input("Enter your name: ")

    bid : int = int(input("How much do you want to bid: $"))
    
    bidders[name] = bid
    
    response : str = input("is there any other bidder? Enter 'yes' or 'no'.").lower()
    
    while response not in available_options:
        response = input("Please, enter either 'yes' or 'no' to proceed: ")
    
    subprocess.run('clear')
    
    if response == 'no':
        break

#Loop through the dictionary to find the maximum value.
values_dict = list(bidders.values())

maximum_bid : int = max(values_dict)

number_of_times : int = values_dict.count(maximum_bid)

highest_bidder = ''

key_dict : dict[str] = list(bidders.keys())

for key in bidders:
    
    if number_of_times == 1:
        bidders[key] == maximum_bid
        highest_bidder = key
        
    else:
        for i, price in enumerate(values_dict):
            if price == maximum_bid:
               highest_bidder += key_dict[i] 

print(f'The highest bidder is {highest_bidder} with a bid of {max(values_dict)}')
