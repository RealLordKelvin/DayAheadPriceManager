
# 90256b9f-46fd-4542-a482-a11f3207e696


from entsoe import EntsoePandasClient
import pandas as pd
import datetime 

# get the day ahead day. meaning the date for tomorrow.
# Note however, that if the request is made before 12 oclock then ENTSOE will not
# have yet the prices from the day ahead auctions since these are made and published
# at 12 clock.

today = datetime.date.today()
# because we want to get the prices for next day we need the start date to
# be tomorrow and the end date to be tomorrow plus one

now = datetime.datetime.now() + datetime.timedelta(hours=2)
today12oclock = now.replace(hour=12, minute=30, second=0, microsecond=0)

def handle_before_and_after_12oclock_dayahead_prices():
    
    '''get the day ahead day. meaning the date for tomorrow.
    Note however, that if the request is made before 12 oclock then ENTSOE will not
    have yet the prices from the day ahead auctions since these are made and published
    at 12 clock'''

    now = datetime.datetime.now() + datetime.timedelta(hours=2)
    today12oclock = now.replace(hour=12, minute=30, second=0, microsecond=0)

    if now < today12oclock:
        start = datetime.date.today()
        end = today + datetime.timedelta(days = 1)
    else:
        start = datetime.date.today() + datetime.timedelta(days = 1)
        end = datetime.date.today() + datetime.timedelta(days = 2)

    start_output = pd.Timestamp(str(start).replace('-', ''), tz='Europe/Brussels')
    end_output = pd.Timestamp(str(end).replace('-', ''), tz='Europe/Brussels')
    
    return start_output, end_output


client = EntsoePandasClient(api_key='90256b9f-46fd-4542-a482-a11f3207e696')

start, end = handle_before_and_after_12oclock_dayahead_prices()


COUNTRY_CODE = 'DE_LU'  # Belgium

data_request = client.query_day_ahead_prices(COUNTRY_CODE, start=start,end=end)
