from database import create_tables,create_connection
from master_data import insert_master_data
from money_ex import money_exchange

def main():

    conn = create_connection()

    create_tables()
    insert_master_data()

    exchange = money_exchange(conn)

    # Check if the customer exists in the database
    nid = input("Enter your identification number (NID): ")
    customer = exchange.find_customer(nid)

    if not customer:
        print("Customer not found.")
        conn.close()
        return

    exchange.show_rates()


    exchange.amount = float(
        input("Enter amount: ")
    )

    exchange.currency = input(
        "Enter your currency: "
    ).upper()

    to_currency = input(
        "Enter currency to convert to: "
    ).upper()

    rate = exchange.get_rate(
        exchange.currency,
        to_currency
    )

    if not rate:

        print("Exchange rate not found.")
        conn.close()
        return
    
    converted_amount=exchange.convert(
        to_currency,
        rate[1]
    )
    exchange.save_transaction(
        customer[0],
        rate[0],
        converted_amount,
        rate[1]
    )
    conn.close()


if __name__ == "__main__":
    main()