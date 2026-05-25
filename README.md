Website link: https://weatherquantmachine.streamlit.app/

This project represents a sophisticated intersection of data engineering and financial analysis. At its core, the application serves as a quantitative dashboard designed to test the sensitivity of energy utilities to local climate fluctuations. By architecting a seamless integration between the Open-Meteo historical weather archive and Yahoo Finance’s market data, the system automates the extraction, transformation, and loading (ETL) of complex time-series datasets.

The technical stack leverages Python’s Pandas for high-speed data alignment and Streamlit for a responsive, cloud-deployed user interface. Key features include dynamic GPS coordinate mapping for multiple global energy hubs and an automated "rolling window" date logic that ensures the analysis is always current. Beyond mere visualization, the tool calculates a real-time correlation coefficient, providing users with immediate insight into whether extreme temperature swings are statistically significant drivers of stock price volatility. This project demonstrates a professional-grade ability to handle asynchronous API calls and resolve real-world data merging challenges in a live production environment.

1. How to use:

a. Select an Energy Hub: Use the sidebar to choose a city. Each city is linked to a major utility stock (e.g., NRG for Houston) and its specific GPS coordinates.

b. The Time Window: The machine automatically looks back at the last 365 days. This provides enough data for a statistical "sample size" without using outdated information from years ago.

c. Run Analysis: This triggers the "Live Fetch." The dots you see are the exact high temperature and the stock's performance for every single day the market was open.

2. Reading the Scatter Plot

This is your most important visual. Each dot represents one day in the last year.

The X-Axis (Bottom): This is the Maximum Temperature in Celsius.

Dots to the right are hot summer days.

Dots to the left are cold winter days.

The Y-Axis (Left): This is the Daily Return of the stock.

Dots above 0.00 mean the stock went up that day.

Dots below 0.00 mean the stock price dropped.

3. Interpreting the AI Prediction Line

Once the AI finishes its learning phase, it draws a line through the center of the dots. This is called the Line of Best Fit.

Sloping Down: This suggests an Inverse Relationship. It means as it gets hotter, the stock tends to perform worse. This might happen if extreme heat causes power grid stress or higher operating costs.

Sloping Up: This suggests a Positive Relationship. As temperatures rise, the stock rises. This often happens in summer when people turn on Air Conditioning, leading to higher revenue for the power company.

Flat Line: This means No Correlation. The AI has decided that the weather has almost no predictable impact on this specific stock.

The Correlation Score: The machine gives you a number between +1 and -1.

+0.7 to +1.0: Strong Positive Strong signal! Weather is a major driver of this stock.

+0.3 to +0.6: Moderate Weather is one of many factors influencing the price.

-0.2 to +0.2Weak / NoiseMost Common. The stock is moved by news or earnings, not the weather.

-0.7 to -1.0 Strong NegativeStrong signal! The stock consistently drops when heat rises.

Note: 
Correlation does not equal Causation. Just because a stock went up on a hot day doesn't mean the heat caused it. It could have been a good earnings report or a general market rally. Use this machine to find clues, not to make gambles!

