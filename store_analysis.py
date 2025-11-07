"""
Store Data Analysis Script
Loads and analyzes store sales data using Pandas and creates visualizations with Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data(file_path):
    """
    Load CSV data into a Pandas DataFrame
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        DataFrame with the loaded data
    """
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df


def calculate_metrics(df):
    """
    Calculate key metrics from the sales data
    
    Args:
        df: DataFrame with sales data
        
    Returns:
        Dictionary with calculated metrics
    """
    metrics = {
        'total_revenue': df['revenue'].sum(),
        'total_units_sold': df['units_sold'].sum(),
        'average_rating': df['rating'].mean(),
        'total_reviews': df['customer_reviews'].sum(),
        'revenue_by_category': df.groupby('category')['revenue'].sum().to_dict(),
        'units_by_category': df.groupby('category')['units_sold'].sum().to_dict(),
        'top_products': df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(5).to_dict()
    }
    return metrics


def create_revenue_visualization(df, output_dir='visualizations'):
    """
    Create revenue trend visualization
    
    Args:
        df: DataFrame with sales data
        output_dir: Directory to save the visualization
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Daily revenue trend
    daily_revenue = df.groupby('date')['revenue'].sum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_revenue.index, daily_revenue.values, marker='o', linewidth=2, markersize=6)
    plt.title('Daily Revenue Trend', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/revenue_trend.png', dpi=300)
    plt.close()
    
    print(f"Revenue trend visualization saved to {output_dir}/revenue_trend.png")


def create_category_visualization(df, output_dir='visualizations'):
    """
    Create category-based visualizations
    
    Args:
        df: DataFrame with sales data
        output_dir: Directory to save the visualization
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Revenue by category
    category_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Bar chart
    ax1.bar(category_revenue.index, category_revenue.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax1.set_title('Revenue by Category', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Category', fontsize=12)
    ax1.set_ylabel('Revenue ($)', fontsize=12)
    ax1.grid(axis='y', alpha=0.3)
    
    # Pie chart
    ax2.pie(category_revenue.values, labels=category_revenue.index, autopct='%1.1f%%', 
            startangle=90, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax2.set_title('Revenue Distribution by Category', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/category_analysis.png', dpi=300)
    plt.close()
    
    print(f"Category analysis visualization saved to {output_dir}/category_analysis.png")


def create_review_visualization(df, output_dir='visualizations'):
    """
    Create review and rating visualizations
    
    Args:
        df: DataFrame with sales data
        output_dir: Directory to save the visualization
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Average rating by category
    category_ratings = df.groupby('category')['rating'].mean().sort_values(ascending=False)
    
    # Total reviews by product
    product_reviews = df.groupby('product')['customer_reviews'].sum().sort_values(ascending=False).head(8)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Average rating by category
    ax1.barh(category_ratings.index, category_ratings.values, color='#2ca02c')
    ax1.set_title('Average Rating by Category', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Average Rating', fontsize=12)
    ax1.set_ylabel('Category', fontsize=12)
    ax1.set_xlim(0, 5)
    ax1.grid(axis='x', alpha=0.3)
    
    # Total reviews by product
    ax2.barh(product_reviews.index, product_reviews.values, color='#ff7f0e')
    ax2.set_title('Total Customer Reviews by Product', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Number of Reviews', fontsize=12)
    ax2.set_ylabel('Product', fontsize=12)
    ax2.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/review_analysis.png', dpi=300)
    plt.close()
    
    print(f"Review analysis visualization saved to {output_dir}/review_analysis.png")


def create_sales_performance_visualization(df, output_dir='visualizations'):
    """
    Create sales performance visualizations
    
    Args:
        df: DataFrame with sales data
        output_dir: Directory to save the visualization
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Top 5 products by revenue
    top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(5)
    
    # Units sold by category over time
    category_daily = df.groupby(['date', 'category'])['units_sold'].sum().unstack(fill_value=0)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Top products by revenue
    ax1.barh(top_products.index, top_products.values, color='#9467bd')
    ax1.set_title('Top 5 Products by Revenue', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Revenue ($)', fontsize=12)
    ax1.set_ylabel('Product', fontsize=12)
    ax1.grid(axis='x', alpha=0.3)
    
    # Units sold by category over time
    for category in category_daily.columns:
        ax2.plot(category_daily.index, category_daily[category], marker='o', label=category, linewidth=2)
    ax2.set_title('Units Sold by Category Over Time', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Units Sold', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sales_performance.png', dpi=300)
    plt.close()
    
    print(f"Sales performance visualization saved to {output_dir}/sales_performance.png")


def print_metrics_summary(metrics):
    """
    Print a summary of calculated metrics
    
    Args:
        metrics: Dictionary with calculated metrics
    """
    print("\n" + "="*60)
    print("STORE METRICS SUMMARY")
    print("="*60)
    print(f"\nTotal Revenue: ${metrics['total_revenue']:,.2f}")
    print(f"Total Units Sold: {metrics['total_units_sold']:,}")
    print(f"Average Rating: {metrics['average_rating']:.2f}/5.0")
    print(f"Total Customer Reviews: {metrics['total_reviews']:,}")
    
    print("\n" + "-"*60)
    print("Revenue by Category:")
    print("-"*60)
    for category, revenue in metrics['revenue_by_category'].items():
        print(f"  {category}: ${revenue:,.2f}")
    
    print("\n" + "-"*60)
    print("Units Sold by Category:")
    print("-"*60)
    for category, units in metrics['units_by_category'].items():
        print(f"  {category}: {units:,} units")
    
    print("\n" + "-"*60)
    print("Top 5 Products by Revenue:")
    print("-"*60)
    for i, (product, revenue) in enumerate(metrics['top_products'].items(), 1):
        print(f"  {i}. {product}: ${revenue:,.2f}")
    
    print("\n" + "="*60)


def main():
    """
    Main function to run the complete analysis
    """
    # Load data
    print("Loading store data...")
    df = load_data('store_data.csv')
    print(f"Loaded {len(df)} records")
    
    # Calculate metrics
    print("\nCalculating metrics...")
    metrics = calculate_metrics(df)
    
    # Print summary
    print_metrics_summary(metrics)
    
    # Create visualizations
    print("\nCreating visualizations...")
    create_revenue_visualization(df)
    create_category_visualization(df)
    create_review_visualization(df)
    create_sales_performance_visualization(df)
    
    print("\n" + "="*60)
    print("Analysis complete! Check the 'visualizations' folder for charts.")
    print("="*60)


if __name__ == "__main__":
    main()
