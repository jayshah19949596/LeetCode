"""

                     i
fir_list = [[0,2],[5,10],[13,23],[24,25]]


              j
sec_list = [[1,5],[8,12],[15,24],[25,26]]


fir_list = [[3, 5]]


              j
sec_list = [[10, 12]]

results = [ [1, 5],  

if second_list[j].start<=first_list[i].end
   find_intersection
elif first_list[i].start<=second_list[j].end
    find_intersection
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        i, j = 0, 0

        results = []
        while i<len(firstList) and j<len(secondList):
            #print(firstList[i][0]<=secondList[j][0]<=firstList[i][1] or secondList[j][0]<=firstList[i][0]<=secondList[j][1])
            if  firstList[i][0]<=secondList[j][0]<=firstList[i][1] or secondList[j][0]<=firstList[i][0]<=secondList[j][1]:
                #find_intersection
                intersection = [max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]
                results.append(intersection)

            if firstList[i][1]<=secondList[j][1]: i += 1
            else: j+=1

        return results 
