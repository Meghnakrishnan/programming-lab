'''Create a function showEmployee() in such a way that it should accept employee
name, and it’s salary and display both, and if the salary is missing in function call
it should show it as 8000 '''

#function showemployee
def showemployee(name,sal=8000):
    print("name of employee:",name) #print name
    print("salary:",sal)    #print salary
showemployee("jeva") 
showemployee("job",10000)


'''output
name of employee: jeva
salary: 8000
name of employee: job
salary: 10000'''
