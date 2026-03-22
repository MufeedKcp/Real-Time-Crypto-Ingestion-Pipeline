# CryptoStream-100

**A simple, automated pipeline that fetches live data for the top 100 cryptocurrencies and stores it safely in a PostgreSQL database.**

### What is this project and why do you need it?

If you are looking for a reliable way to build your own historical price database without manual work, you have found the right place. Most people struggle with messy API responses or losing data because they don't have a place to store it. This project solves that by creating a bridge between live market data and your own private database.

- **Data Ingestion:** Automatically pulls the latest prices, market cap, and volume for the top 100 coins.
    
- **Storage:** Converts complex JSON data into clean, organized tables in PostgreSQL.
    
- **Analysis Ready:** Every entry is timestamped, making it the perfect foundation for future price trend analysis and AI modeling.
    
- **Set and Forget:** Includes a built-in timer to fetch data repeatedly without manual intervention.
    

---

### Visualls

<style>
.image-space {
    margin-right: 20px;
}
</style>
<img src="docs/code_running.png" class="image-space" alt="My Image" style="width:400px;"> 
<img src="docs/PostgreSQL_table.png" alt="My Image" style="width:400px;">


---

### Instructions

#### How to run it (For users)

    
1. . Sign up at [CoinMarketCap Developers](https://www.google.com/url?sa=E&q=https%3A%2F%2Fpro.coinmarketcap.com%2F) to get your key.
    
2. Setup a PostgreSQL database ready to receive the data.
    
3. Run the script

### For Developer

1. **Clone the Repo:**
    ```
    git clone (https://github.com/MufeedKcp/Real-Time-Crypto-Ingestion-Pipeline.git)
    cd cryptostream-100
    ```
    
2. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```
    
3. **Configure Environment Variables:**  
    Create a .env file:
    ```
    API_KEY=your_coinmarketcap_key_here
    DATABASE_PATH=postgresql://username:password@localhost:5432/your_db_name
    ```
    
4. You can change the limit in the **api_collector()** function to track more than 100 coins or adjust the sleep timer to change the frequency.
    

---

### Contributor Expectations

If you want to contribute:

- Don't add over-complicated code.
    
- If you find a bug, open an "Issue" first.
    
- I am planning to add data transformation soon. If you want to help with that, please reach out via a Pull Request.
    

---

### Known Issues

While this project is robust, there are a few things it currently does **not** do:

- The data is stored in its raw format. (Transformation features coming in the next update).
    
- The script is currently set to run exactly 5 times and stop.
    
- If you run the script multiple times, it will keep appending data; it does not check if the coin data for that exact second already exists.
    
- It does not automatically handle CoinMarketCap's rate limit errors if you try to run it every second.



### Future Improvements:
- Data Transformation The "Silver" Layer.
- Dockerization.
- Real-time Dashboard.
- Automated Scheduling using Airflow or a simple Cron job for 24/7 data collection.
- Integrating a notification system  (Email) to alert, if the API fails.

---

### Support This Project 

If this project helped you save hours of work or helped you build your crypto dashboard, consider buying me a coffee. Every bit of support helps me keep this repo updated!


