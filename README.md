# customer-segmentation

The approach used :

The customer segmentation model was developed using clustering techniques to group customers based on their spending behavior, income, and age. The dataset was first explored through EDA (Exploratory Data Analysis) to understand patterns and trends. K-Means clustering was applied to segment customers into different groups. The model's results were visualized using scatter plots to make the clusters more interpretable. A simple Streamlit-based UI was created, allowing users to upload their dataset and receive insights about customer segments.

Challenges faced:

One challenge was determining the optimal number of clusters, which was addressed using the Elbow Method. Another challenge was ensuring that the clustering results were meaningful and interpretable for businesses. Handling different datasets dynamically in the Streamlit app also required careful feature selection and preprocessing.

Model performance & improvements:

The model successfully segmented customers into distinct groups based on their spending and demographics. The insights generated can help businesses tailor their marketing strategies. Future improvements could include testing other clustering algorithms like DBSCAN or hierarchical clustering and integrating more advanced techniques for automated feature selection to make the model more flexible for different datasets.

Check it out on:
https://huggingface.co/spaces/usaid123/customer-segments-app
