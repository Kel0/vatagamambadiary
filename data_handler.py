from scraper import TradesScraper
from settings import ACCOUNT_LAST_4_ID, EMAIL, PASSWORD


def get_deals():
    results = []
    scr = TradesScraper(EMAIL, PASSWORD, ACCOUNT_LAST_4_ID)
    deals = scr.scrape()
    for deal in deals["deals"]:
        profit = deal["pnl_profit"].encode("ascii", "ignore").decode("utf-8")
        fees = deal["fees"].encode("ascii", "ignore").decode("utf-8")

        results.append(
            {
                "ticker": deal["symbol_code"],
                "openTime": deal["open_time"],
                "direction": "LONG" if deal["side"] == "Покупка" else "SHORT",
                "quantity": deal["max_quantity"],
                "pnl_points": deal["pnl_points"],
                "pnl_profit": round(float(profit) - float(fees), 2),
            }
        )
    return results
