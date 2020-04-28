#seaborn_heatmap_use

import seaborn as sns
dataset=sns.load_dataset('tips')    #Load a dataset from the online repository (requires internet)
dataset.head()                      # Return the first `n` rows , n : int, default 5
plot=sns.heatmap(dataset.corr())    # heatmap() -> Plot rectangular data as a color-encoded matrix.
                                    # corr() -> Compute pairwise correlation of columns, excluding NA/null values
