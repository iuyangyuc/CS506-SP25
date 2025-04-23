import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def polynomial_regression_forecast(
    df,
    x_column,
    y_column,
    forecast_years=2,
    test_degrees=[2, 3, 4],
    title="Polynomial Regression Forecast",
    y_label="Value",
    figsize=(12, 8),
    currency_format=True,
    yoy_analysis=True,
    interactive=True
):
    """
    Perform polynomial regression on time series data and forecast future values
    with interactive visualizations.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe containing the time series data
    x_column : str
        The name of the column containing the years/dates
    y_column : str
        The name of the column containing the values to forecast
    forecast_years : int, default=2
        The number of years to forecast into the future
    test_degrees : list, default=[2, 3, 4]
        List of polynomial degrees to test
    title : str, default="Polynomial Regression Forecast"
        The title of the main plot
    y_label : str, default="Value"
        The label for the y-axis
    figsize : tuple, default=(12, 8)
        The size of the figure (for non-interactive plots)
    currency_format : bool, default=True
        Whether to format y-axis as currency (with $ and M for millions)
    yoy_analysis : bool, default=True
        Whether to create a year-over-year percentage change plot
    interactive : bool, default=True
        Whether to create interactive plots (True) or static matplotlib plots (False)

    Returns:
    --------
    dict
        A dictionary containing the results of the analysis:
        - 'best_degree': The best polynomial degree
        - 'best_model': The trained model with the best fit
        - 'predictions': Dictionary of predictions for each model
        - 'future_predictions': Forecasted values
        - 'equation': The equation of the best model
        - 'metrics': Dictionary of metrics (R², MSE) for each model
        - 'fig': The interactive Plotly figure (if interactive=True)
    """
    # Extract data from dataframe
    years = df[x_column].values
    values = df[y_column].values

    # Reshape the data for sklearn
    X = years.reshape(-1, 1)
    y = values

    # Prepare results
    models = {}
    predictions = {}
    metrics = {}
    colors = ['blue', 'green', 'red', 'purple', 'cyan']  # More colors for more degrees

    # Get the last year in the data
    last_year = int(years[-1])

    # Create future years array for predictions
    future_years = np.array(range(int(years[0]), last_year + forecast_years + 1)).reshape(-1, 1)

    # Try different polynomial degrees and find the best fit
    for i, degree in enumerate(test_degrees):
        color_idx = i % len(colors)  # Use modulo to cycle through colors if more degrees than colors

        # Create polynomial features
        poly_features = PolynomialFeatures(degree=degree)
        X_poly = poly_features.fit_transform(X)

        # Fit the model
        model = LinearRegression()
        model.fit(X_poly, y)
        models[degree] = model

        # Make predictions for the training data
        y_pred = model.predict(X_poly)
        predictions[degree] = y_pred

        # Calculate metrics
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        metrics[degree] = {'mse': mse, 'r2': r2}

    # Find the best model based on R² score
    best_degree = max(models.keys(), key=lambda d: metrics[d]['r2'])
    print(f"Best polynomial degree: {best_degree}")

    # Get the best model
    best_model = models[best_degree]

    # Predict future values using the best model
    poly_features = PolynomialFeatures(degree=best_degree)
    poly_features.fit(X)  # Fit the transformer first
    future_years_pred = np.array(range(last_year + 1, last_year + forecast_years + 1)).reshape(-1, 1)
    future_poly = poly_features.transform(future_years_pred)
    future_predictions = best_model.predict(future_poly)

    # Print future predictions
    print("\nPredicted future values:")
    if currency_format:
        for year, pred in zip(future_years_pred.flatten(), future_predictions):
            print(f"Year {int(year)}: ${pred:,.2f}")
    else:
        for year, pred in zip(future_years_pred.flatten(), future_predictions):
            print(f"Year {int(year)}: {pred:,.2f}")

    # Display the best model's coefficients
    best_poly_features = PolynomialFeatures(degree=best_degree)
    X_best_poly = best_poly_features.fit_transform(X)
    coefficients = best_model.coef_
    intercept = best_model.intercept_

    print("\nBest model equation:")
    equation = f"y = {intercept:.2e}"
    for i, coef in enumerate(coefficients[1:], 1):
        equation += f" + {coef:.2e}x^{i}"
    print(equation)

    if interactive:
        # Create interactive plotly figure
        fig = create_interactive_plots(
            years, values, models, future_years, metrics, last_year,
            forecast_years, best_degree, future_years_pred, future_predictions,
            x_column, y_label, title, currency_format, yoy_analysis
        )
        fig.show()

        # Return the results with figure
        return {
            'best_degree': best_degree,
            'best_model': best_model,
            'predictions': predictions,
            'future_predictions': future_predictions,
            'equation': equation,
            'metrics': metrics,
            'fig': fig
        }
    else:
        # Create static matplotlib figure
        create_static_plots(
            years, values, models, future_years, metrics, last_year,
            forecast_years, best_degree, poly_features,
            x_column, y_label, title, figsize, currency_format, yoy_analysis
        )

        # Return the results without figure
        return {
            'best_degree': best_degree,
            'best_model': best_model,
            'predictions': predictions,
            'future_predictions': future_predictions,
            'equation': equation,
            'metrics': metrics
        }

