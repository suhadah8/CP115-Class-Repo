minutes = int(input("enter time in minutes :"))

hours = minutes / 60
remaining_minutes = minutes % 60

print("original minutes : " , minutes)
print(f"converted time : {hours} hours and {remaining_minutes} minutes")