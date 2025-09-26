# inbuilt functions 
scores = [90,80,90]
sum_scores = 0
for score in scores:
    sum_scores = sum_scores + score
print("Total Score: ", sum_scores)    
    
# inbuilt functions : rather we write, we use already defined functions / utilities
scores = [90,80,90,70]
sum_scores = sum(scores)
print(sum_scores)
print(len(scores))
avg_score = sum_scores/len(scores)
print(avg_score)
max_value = max(scores)
print(max_value)
min_value = min(scores)
print(min_value)