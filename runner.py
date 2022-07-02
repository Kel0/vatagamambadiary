from data_handler import get_deals
from gsheet import DealExporter


def export():
    exporter = DealExporter()
    deals = get_deals()
    exporter.export(deals)


if __name__ == "__main__":
    export()
