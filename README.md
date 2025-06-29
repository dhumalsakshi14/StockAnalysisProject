# StockAnalysisProject
Develop a mini full-stack web application that integrates: 1. Java Spring Boot (backend) 2. Python (data analysis) 3. React.js or JavaScript (frontend visualization)  The application will process stock market data, analyze trends, and display visual insights.

 1. Backend API (Java Spring Boot or Python)
         • Develop a RESTful API that:
         o Accepts a CSV file containing historical stock data.
         o Calls a Python script for data analysis.
         o Retrieves the processed data and serves it to the frontend.

2. Data Processing (Python - Pandas, Matplotlib, NumPy, or Scikit-learn)
         • The Python script should:
         o Perform basic data analysis, e.g., calculating moving averages, highest/lowest stock price,and volatility.
         o Generate a line plot showing price trends and highlight key metrics (e.g., moving averages).
         o Save the plot as a PNG/JPEG file or return data in JSON format.

3. Frontend Visualization (React.js or JavaScript with Chart.js/Plotly)
         • The frontend should:
         o Provide a file upload interface for users to submit CSV files.
         o Fetch processed data or the generated plot from the backend.
         o Display dynamic stock trend visualizations using Chart.js or Plotly.
