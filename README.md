# dissimilarity
Analysis of the impact of dissimilarity in recommendation through rating-based metrics


In the era of digitization, thanks to the spread of the web, it is important to provide personalized advice for each user based on the choices he or she has made in the past, to recommend articles that can be enjoyed with the aim of offering the most satisfactory service possible.
In these recommendation scenarios, similarity measures play a key role because they help to identify similar users or similar articles, so as to assist customers in making decisions, recommending the purchase or use of those articles that match their interests.
In this thesis work, a study is made of the importance and impact of dissimilarity combined with similarity in recommendation systems. In detail, a numerical rating-based similarity metrics are defined from the Pearson Correlation Coefficient, introducing asymmetric similarity and dissimilarity. Subsequently, recommendations are tested using these new coefficients, and we understand how these derived parameters can give more importance to the recommendations.

The recommendation system implemented is user-kNN, but the solution can also be applied to item-kNN.
In the experiment represented here the dataset movielens100k [1] has been used, it has been cleaned from possible items and users with less than 5 evaluations and has been split per user in the percentages 80-20, so to build the train_movielens.csv and the test_movielens.csv.

In chronological order, the first file to start is "user_user.py" which generates a table of user-user similarity based on the metrics chosen from those in the file "metrics.pdf".

The python file "user_user.py" calls the files "metriche.py" and "open_db.py" and builds the table.

Then, to get the top 10 recommendations for each user, you need to start the file "pred.py" which generates a file containing the recommendations.

The evaluations can be found in the file "evaluation.csv". The indexes are:
- EFD_Top10 : expected free discovery
- EPC_Top10 : expected popularity complement
- Gini_Top10 : Gini Diversity in top-N 
- Diversity : Aggregate Diversity in top-N
- Prec_Top10 : Precision in top-N 
- Recall_Top10 : Recall in top-N
- SE_Top10 : Shennon Entropy in top-N
- nDCG_Top10 : Normalized Discounted Comulative Gain in top-N



[1]: Movielens100k https://grouplens.org/datasets/movielens/100k/
