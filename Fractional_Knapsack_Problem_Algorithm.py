class Knasack:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
def Fractional_knapsack(W,arr):
    arr.sort(key=lambda x :(x.profit / x.weight) , reverse=True)
    final_value=0.0
    for i in arr:
        if i.weight <= W:
            W-=i.weight
            final_value +=i.profit
        else:
            final_value += i.profit *W/ i.weight
            break
    return final_value
if __name__ == "__main__":
    w=50
    arr=[Knasack(60,10),Knasack(100,20),Knasack(120,30)]
    max=Fractional_knapsack(w,arr)
    print(max)
