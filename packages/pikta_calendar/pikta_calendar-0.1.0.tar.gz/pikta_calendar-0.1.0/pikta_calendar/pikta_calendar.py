from datetime import date
from bs4 import BeautifulSoup
from .consult_service import ConsultService


class PiktaCalendar:
    def __init__(self, year: int, proxy: dict = None):
        self.__consultant = ConsultService(proxy)

        if self.__consultant.is_content_available(year):
            self.__year = year
        else:
            raise ValueError("Data not available")

    # Holiday check
    def is_holiday(self, month: int, day: int):
        if self.__is_correct_date(month, day):
            return date(self.__year, month, day) in self.get_holidays_by_month(month)
        else:
            raise ValueError("Incorrect month or day")

    # Weekend check
    def is_weekend(self, month: int, day: int):
        if self.__is_correct_date(month, day):
            return date(self.__year, month, day) in self.get_weekends_by_month(month)
        else:
            raise ValueError("Incorrect month or day")

    # Returns a list of holiday days
    def get_holidays_by_month(self, month: int):
        return self.__get_dates_by_selector("holiday", month)

    # Returns a list of weekend days
    def get_weekends_by_month(self, month: int):
        return self.__get_dates_by_selector("weekend", month)

    # Returns a list of business days
    def get_business_days_by_month(self, month: int):
        return self.__get_dates_by_selector("", month)

    # Returns html calendar for all months
    def __get_months_content(self):
        content = self.__consultant.get_html_content(self.__year)
        soup = BeautifulSoup(content, features="html.parser")

        return soup.select(".cal tbody")

    # Checks a date for correctness
    def __is_correct_date(self, month, day=1):
        try:
            date(self.__year, month, day)
            return True
        except ValueError:
            return False

    # Returns a list of dates of the month by css selector
    def __get_dates_by_selector(self, class_name, month):
        if self.__is_correct_date(month):
            data = []
            months_content = self.__get_months_content()[month - 1]

            for item in months_content.find_all("td"):
                if class_name:
                    if class_name in item.get("class"):
                        data.append(date(self.__year, month, int(item.text)))
                else:
                    if not item.get("class"):
                        data.append(date(self.__year, month, int(item.text)))

            return data
        else:
            raise ValueError("Incorrect month")
