import math

def minimax( curDepth, node, maxTurn, scores, targetDepth, path):
    if curDepth == targetDepth:
        return scores[node], path
    

    if maxTurn: 
        leftScore, leftPath = minimax(curDepth+1, node*2, False, scores, targetDepth, path+" L " )
        rightScore, rightPath = minimax(curDepth+1, node*2 + 1, False, scores, targetDepth, path+" R " )

        if leftScore > rightScore:
            return leftScore,leftPath
        else:
            return rightScore,rightPath
        
    else: 
        leftScore, leftPath = minimax(curDepth+1, node*2, True, scores, targetDepth, path+" L " )
        rightScore, rightPath = minimax(curDepth+1, node*2 + 1, True, scores, targetDepth, path+" R " )

        if leftScore < rightScore:
            return leftScore,leftPath
        else:
            return rightScore,rightPath
        

score_string=input("Enter the scores: ")
scores=[int(x) for x in score_string.split()]
treeDepth = math.log(len(scores),2)
result, path= minimax(0, 0, True, scores, treeDepth, "")

print("The optimal value is: ", result)
print("The path from the terminal value to root node is: ",path)