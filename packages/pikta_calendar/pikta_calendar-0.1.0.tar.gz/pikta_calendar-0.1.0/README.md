# pikta-calendar
Production calendar from [www.consultant.ru](http://www.consultant.ru/law/ref/calendar/proizvodstvennye/)

## Standard use

```python
from pikta_calendar import PiktaCalendar

prod_cal = PiktaCalendar(2021)

holidays = prod_cal.get_holidays_by_month(5)  # returns a list of holiday days
weekends = prod_cal.get_weekends_by_month(5)  # returns a list of weekend days
business_days = prod_cal.get_business_days_by_month(5)  # returns a list of business days

is_holiday = prod_cal.is_holiday(12, 31)  # holiday check
is_weekend = prod_cal.is_weekend(12, 19)  # weekend check

```

## Using with a proxy

```python
from pikta_calendar import PiktaCalendar

my_proxy = {
    "url": "your_proxy:port",
    "login": "your_login",
    "password": "your_password"
}

prod_cal = PiktaCalendar(2021, my_proxy)

holidays = prod_cal.get_holidays_by_month(5) 

```
