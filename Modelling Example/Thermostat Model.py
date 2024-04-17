def thermostat(actual, target):
    if actual > target:
        return 1
    else:
        return 0
    
temp_on_or_off = thermostat(19, 23)

print(temp_on_or_off)