def create_interactive_plots(
    years, values, models, future_years, metrics, last_year,
    forecast_years, best_degree, future_years_pred, future_predictions,
    x_column, y_label, title, currency_format, yoy_analysis
):
    """
    Create interactive Plotly visualizations for polynomial regression.
    """
    # Colors for different polynomial degrees
    colors = ['blue', 'green', 'red', 'purple', 'cyan']

    # Create figure with subplots if yoy_analysis is True
    if yoy_analysis and len(values) > 1:
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=[title, f'Year-over-Year Percentage Change in {y_label}'],
            vertical_spacing=0.15,
            specs=[[{"type": "scatter"}], [{"type": "bar"}]]
        )
        fig_height = 800
    else:
        fig = go.Figure()
        fig.update_layout(title=title)
        fig_height = 600

    # Add original data points
    hover_template = '%{x}, ' + ('$%{y:,.2f}' if currency_format else '%{y:,.2f}')
    fig.add_trace(
        go.Scatter(
            x=years,
            y=values,
            mode='markers',
            name='Original Data',
            marker=dict(color='orange', size=10),
            hovertemplate=hover_template
        ),
        row=1, col=1
    )

    # Add polynomial fits
    for i, degree in enumerate(models.keys()):
        color_idx = i % len(colors)
        model = models[degree]

        # Calculate predictions for the expanded year range
        poly_features = PolynomialFeatures(degree=degree)
        future_poly = poly_features.fit_transform(future_years)
        future_pred = model.predict(future_poly)

        # Add line for this polynomial degree
        r2 = metrics[degree]['r2']
        mse = metrics[degree]['mse']

        fig.add_trace(
            go.Scatter(
                x=future_years.flatten(),
                y=future_pred,
                mode='lines',
                name=f'Degree {degree} (R² = {r2:.4f})',
                line=dict(color=colors[color_idx], width=2),
                hovertemplate=hover_template + '<br>Model: Degree %{customdata}<extra></extra>',
                customdata=[degree] * len(future_years),
                visible='legendonly' if degree != best_degree else True
            ),
            row=1, col=1
        )

    # Add forecast region for best model
    forecast_years_array = np.array(range(last_year, last_year + forecast_years + 1))
    forecast_values = []

    # Calculate forecast values using the best model
    poly_features = PolynomialFeatures(degree=best_degree)
    forecast_poly = poly_features.fit_transform(forecast_years_array.reshape(-1, 1))
    forecast_values = models[best_degree].predict(forecast_poly)

    # Add a vertical line at the last actual data point
    fig.add_vline(
        x=last_year, line_width=2, line_dash="dash", line_color="black",
        annotation_text=f"Last data point ({last_year})",
        annotation_position="top",
        row=1, col=1
    )

    # Highlight forecast region
    fig.add_trace(
        go.Scatter(
            x=np.concatenate([forecast_years_array, forecast_years_array[::-1]]),
            y=np.concatenate([forecast_values, [np.min(values)]*len(forecast_years_array)]),
            fill='toself',
            fillcolor='rgba(128, 128, 128, 0.2)',
            line=dict(color='rgba(255, 255, 255, 0)'),
            hoverinfo='skip',
            name='Forecast Region',
            showlegend=True
        ),
        row=1, col=1
    )

    # Add predicted future points with annotations
    fig.add_trace(
        go.Scatter(
            x=future_years_pred.flatten(),
            y=future_predictions,
            mode='markers+text',
            marker=dict(color='red', size=12, symbol='diamond'),
            text=[f"{int(yr)}: " + ('$' if currency_format else '') + f"{val:,.0f}" +
                  ('M' if currency_format and val > 1e6 else '')
                  for yr, val in zip(future_years_pred.flatten(), future_predictions)],
            textposition="top center",
            name='Predictions',
            hovertemplate='Year %{x}<br>' + ('$%{y:,.2f}' if currency_format else '%{y:,.2f}') + '<extra></extra>'
        ),
        row=1, col=1
    )

    # Add Year-over-Year percentage change chart if requested
    if yoy_analysis and len(values) > 1:
        yoy_change = np.diff(values) / values[:-1] * 100

        # Create the bar chart for YoY change
        fig.add_trace(
            go.Bar(
                x=years[1:],
                y=yoy_change,
                marker_color='skyblue',
                text=[f"{val:.1f}%" for val in yoy_change],
                textposition='outside',
                name='YoY Change',
                hovertemplate='Year %{x}<br>Change: %{y:.1f}%<extra></extra>'
            ),
            row=2, col=1
        )

        # Add horizontal line at 0% for reference
        fig.add_shape(
            type="line",
            x0=min(years[1:]),
            x1=max(years[1:]),
            y0=0,
            y1=0,
            line=dict(color="black", width=1, dash="solid"),
            row=2, col=1
        )

    # Update layout
    fig.update_layout(
        height=fig_height,
        hovermode="closest",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # Update x and y axis labels
    fig.update_xaxes(title_text=x_column, row=1, col=1)
    fig.update_yaxes(title_text=y_label, row=1, col=1)

    if yoy_analysis and len(values) > 1:
        fig.update_xaxes(title_text=x_column, row=2, col=1)
        fig.update_yaxes(title_text='Percentage Change (%)', row=2, col=1)

    # Format y-axis with currency if requested
    if currency_format:
        fig.update_yaxes(
            tickprefix='$',
            tickformat=',.0f',
            row=1, col=1
        )

    # Add buttons to toggle polynomial degrees
    degree_buttons = []
    for degree in models.keys():
        degree_buttons.append(
            dict(
                method='update',
                label=f'Degree {degree}',
                args=[{'visible': [True] +
                      [deg == degree for deg in models.keys()] +
                      [True, True]}]
            )
        )

    # Add all models button
    all_visible = [True] * (len(models) + 3)  # +3 for original data, forecast region, predictions
    degree_buttons.append(
        dict(
            method='update',
            label='All Models',
            args=[{'visible': all_visible}]
        )
    )

    # Add buttons to figure
    fig.update_layout(
        updatemenus=[
            dict(
                type='buttons',
                direction='right',
                buttons=degree_buttons,
                pad={'r': 10, 't': 10},
                showactive=True,
                x=0.01,
                xanchor='left',
                y=1.15,
                yanchor='top',
                bgcolor='rgba(255, 255, 255, 0.8)',
                bordercolor='rgba(0, 0, 0, 0.2)',
                borderwidth=1
            )
        ]
    )

    # No annotation for best model - removed as requested

    return fig

def create_static_plots(
    years, values, models, future_years, metrics, last_year,
    forecast_years, best_degree, poly_features,
    x_column, y_label, title, figsize, currency_format, yoy_analysis
):
    """
    Create static matplotlib visualizations (original implementation).
    """
    # Colors for different polynomial degrees
    colors = ['blue', 'green', 'red', 'purple', 'cyan']

    # Create a figure for visualization
    plt.figure(figsize=figsize)

    # Plot original data
    plt.scatter(years, values, color='orange', label='Original data')
    plt.title(title)
    plt.xlabel(x_column)
    plt.ylabel(y_label)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Plot polynomial fits
    for i, degree in enumerate(models.keys()):
        color_idx = i % len(colors)
        model = models[degree]

        # Calculate predictions for the expanded year range
        poly_features_deg = PolynomialFeatures(degree=degree)
        future_poly = poly_features_deg.fit_transform(future_years)
        future_pred = model.predict(future_poly)

        # Plot the polynomial fit
        mse = metrics[degree]['mse']
        r2 = metrics[degree]['r2']
        plt.plot(future_years, future_pred, color=colors[color_idx],
                label=f'Degree {degree} (R² = {r2:.4f}, MSE = {mse:.2e})')

    # Highlight forecast region
    forecast_years_array = np.array(range(last_year, last_year + forecast_years + 1))
    forecast_poly = poly_features.transform(forecast_years_array.reshape(-1, 1))
    forecast_values = models[best_degree].predict(forecast_poly)
    plt.fill_between(forecast_years_array, forecast_values, alpha=0.2, color='gray', label='Forecast region')

    # Add a vertical line at the last actual data point
    plt.axvline(x=last_year, color='black', linestyle='--', alpha=0.5, label=f'Last data point ({last_year})')

    # Format y-axis with millions if currency format is enabled
    if currency_format:
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1e6:.0f}M'))

    plt.legend()
    plt.tight_layout()
    plt.show()

    # Additional analysis: Year-over-year percentage change
    if yoy_analysis and len(values) > 1:
        yoy_change = np.diff(values) / values[:-1] * 100

        plt.figure(figsize=(12, 6))
        plt.bar(years[1:], yoy_change, color='skyblue')
        plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        plt.title(f'Year-over-Year Percentage Change in {y_label}')
        plt.xlabel(x_column)
        plt.ylabel('Percentage Change (%)')
        plt.grid(True, linestyle='--', alpha=0.7)

        for i, value in enumerate(yoy_change):
            plt.text(years[i+1], value + (2 if value > 0 else -5), f'{value:.1f}%', ha='center')

        plt.tight_layout()
        plt.show()

