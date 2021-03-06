import joblib, numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns


def train_test_RMSE(deg_lim: int, X: 'array-like', y: 'array-like'):

    "decide the best polynomial order for transformation of features or predictors"
    "by calculating the root mean squared errors"
    "for both train and test sets of given dataset" 
    "at incremental polynomial order of features"
    
    "return dicts: train_rmse, test_rmse"
    
    from sklearn.preprocessing import PolynomialFeatures
    
    train_rmse, test_rmse = {}, {}  # to store each rmse at different polynomial order
    
    for n in range(1, deg_lim):
        converter = PolynomialFeatures(degree=n, include_bias=False)  #  transform to n degrees
        X_polynomial = converter.fit_transform(X)  # X features has been transformed

        # calculate the separate RMSEs for transformed train and test sets of features
        from sklearn.model_selection import train_test_split
        # split polynomial features, y label into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_polynomial, y, test_size=0.3, random_state=101)
        
        from sklearn.linear_model import LinearRegression
        estimator = LinearRegression()  # instance of linear model to serve as estimator
        estimator.fit(X_train, y_train)  # teach the estimator about dataset perculiarities with train set

        train_pred = estimator.predict(X_train)  # produce label estimates based on input from polynomial features train set
        test_pred = estimator.predict(X_test)  # produce label estimates based on input from polynomial features test set
        
        from sklearn.metrics import mean_squared_error
        import numpy as np
        # calculate root mean squared error for each estimate/predictions
        tr_rmse, te_rmse = np.sqrt(mean_squared_error(y_train, train_pred)), np.sqrt(mean_squared_error(y_test, test_pred))

        # separately store rmse
        train_rmse.setdefault(n, tr_rmse), test_rmse.setdefault(n, te_rmse)
        
    return train_rmse, test_rmse

    
def plot_graph(X_ax: 'array-like', y_ax:'array-like', fig_loc: str, size: tuple=[6, 3], clarity: int=150, ncols=2, plot_type: tuple=['line', 'scatter']):
    '''
    plot a graph for X against y
    consisting of num_sections of sections
    along with corresponding plots
    returns figure storage location - fig_loc
    
    NOTE: length of plot_type and number of columns must match
    return: fig_loc
    '''
    import matplotlib.pyplot as plt, seaborn as sns
    
    fig = plt.figure(figsize=size, dpi=clarity)
    
    # create a dict of section: plot_type
    sects, x = {}, 0
    for j in range(ncols):
        w = 0.6
        axis = fig.add_axes([x, 0, w, 1])
        x += 0.2 + w
        plotter = f"sns.{plot_type[j]}plot(x=X_ax, y=y_ax, ax=axis)"
        eval(plotter)
    
    fig.savefig(fname=fig_loc, bbox_inches='tight')
    
    return fig_loc
    
def ds_modules_importer():
    '''
    import the following data science modules:
    pandas as pd, numpy as np, seaborn as sns
    matplotlib.pyplot as plt
    :return pd, np, plt, sns, train_test_split, PolynomialFeatures, StandardScaler, SCORERS, mean_absolute_error, mean_squared_error
    '''
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import PolynomialFeatures, StandardScaler
    from sklearn.metrics import SCORERS, mean_absolute_error, mean_squared_error

    print('\n\nData Science Modules imported!\n'
          'numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns\n')
    return pd, np, plt, sns, train_test_split, PolynomialFeatures, StandardScaler, SCORERS, mean_absolute_error, mean_squared_error
    
def percentage_missing_data(df: 'DataFrame or Series'):
    '''
    returns the percentage of missing data per column
    input is dataframe or series
    output is the number of missing rows in percentage
    return missing_data, missing_data_perc
    '''
    
    missing_data = df.isna().sum()[df.isna().sum() > 0].sort_values(ascending=False)
    missing_data_perc = np.round(missing_data/df.shape[0] * 100, 2)
    
    #  plot graph to display info
    fig = plt.figure(figsize=(6, 3), dpi=150)
    ax = fig.add_axes(rect=[0, 0, 1, 1])
    sns.barplot(x=missing_data_perc.index, y=missing_data_perc, ax=ax)
    ax.set_xticklabels(labels=missing_data_perc.index, rotation=90)
    
    #  save graph as image
    graph_folder = f'{joblib.os.getcwd()}\\DisplayGraphs'
    joblib.os.makedirs(graph_folder, exist_ok=True)  # folder created
    graph_file = f'{graph_folder}\\plot1.png'
    fig.savefig(fname=graph_file, bbox_inches='tight')
    
    # display saved figure image
    from PIL import Image, ImageShow
    img = Image.open(graph_file)
    ImageShow.show(img)
    
    return missing_data, missing_data_perc