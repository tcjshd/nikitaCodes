import math

def minimax(curDepth, nodeIndex, scores, maxTurn, targetDepth, path):

    if curDepth == targetDepth:
        return scores[nodeIndex], path
    
    if maxTurn:
        leftscore, leftpath = minimax(curDepth+1, nodeIndex*2, scores, False, targetDepth, path + 'L')
        rightscore, rightpath = minimax(curDepth+1, nodeIndex*2 + 1, scores, False, targetDepth, path + 'R')
        if leftscore > rightscore:
            return leftscore, leftpath
        else:
            return rightscore, rightpath
        
    else:
        leftscore, leftpath = minimax(curDepth+1, nodeIndex*2, scores, True, targetDepth, path + 'L')
        rightscore, rightpath = minimax(curDepth+1, nodeIndex*2 + 1, scores, True, targetDepth, path + 'R')
        if leftscore < rightscore:
            return leftscore, leftpath
        else:
            return rightscore, rightpath
    


scores = []
n = int(input("Enter the number of scores:"))
print("Enter the Scores:")
for i in range(n):
    score = int(input())
    scores.append(score)
treeDepth = math.log(len(scores),2)
result, path = minimax(0, 0, scores, True, treeDepth, "")
print("Optimal Value: ",result)
print("Optimal Path: ",path)
