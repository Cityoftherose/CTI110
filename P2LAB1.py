gas_milage = float(input())
gas_cost = float(input())
per_mile = gas_cost / gas_milage
twenty_mile = per_mile * 20
seventy_five_mile = per_mile * 75
fiveh_mile = per_mile * 500
print(f'{twenty_mile:.2f} {seventy_five_mile:.2f} {fiveh_mile:.2f}')