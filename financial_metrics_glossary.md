# Financial Metrics Glossary

A concise explanation of the indicators used in the Agentic Financial Intelligence System, consistent with the project's calculation methodology.

| Metric | Meaning in this project |
|---|---|
| **Annualized Return** | Geometrically annualized historical return, estimated from daily logarithmic returns over the selected period. |
| **Annualized Volatility** | Variability of daily logarithmic returns within the selected period, expressed on an annual basis even when the period is shorter than one year. |
| **Return-to-Risk Ratio** | Annualized return relative to annualized volatility, without subtracting the risk-free rate. |
| **Sharpe Ratio** | Annualized excess return per unit of volatility, accounting for a risk-free rate. |
| **Pearson Correlation** | Strength and direction of the linear relationship between two stocks' daily logarithmic returns. |
| **Momentum** | Cumulative price performance over the selected number of months, based on compounded monthly returns. |
| **Average Dollar Volume** | Average daily monetary trading activity (share price multiplied by trading volume) over the selected window. |
| **Momentum Ranking** | Ranking of stocks from highest to lowest calculated momentum. |
| **CAPM Beta** | Sensitivity of a stock's daily logarithmic returns to movements in the Dow Jones benchmark. |
| **Annualized Alpha** | Annualized intercept of the stock-versus-benchmark return regression; distinct from the CAPM return differential. |
| **R²** | Proportion of variation in a stock's returns explained by its regression against the benchmark. |
| **Observed Annual Return** | Geometrically annualized return actually observed in the selected historical period. |
| **CAPM Expected Return** | Model-implied annual return based on the risk-free rate, the stock's Beta and the Dow Jones market risk premium. |
| **Return Differential** | Difference between the observed annual return and the CAPM expected return. |

*The system uses 252 trading days for annualization and a default annual risk-free rate of 3%. Indicators are historical or model-based analytical measures, not investment recommendations.*