def run_overtime_forecast(
    department_name: str,
    dept_dfs: dict[str, pd.DataFrame],
    forecast_years: int = 2,
    test_degrees: list[int] = (2, 3, 4),
    x_column: str = 'YEAR',
    y_column: str = 'OVERTIME',
    title: str = None,
    y_label: str = 'Overtime Pay',
    **other_kwargs
) -> dict:
    """
    1. Check if the specified department exists.
    2. Call the polynomial_regression_forecast function.
    3. Print a formatted summary of the results.
    """
    df = dept_dfs.get(department_name)
    if df is None:
        print(f"[Error] Department '{department_name}' not found.")
        return None

    # If no title is provided, build a default title
    if title is None:
        title = f"Overtime Pay for {department_name} ({df[x_column].min()}–{df[x_column].max()})"

    # Call the forecasting function
    results = polynomial_regression_forecast(
        df=df,
        x_column=x_column,
        y_column=y_column,
        forecast_years=forecast_years,
        test_degrees=test_degrees,
        title=title,
        y_label=y_label,
        **other_kwargs
    )

    # Print a concise summary
    best = results['best_degree']
    r2 = results['metrics'][best]['r2']
    eq = results['equation']
    print(f"\n=== Forecast Summary for {department_name} ===")
    print(f"* Best polynomial degree: {best}")
    print(f"* R² score             : {r2:.4f}")
    print(f"* Model equation       : {eq}")

    return results