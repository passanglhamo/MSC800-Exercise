import sqlite3


def create_connection():
    conn = sqlite3.connect("money_exchange.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def insert_master_data():
    conn = create_connection()
    cursor = conn.cursor()

    try:

        # ==========================================
        # CUSTOMERS
        # ==========================================
        customers = [
            (
                "Passang",
                "Lhamo",
                "passang.lhamo@gmail.com",
                "5667777777",
                "NID001",
                "Auckland"
            ),
            (
                "Sonam",
                "Yeshi",
                "sonam.yeshi@gmail.com",
                "0212345678",
                "NID002",
                "Wellington"
            )
        ]

        cursor.executemany("""
            INSERT INTO customers
            (
                first_name,
                last_name,
                email,
                phone,
                nid,
                address
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, customers)


        # ==========================================
        # CURRENCIES
        # ==========================================
        currencies = [
            ("New Zealand Dollar", "NZD"),
            ("United States Dollar", "USD"),
            ("Australian Dollar", "AUD"),
            ("Indian Rupee", "INR"),
            ("British Pound", "GBP"),
            ("Euro", "EUR")
        ]

        cursor.executemany("""
            INSERT INTO currencies
            (name, symbol)
            VALUES (?, ?)
        """, currencies)


        # ==========================================
        # GET CURRENCY IDs
        # ==========================================
        cursor.execute("""
            SELECT id, symbol
            FROM currencies
        """)

        currency_map = {
            symbol: currency_id
            for currency_id, symbol in cursor.fetchall()
        }


        # ==========================================
        # EXCHANGE RATES
        # ==========================================
        exchange_rates = [

            # USD -> NZD
            (
                currency_map["USD"],
                currency_map["NZD"],
                1.65           
            ),

            # AUD -> NZD
            (
                currency_map["AUD"],
                currency_map["NZD"],
                1.08
            ),

            # INR -> NZD
            (
                currency_map["INR"],
                currency_map["NZD"],
                0.019
            ),

            # GBP -> NZD
            (
                currency_map["GBP"],
                currency_map["NZD"],
                2.20
            ),

            # EUR -> NZD
            (
                currency_map["EUR"],
                currency_map["NZD"],
                1.90
            ),

            # NZD -> USD
            (
                currency_map["NZD"],
                currency_map["USD"],
                0.59
            )
        ]

        cursor.executemany("""
            INSERT INTO exchange_rates
            (
                base_currency_id,
                target_currency_id,
                rate
            )
            VALUES (?, ?, ?)
        """, exchange_rates)


        # ==========================================
        # COMMIT
        # ==========================================
        conn.commit()

        print("Customers, currencies and exchange rates inserted successfully.")


    except sqlite3.Error as e:
        conn.rollback()
        print("Error inserting master data:", e)

    finally:
        conn.close()
