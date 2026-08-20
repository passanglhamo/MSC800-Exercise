class money_exchange:

    def __init__(self, conn):
        self.conn = conn
        self.amount = 0
        self.currency = ""

    def find_customer(self, nid):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT id, first_name, last_name
            FROM customers
            WHERE nid = ?
        """, (nid,))

        return cursor.fetchone()

    def get_rate(self, from_currency, to_currency):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT
                er.id,
                er.rate
            FROM exchange_rates er

            JOIN currencies base
                ON er.base_currency_id = base.id

            JOIN currencies target
                ON er.target_currency_id = target.id

            WHERE base.symbol = ?
            AND target.symbol = ?

            ORDER BY er.effective_date DESC

            LIMIT 1
        """, (from_currency, to_currency))

        return cursor.fetchone()

    def show_rates(self):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT
                base.symbol,
                target.symbol,
                er.id,
                er.rate
            FROM exchange_rates er

            JOIN currencies base
                ON er.base_currency_id = base.id

            JOIN currencies target
                ON er.target_currency_id = target.id

            ORDER BY base.symbol, target.symbol
        """)

        rates = cursor.fetchall()

        for from_currency, to_currency, rate_id, rate in rates:

            print(
                f"ID: {rate_id} | "
                f"{from_currency} -> {to_currency} "
                f"| RATE: {rate}"
            )

    def convert(self, to_currency, rate):

        converted_amount = self.amount * rate

        print(
            f"{self.amount:.2f} {self.currency} "
            f"= {converted_amount:.2f} {to_currency}"
        )

        return converted_amount

    def save_transaction(
        self,
        customer_id,
        rate_id,
        to_amount,
        rate
    ):

        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (
                customer_id,
                rate_id,
                from_amount,
                to_amount,
                rate_applied
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            customer_id,
            rate_id,
            self.amount,
            to_amount,
            rate
        ))

        self.conn.commit()

        print("Transaction saved successfully.")
        print(
            f"Transaction ID: {cursor.lastrowid}"
        )