import sqlite3


def create_connection():
    conn = sqlite3.connect("money_exchange.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # 1. CUSTOMERS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            nid TEXT NOT NULL UNIQUE,
            address TEXT,
            regis_date TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)

    # 2. CURRENCIES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            symbol TEXT
        )
    """)

    # 3. EXCHANGE RATES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base_currency_id INTEGER NOT NULL,
            target_currency_id INTEGER NOT NULL,
            rate REAL NOT NULL CHECK (rate > 0),
            effective_date TEXT NOT NULL DEFAULT (datetime('now')),

            FOREIGN KEY (base_currency_id)
                REFERENCES currencies(id),

            FOREIGN KEY (target_currency_id)
                REFERENCES currencies(id),

            CHECK (base_currency_id != target_currency_id)
        )
    """)

    # 4. TRANSACTIONS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            rate_id INTEGER NOT NULL,
            from_amount REAL NOT NULL CHECK (from_amount > 0),
            to_amount REAL NOT NULL CHECK (to_amount > 0),
            rate_applied REAL NOT NULL CHECK (rate_applied > 0),
            trans_date TEXT NOT NULL DEFAULT (datetime('now')),

            FOREIGN KEY (customer_id)
                REFERENCES customers(id),
            FOREIGN KEY (rate_id)
                REFERENCES exchange_rates(id)    
        )
    """)

    conn.commit()
    conn.close()

    print("All tables created successfully.")