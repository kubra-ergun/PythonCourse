# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:32:01 2021

@author: kuber
"""

import wbdata
import datetime

wbdata.search_indicators('arable land') #AG.LND.ARBL.HA.PC - Arable land (hectares per person)
wbdata.search_indicators('net migration') #SM.POP.NETM - Net migration
wbdata.search_indicators('GDP per capita') #NY.GDP.PCAP.CD - GDP per capita (current US$)

data_date = (datetime.datetime(1960, 1, 1), datetime.datetime(2021, 1, 1))
indicators = {'AG.LND.ARBL.HA.PC':'arable_land','NY.GDP.PCAP.CD':'gdppc','SM.POP.NETM':'net_migration'}
countries = [i['id'] for i in wbdata.get_country(incomelevel="LIC" and "MIC")] 
df = wbdata.get_dataframe(indicators, country=countries)

df.to_csv('data.csv')
df.describe()

from regression import regression
regression(df)

