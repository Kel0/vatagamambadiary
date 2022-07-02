import os
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials

ABS_PATH = Path().resolve()


class DealExporter:
    def __init__(self):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
        ]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            os.path.join(ABS_PATH, "simpleapply-8a9878d256f4.json"), self.scope
        )
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("myDiary").get_worksheet(0)

    def export(self, data):
        for _id, deal in enumerate(data):
            writtenOrders = []
            try:
                with open(os.path.join(ABS_PATH, "temp/tempOrders.txt"), "r") as f:
                    writtenOrders = f.read().split(",")
            except FileNotFoundError:
                pass

            if f"{deal['ticker']}:{deal['openTime']}" in writtenOrders:
                continue

            self.sheet.append_row(
                (
                    deal["ticker"],
                    deal["openTime"].split("T")[-1],
                    "",
                    deal["direction"],
                    deal["quantity"],
                    "",
                    deal["pnl_points"],
                    deal["pnl_profit"],
                )
            )
            with open(os.path.join(ABS_PATH, "temp/tempOrders.txt"), "a+") as f:
                f.write(f"{deal['ticker']}:{deal['openTime']},")
