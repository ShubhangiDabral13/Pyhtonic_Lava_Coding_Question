def find_pairs(x,y):
    ans= []
    for i in range(len(x)):
        for j in range(len(y)):
            if (pow(x[i],y[j]) > pow(y[j],x[i])):
                ans.append([x[i],y[j]])
    return ans


#Driver function
x = [2,1,6]
y = [1,5]
result = find_pairs(x,y)
print("The pairs are :-")
print(result)
