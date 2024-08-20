# -*- coding: utf-8 -*-
"""Report _on_markering_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RZW-dfiykSdo-bPWUoTzMwtuoy5ZJRRL

# Markering Campaign Analysis Report

## Introduction
This report provides an analysis of marketing campaign data to identify factors contributing to successful campaigns. Key aspects analyzed include budget, device type, geographic region, ROI, and target audience.

## Preparing the data for analysis
"""

#uploading the dataset
import pandas as pd
df = pd.read_csv('marketing_campaign_data.csv')
print(df.head())

# Checking for nulls and relevant data type!
print(df.info())
print(df.isnull().sum())

"""Checking data types and missing values!

"""

#converting columns to strings to for accurate calculations.
df['Cost'] = df['Cost'].astype(str).replace({'\$': '', ',': ''}, regex=True).astype(float)
df['Revenue'] = df['Revenue'].astype(str).replace({'\$': '', ',': ''}, regex=True).astype(float)

#checking the data
print(df[['Campaign ID', 'Cost', 'Revenue', 'ROI', 'Cost per acquisition']].head())

#calculating summary metrics
summary_metrics = df[['Impressions', 'Clicks', 'Conversions', 'Cost', 'Revenue', 'Cost per acquisition', ]].describe()
print("Summary Metrics:\n", summary_metrics)

"""## Analyzing the data and finding insights

## Campaign type performance
We analyzed the performance of different campaign types.
"""

#top 5 campaigns by ROI!
top_campaigns_by_roi = df.sort_values(by='ROI', ascending=False).head(5)
print("\n Top Five Campaigns by ROI:\n", top_campaigns_by_roi[['Campaign ID', 'ROI', 'Revenue', 'Cost']])

#top 5 campaigns by conversions
top_campaigns_by_conversions = df.sort_values(by='Conversions', ascending=False).head(5)
print("\n Top Five Campaigns by Conversions:\n", top_campaigns_by_conversions[['Campaign ID', 'ROI','Revenue', 'Cost']])

#top 5 camapigns by revenue!
top_campaigns_by_revenue = df.sort_values(by='Revenue', ascending=False).head(5)
print("\n Top Five Campaigns by Revenue:\n", top_campaigns_by_revenue[['Campaign ID','Cost', 'ROI', 'Budget']])

"""### Analyzing by segments"""

# Analyzing performance by segment
segment_performance = df.groupby('Target Audience')['ROI'].mean().sort_values(ascending=False)
print("Segment Performance:\n", segment_performance)

"""Targeting Adults resulted in more conversions."""

# Evaluating campaign type performance
campaign_type_performance = df.groupby('Campaign Type')['ROI'].mean().sort_values(ascending=False)
print("Campaign Type Performance:\n", campaign_type_performance)

"""As we can see Email campaign type performed better and yeilded greater ROI."""

# Evaluating ad content performance!
ad_content_performance = df.groupby('Ad Content Type')['ROI'].mean().sort_values(ascending=False)
print("Ad Content Performance:\n", ad_content_performance)

""" Ad Content in form of text resulted in greater ROI. This shows people prefer ad in the form of text rather than in form of any other type."""

# Performance by device type
device_performance = df.groupby('Device Type')['ROI'].mean().sort_values(ascending=False)
print("Device Performance:\n", device_performance)

"""Desktop device type yeilded higher ROI as compared to others, suggesting that desktop users are more likely to convert."""

# Performance by Geographic region!
geographic_performance = df.groupby('Geographic Region')['ROI'].mean().sort_values(ascending=False)
print("Geographic Performance:\n", geographic_performance)

"""Campaign targeting the Oceania region resulted in higher ROI, indicating marketing efforts in Oceania are particularly effective."""

# Analyzing the relationship between Budget and ROI!
import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot Budget vs ROI
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Budget', y='ROI', data=df)
plt.title('Budget vs. ROI')
plt.xlabel('Budget')
plt.ylabel('ROI')
plt.show()

# correlation b/w Budget and ROI
budget_roi_corr = df[['Budget', 'ROI']].corr().iloc[0, 1]
print(f"Correlation between Budget and ROI: {budget_roi_corr:.2f}")

"""It indicates positive but weak relationship, not strong enough to make assumptions and predections."""

# Impressions, Clicks, and Conversions relationship b/w ROI.

plt.figure(figsize=(12, 8))

plt.subplot(1, 3, 1)
sns.scatterplot(x='Impressions', y='ROI', data=df)
plt.xlabel('Impressions')
plt.ylabel('ROI')
plt.title('Impressions vs ROI')

plt.subplot(1, 3, 2)
sns.scatterplot(x='Clicks', y='ROI', data=df)
plt.xlabel('Clicks')
plt.ylabel('ROI')
plt.title('Clicks vs ROI')

plt.subplot(1, 3, 3)
sns.scatterplot(x='Conversions', y='ROI', data=df)
plt.xlabel('Conversions')
plt.ylabel('ROI')
plt.title('Conversions vs ROI')
plt.tight_layout()
plt.show()

# Analyzing impacts of Cost and Cost per acquisition on ROI!
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Cost', y='ROI', data=df)
plt.title('Cost vs. ROI')
plt.xlabel('Cost')
plt.ylabel('ROI')
plt.show

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Cost per acquisition', y='ROI', data=df)
plt.title('Cost per Acquisition vs. ROI')
plt.xlabel('Cost per Acquisition')
plt.ylabel('ROI')
plt.show

# interactive bar plot for Campaign Type performance!
import plotly.express as  px
sns.set(style="whitegrid")
fig = px.bar(campaign_type_performance.reset_index(), x='Campaign Type', y='ROI', labels={'index': 'Campaign Type', 'ROI': 'ROI'}, title='Campaign Type Performance')
fig.show()

# Interactive bar plot for Ad Content type performance!
sns.set(style="whitegrid")
fig = px.bar(ad_content_performance.reset_index(), x='Ad Content Type', y='ROI', labels={'index': 'Ad Content Type', 'ROI': 'ROI'}, title='Ad Content Type Performance')
fig.show()

# Interactive bar plot for target audience
sns.set(style="whitegrid")
fig = px.bar(segment_performance.reset_index(), x='Target Audience', y='ROI', labels={'index': 'Target Audience', 'ROI': 'ROI'}, title='Target Audience Performance')
fig.show()

# Interactive bar plot for Geographic Region!
sns.set(style="whitegrid")
fig = px.bar(geographic_performance.reset_index(), x='Geographic Region', y='ROI', labels={'index': 'Geographic Region', 'ROI': 'ROI'}, title='Geographic Region Performance')
fig.show()

# Interactive bar plot for device type performance!
sns.set(style="whitegrid")
fig = px.bar(device_performance.reset_index(), x='Device Type', y='ROI', labels={'index': 'Device Type', 'ROI': 'ROI'}, title='Device Type Performance')
fig.show()

# bar chart of top five campaigns by ROI!
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x='Campaign ID', y='ROI', data=top_campaigns_by_roi, palette='Blues_d', hue='Campaign ID', dodge=False)
plt.title('Top 5 Campaigns by ROI')
plt.xlabel('Campaign ID')
plt.ylabel('ROI (%)')
plt.legend([],[], frameon=False)
plt.show()

#summarizing the funnel data
funnel_data = df[['Impressions', 'Clicks', 'Conversions']].sum()

# Plotting the conversion funnel
plt.figure(figsize=(10, 6))
sns.barplot(x=funnel_data.index, y=funnel_data.values, palette='Blues_d')
plt.title('Conversion Funnel')
plt.xlabel('Stage')
plt.ylabel('Number of Actions')
plt.show()