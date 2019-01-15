#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import time

'''szsm = ts.get_h_data('000034', autype='hfq', start='2008-12-31', end='2018-12-31')

szsm.to_excel('E:/PY/szsm.xls', columns=['close'])

'''

def get_eps():

	eps = 0
	x = 0

	for year in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]:
		for quarter in [4]:
			eps1 = ts.get_report_data(year,quarter).ix[:, ['code', 'eps']].rename(columns = {'eps': '%s-%s' %(year, quarter)})
			#ts.get_profit_data(year,quarter).to_excel('E:/PY/MGSY%s_%s.xls' %(year, quarter))

			if x:
				eps = eps.merge(eps1, on = 'code', how = 'outer')
			else:
				eps = eps1
			
			x+=1

	eps.to_excel('E:/PY/investmode/davis/eps.xls')
			
def get_kline(code):
	

		
#JLR1 = ts.get_growth_data(2014,1).ix[:, ['code', 'name', 'nprg']].rename(columns = {'nprg': '2014-1'})
#JLR2 = ts.get_growth_data(2014,2).ix[:, ['code', 'name', 'nprg']].rename(columns = {'nprg': '2014-2'})

#JLR = 0

#JLR = JLR1.merge(JLR2, on = 'code').to_excel('E:/PY/test.xls')
#JLR2 = JLR

