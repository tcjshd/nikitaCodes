import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, path):
    if curDepth == targetDepth:
        return scores[nodeIndex], path
    
    if maxTurn:
        leftScore, leftPath = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth, path + "L->")
        rightScore, rightPath = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, path + "R->")
        if leftScore > rightScore:
            return leftScore, leftPath
        else:
            return rightScore, rightPath
    else:
        leftScore, leftPath = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth, path + "L->")
        rightScore, rightPath = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, path + "R->")
        if leftScore < rightScore:
            return leftScore, leftPath
        else:
            return rightScore, rightPath

# Driver code
scores = []
num_scores = int(input("Enter the number of scores: "))
print("Enter the scores:")
for _ in range(num_scores):
    score = int(input())
    scores.append(score)

treeDepth = int(math.log(len(scores), 2))
result, path = minimax(0, 0, True, scores, treeDepth, "")
print("The optimal value is:", result)
print("The path from the terminal value to the root node is:", path)
