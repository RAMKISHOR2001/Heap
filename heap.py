from math import ceil
class Heap:
    def __init__(self):
        self.array = []
        self.pointer = -1
    
    def insert(self,val):
        self.array.append(val)
        self.pointer += 1
        temp = self.pointer
        while temp > 0:
            idx = ceil(temp/2) - 1
            if self.array[idx] < self.array[temp]:
                self.array[idx],self.array[temp] = self.array[temp],self.array[idx]
            else:
                break
            temp = idx
    
    def deletion(self):
            if not self.array:
                print("No Heap: No Element present")
                return 
            result = self.array[0]
            self.pointer -= 1
            self.array[0] = self.array[-1]
            self.array.pop(-1)
            if self.pointer + 1:
                temp = 0
                while temp < self.pointer:
                    left = 2*temp + 1
                    right = left + 1
                    if (right <= self.pointer) and (self.array[right] > self.array[left]) and (self.array[right] > self.array[temp]):
                        self.array[right], self.array[temp] = self.array[temp], self.array[right]
                        temp = right
                    elif (left <= self.pointer) and (self.array[temp] < self.array[left]):
                        self.array[left], self.array[temp] = self.array[temp], self.array[left]
                        temp = left
                    else:
                        break 
            return result
    

h = Heap()
array = [1,2,3,4,5,7,8]
for i in array:
    h.insert(i)
sorted_array = []

for i in range(len(h.array)):
        a = (h.deletion())
        print(a)
        sorted_array.append(a)
print(sorted_array)



