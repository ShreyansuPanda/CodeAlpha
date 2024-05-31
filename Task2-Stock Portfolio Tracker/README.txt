# Stock Portfolio Tracker

A stock portfolio tracking application built with Flask for the backend, JavaScript for the frontend, and SQLite3 for the database. This application allows users to track stock prices, monitor changes in real-time, and view the total portfolio value.

##Video Guide for this project: https://www.linkedin.com/posts/shreyansu-panda-5a9854276_stockportfoliotracker-codealphainternship-activity-7161969750602973184-yFyY?utm_source=share&utm_medium=member_desktop


## Features

- **Real-Time Stock Updates:** Fetches stock data using the Yahoo Finance API and updates prices dynamically.
- **Add and Remove Stocks:** Users can add stocks to their portfolio and remove them as needed.
- **Visual Representation:** Provides a graphical representation of stock prices with color-coded indicators for price changes.
- **Total Portfolio Value:** Calculates and displays the total value of the user's stock portfolio.

## Tools Used

- **Flask:** Web framework for backend development
- **JavaScript:** Programming language for dynamic frontend interactions
- **SQLite3:** Database management system for storing user data

## Requirements

- Python 3.x
- Flask
- yfinance (Yahoo Finance API wrapper)
- SQLite3 (usually included with Python)

## Installation

1. Clone the repository

2. Install required packages:
    ```sh
    pip install Flask yfinance
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

3. Here are the available functionalities:

    - **Add Stock:** Enter the stock ticker symbol and quantity of shares to add to your portfolio.
    - **Remove Stock:** Click the "Remove" button next to a stock to remove it from your portfolio.
    - **Real-Time Updates:** Stock prices are updated dynamically every 15 seconds.
    - **Total Portfolio Value:** The total value of your portfolio is displayed at the bottom of the page.

## Project Structure
   Stock Portfolio Tracker/
│
├── app.py
├── templates/
│ └── index.html
└── static/
└── script.js

## Functions

### `app.py`

- **`index()`**: Renders the main HTML template.
- **`get_stock_data()`**: Fetches stock data from Yahoo Finance API and returns JSON response.

### `script.js`

- **`startUpdateCycle()`**: Initiates the cycle for updating stock prices.
- **`addTickerToGrid(ticker, shares)`**: Adds a new stock to the grid with specified ticker and shares.
- **`updatePrices()`**: Fetches stock data for each ticker and updates prices dynamically.
- **`updateTotalAmount()`**: Calculates and updates the total value of the stock portfolio.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

