import requests

from enums import VatagaURL


class TradesScraper:
    def __init__(self, email: str, password: str, last_id: str) -> None:
        self.email = email
        self.password = password
        self.last_id = last_id
        self._session = None

    def _init_session(self):
        self._session: requests.Session = requests.Session()

    def scrape(self):
        self._init_session()
        self._session.post(
            VatagaURL.LOGIN.value,
            data={"email": self.email, "password": self.password, "sso_token": False},
        )
        deals = self._session.get(VatagaURL.TRADES_FOR_TODAY.value.format(self.last_id))
        self._session.close()
        return deals.json()
