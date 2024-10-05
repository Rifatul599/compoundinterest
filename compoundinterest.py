def interest(principle,rate,time):
    A = principle*(1+rate/100)**time
    ci = principle-A
    return ci
print(interest(100,10,2))