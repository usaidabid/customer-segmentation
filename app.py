import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Title
st.title("Customer Segmentation using K-Means Clustering")

# Upload CSV File
uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])

if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   st.write("### Preview of Uploaded Dataset:")
   st.write(df.head())

   # Select Features
   st.write("### Select Features for Clustering:")
   selected_features = st.multiselect("Choose columns", df.columns)

   if len(selected_features) >= 2:
       df_selected = df[selected_features].dropna()

       # Select Number of Clusters
       k = st.slider("Select number of clusters (K)", min_value=2, max_value=10, value=4)
       kmeans = KMeans(n_clusters=k, random_state=42)
       df_selected["Cluster"] = kmeans.fit_predict(df_selected)

       # Cluster Means
       cluster_means = df_selected.groupby("Cluster").mean()

       # Assigning Labels
       cluster_names = {}
       for i, row in cluster_means.iterrows():
           if row["Spending Score (1-100)"] > 60 and row["Age"] < 35:
               cluster_names[i] = "Young High Spenders"
           elif row["Spending Score (1-100)"] < 40 and row["Annual Income (k$)"] > 60:
               cluster_names[i] = "Rich Low Spenders"
           elif row["Annual Income (k$)"] < 40:
               cluster_names[i] = "Low Income Group"
           else:
               cluster_names[i] = "Average Spenders"

       df_selected["Cluster Name"] = df_selected["Cluster"].map(cluster_names)

       # Show Updated Data
       st.write("### Clustered Data with Labels:")
       st.write(df_selected)

       # Show Cluster Summary
       st.write("### Cluster Insights:")
       for i, name in cluster_names.items():
           st.write(f"**Cluster {i}: {name}** - {len(df_selected[df_selected['Cluster'] == i])} Customers")

       # Visualization
       if len(selected_features) == 2:
           st.write("### Cluster Visualization:")
           fig, ax = plt.subplots()
           scatter = ax.scatter(df_selected.iloc[:, 0], df_selected.iloc[:, 1], c=df_selected["Cluster"], cmap="viridis")
           ax.set_xlabel(selected_features[0])
           ax.set_ylabel(selected_features[1])
           plt.colorbar(scatter)
           st.pyplot(fig)

   else:
       st.warning("Please select at least 2 features for clustering.")
