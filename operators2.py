#this is for lab 2  - operators and experssions

#this is the input data
start_hours =  float(input("Input your start hours in here: "))
start_minutes  =  float(input ("Input your start minutes here: "))
duration =  float(input("input your session duration here in minutes: "))


#find out how many minutes are in the duration
duration_hours = duration // 60
#test step
print ("duration_hours", duration_hours)

#find out how many minutes are remainder from the duration
#duration_minutes = (duration % 60)//60
#test step 2
#print ("duration_minutes ", duration_minutes)

#work out the final minutes
final_minutes = int((duration + start_minutes)) % 60
print ("final minutes= " , final_minutes)

#work out the final hours
total_hours = ((duration + start_minutes) // 60)
print ("total hours ", total_hours)
# + start_hours
final_hours = total_hours + start_hours
print ("final_hours " , final_hours)

#what if it adds to greater than 24 hours?
final_hours_24 = int(final_hours) % 24 
print ("final_hours_24 " , final_hours_24)

#output the final time as minutes and hours
print ("end time = ", final_hours_24, ":" , final_minutes)
