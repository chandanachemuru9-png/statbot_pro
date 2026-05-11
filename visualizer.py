import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(df, x_col, y_col):
    fig, ax = plt.subplots()
    sns.barplot(data=df, x=x_col, y=y_col, ax=ax, palette="Blues_d")
    ax.set_title(f"{y_col} by {x_col}")
    plt.xticks(rotation=45)
    return fig

def plot_line(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker='o', color='steelblue')
    ax.set_title(f"{y_col} trend over {x_col}")
    plt.xticks(rotation=45)
    return fig

def plot_pie(df, col):
    fig, ax = plt.subplots()
    df.groupby(col).sum(numeric_only=True).iloc[:, 0].plot.pie(
        autopct="%1.1f%%", ax=ax, colors=sns.color_palette("Blues")
    )
    ax.set_title(f"{col} Distribution")
    ax.set_ylabel("")
    return fig

def plot_scatter(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.scatter(df[x_col], df[y_col], color='steelblue', s=100)
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    return fig

def plot_histogram(df, col):
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=10, color='steelblue', edgecolor='white')
    ax.set_title(f"{col} Distribution")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    return fig