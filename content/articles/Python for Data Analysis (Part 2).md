Title:Notes: Python for Data Analysis (Part 2)
Date: 2015-10-23 17:40
Modified: 2015-10-23 18:10
Tags: tech-iT 
Category: Blog/English
Slug: notes python for data analysis 2
Author: JIN Lin
[TOC]

To continue with [previous post](http://linnus.net/posts/2015/Oct/12/notes%20python%20for%20data%20analysis/) about the basics of NumPy and Pandas. 

### Plotting and Visulization 

**matplotlib**

It is the primary MATLIB-like 2D plot; add-on toolkits like **mplot3d** for 2D plot, and **basemap** for mapping and projections. 

	#launch interaction between *IPython* and *matplotlib*
	ipython --pylab
	import matplotlib.pyplot as plt

**Figures & Subplots**

	fig = plt.figure(figsize=(w,h),dpi= None,...) 
	#it is a top level container for all plot elements. 

[More here](http://matplotlib.org/api/figure_api.html)

	fig.add-subplot(*args,*kwargs)
	#args same as in *plt.subplot* 
	subplot(nrows, ncols, plot_number)
	#*kwargs: xlabel,ylabel, etc. 

**Spacing around plots**

	plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)

**Colors,Markers, Line Styles**


	e.g. 
	plot(randn(x,y, color='k', linestyle='dashed', marker='o',label='Default') 


**Ticks, Labels. Legends**

xlim, xticks, xticklabels 

	e.g.
	plt.xlim() or plt.xlim([a,b])
	
All such methods act on the active or most recently-created *AxesSubplot*. corresponds to two methods: ax.get_xlim, and  ax.set_xlim 

	e.g. 
	ax.legend() or plt.legend() 
	#automatically creates legends. 

**Annotations, Drawing**

*text, arrow, annotate*

	e.g. 
	ax.text(x,y,'Tidehello',family='monsapce',fontsize=12) 
	#(x,y) cooridates on the plot


**Shapes**

*matplotlib.patches* 

	e.g. 
	rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3);
 	ax.add_patch(rect)

**Saving plots**

	plt.savefig('figpath.png', dpi=400, bbox_inches='tight')

**matplotlib configuration**

The default configuration is geared towards for publication, however, it can be modified by changing the config settings. 

	e.g. 
	plt.rc('figure', figsize=(10, 10))

### Plotting Functions in pandas 

Compard to *matplotlib*, it offers a high-level plotting methods due to the highly organized Series/DataFrames. 

*Series.plot()* arguments: 

- label, ax, style, alpha, kind(bar,line,barh,kde), logy, use_index, rot, xticks, yticks, xlim, ylim, grid. 

*DataFrame specific arguments*

- subplots, sharex, sharey, figsize, title, legend, sort_columns


**Bar plots**

	ax.plot(kind = 'bar'  or 'barh', stacked= True/False)

**Histograms/ Density Plot**

e.g. 

	values.hist(bins=100, alpha=0.3, color='k', normed=True)
	values.plot(kind='kde', style='k--')


**Scatter plots**

	plt.scatter(x,y)


**Maps**

refer to [2015 Federal Electon Tutorial](http://linnus.net/posts/2015/Oct/04/2016_US_Federal_Election_Contributors/) for more. 


### Data Aggregation and Group Operations. 

**GroupBy** mechanism: *split-apply-combine* 

`df.groupby(key or keys).mean()`: *df.groupby()* returns a GroupBy object which is ready for subsequent computation, *.mean()* does the *apply-combine* opeartion. By default, it groups on axis = 0. 

`df.groupby(key or keys).size()`: returning a Series containing group size ( how many elements are grouped under each key)

Keys could be in the form of ndarray, dict or Series. e.g. mapping the column names to other category information.

	mapping = {'a': 'red', 'b': 'red', 'c': 'blue', ....: 'd': 'blue', 'e': 'red', 'f' : 'orange'}
	# by dict mapping
	by_column = people.groupby(mapping, axis=1)
	# by series 
	map_series = Series(mapping)
	people.groupby(map_series, axis=1).count()
 
- **Iterating over groups**

		e.g. 
		for (k1, k2), group in df.groupby(['key1', 'key2'])
	

- **Selecting subset columns**

		e.g 
		df.groupby(['key1', 'key2'])[['data2']].mean()

- **Grouping with Functions**

e.g `people.groupby(len).sum()`: len is the length of *names*. Everything will be converted to array internally. 

- **Grouping by Index Levels**

		e.g.
		hier_df.groupby(level='cty', axis=1).count()


**Data Aggregation**

Data transformation that produces scalar vaues from arrays. 

- **optimized groupby methods**

count, sum, mean, median, std, var, min, max, prod, first, last. describe.

- **user functions** 

aggregate / agg : `grouped.agg(user_functions)`. Normal fuctions can still be used,e.g.`grouped.agg('mean','sum')`

- **Other operations**

A list of (name,functions) tuples can be passed to the agg keys. *name*  will replace *functions name*. e.g. `grouped.agg([('foo', 'mean'), ('bar', np.std)])`

Apply different functions to different columns: e.g. `grouped.agg({'tip' : [np.max, 'min'], 'size' : 'sum'})`

 Return aggregated data in unindexed form. e.g 'tips.groupby(['sex', 'smoker'], as_index=False).mean()'.  *reset_index* could be used to reset the index. 
 
 
 **Group-wise Operations and Transformations** 
 
 - **transform**

aggregate + merge : add columns to existing df. 

*Transform* applies a function to each group, then places the results in the appropriate locations. If each group produces a scalar value, it will be propagated (broadcasted) to the same size as the df. .eg. ` people.groupby(key).transform(np.mean)`. 
 
 - **apply**

*Apply* splits the object being manipulated into pieces, invokes the passed function on each piece, then attempts to concatenate the pieces together. 

In GroupBy, the *describe* method is a shortcut for 

	f = lambda x: x.describe() 
	grouped.apply(f)
	
group-keys can be opened up, i.e. each row has a corresponding key. 
e.g. ` tips.groupby('smoker', group_keys=False).apply(top)`


- **Bucket/Quantile Analysis**

*cut/qcut* e.g: 
	factor = pd.cut(frame.data1, 4) 
	grouped = frame.data2.groupby(factor)
	grouped.apply(get_stats).unstack()
	
- **Fill missing values**

Fill NA with fixed value. e.g. 

	s.fillna(s.mean())
	
Fill vaule varied by group. e.g. 

	states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
	group_key = ['East'] * 4 + ['West'] * 4
	fill_mean = lambda g: g.fillna(g.mean())
	data.groupby(group_key).apply(fill_mean)
	
Fill pre-defined values. e.g. 

	fill_values = {'East': 0.5, 'West': -1}
	fill_func = lambda g: g.fillna(fill_values[g.name])
	data.groupby(group_key).apply(fill_func)
	
- **Other application examples**

- Random sampling and permutation: 

e.g 

	#create a deck of cards 
	# Hearts, Spades, Clubs, Diamonds 
	suits = ['H','S','C','D']
	# let Ace be 1
	card_val = (rang(1,11)+[10]*3)*4
	base_names = ['A'] + range(2, 11) + ['J', 'K', 'Q']
	cards = []
	for suit in ['H', 'S', 'C', 'D']: 
		cards.extend(str(num) + suit for num in base_names)
	# deck e.g AH 1; KH 10 	
	deck = Series(card_val, index=cards)
	
	# draw 5 cards 
	def draw(deck,n = 5):
		return deck.take(np.random.permutation(len(deck))[:n])
		
	# Draw two random cards from each suit 
	get_suit = lambda card: card[-1] # last letter is suit
	deck.groupby(get_suit).apply(draw, n=2)
	
	
- group weighted average and correlation ( between columns / series) 

e.g.

	 			    #AAPL   MSFT  XOM  SPX 
	 	#2011-10-11 400.29 27.00 76.27 1195.54
	 	spx_corr = lambda x: x.corrwith(x['SPX'])
	 	by_year = rets.groupby(lambda x: x.year)
	 	by_year.apply(spx_corr
	 	

- linear regression

**Pivot-tables / Cross Tabulation**

*pivot_table* e.g. 
	
	tips.pivot_table(rows=['sex', 'smoker']) 
	# groupby has the same function 
	# *margin* method could be used to include partial total. 
	tips.pivot_table(['tip_pct', 'size'], rows=['sex', 'day'],cols = 'smoker', margins = True)
	
	#other options:  values, rows, cols, aggfunc, fill_value, margins
	
*Cross-tabulation: crosstab*

computes group frequencies. e.g` pd.crosstab(data.Gender, data.Handedness, margins=True)`


### Time Series 

- Python **datetime** module 

Types: date, time, datetime, timedelta

e.g.`from datetime import datetime; now = datetime.now()`

 
- Converting between string & datetime  

e.g.

	# time to string 
	stamp = datetime(2011, 1, 3) 
	#str
	str（stamp）
	#strftime 
	stamp.strftime('%Y-%m-%d')
	
	# string to time 
	value = '2011-01-03'
	datetime.strptime(value, '%Y-%m-%d')
		
	# parse date formats 
	from dateutil.parser import parse
	parse('2011-01-03')
	
	# pandas to_datetime method 
	pd.to_datetime(['1/1/2011'])
	
	# NaT (Not a Time) is pandas’s NA value for timestamp data.


Other datetime formats: %Y(4-digit year), %y (2-digit year), %m(2-digit month), %d (2-digit day),%H(24-hour clock); %I (12-hour clock), %M(2-digit minute）, %S(second),%w (weekday as ineger, [0 Sunday,6]), %U (week number of a year [0,53],Sun is the first day of a week),%W (week number of a year [0,53],Mon is the first day of a week), %z(UTC timezone offsets), %F(Shortcut for%Y-%m-%d),%D(Shortcut for%m/%d/%y). 

**timestamp**

DatetimeIndex; dtype: datetime64

*TimeSeries* is a subset of Series, therefore can be indexed, sliced, and selected, 

	e.g.
	index=pd.date_range('1/1/2000', periods=1000))
	# truncate between two dates. 
	ts.truncate(after='1/9/2011')
	
duplicate indices 

	# is_unique 
 
**Date ranges/frequencies/shifting**

By default, *date_range* generates daily timestamp. 

	e.g. # BM last business day of month.
	pd.date_range('1/1/2000', '12/1/2000', freq='BM')

By default, the time series has no fixed frequency. *base frequency*
like 'M', 'H'，'B'(business day),'Q-JAN'(quater end), 'A-JAN'(year end)

	e.g. 
	# import base frequencies
	from pandas.tseries.offsets import Hour, Minute
	# multiplier 
	four_hours = Hour(4)
	#
	pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')
	# WOM, week of month, WOM-3FRI: third Fri of each month. 
	rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')

**Shifting Data**

Applicaton: compute percent changes in time series in the form of ts / ts.shift(1) - 1.
	
	e.g. 
	ts.shift(1, freq='3D') 

Offsets can also be used to shift time

	e.g. 
	from pandas.tseries.offsets import Day, MonthEnd
	now + 3 * Day()
	# rollforward, rollbackward,
	offset = MonthEnd()
	offset.rollforward(now)
	
**Timezone**

>UTC: coordinated universal time 
>
>Greenwich Mean Time 
>
>DST: daylight savings time
>

In Python, time zone infor is stored in 3rd party module *pytz* 

	import pytz
Localization & Conversion
	
	e.g. 
	pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC')
	#localize  (tz_localize)
	ts_utc = ts.tz_localize('UTC')
	#convert   (tz_convert)
	ts_utc.tz_convert('US/Eastern')
	
Timezone-aware Timestamp Objects 

	e.g. 
	stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
	
	#or localize 
	stamp.tz_localize('US/Eastern')
	
Operations between time zones 

When two time series are combined, the resulting timezone will be UTC. 

**Periods**

	e.g.
	# timespan from 1-1-2007 - 12-31-2007
	p = pd.Period(2007, freq='A-DEC')  
	
	# period_range 
	rng = pd.period_range('1/1/2000', '6/30/2000', freq='M')
	# convert frequency 
	p.asfreq('M', how='start') # or p.asfreq('M','start')
	
	#period_index 
	values = ['2001Q3', '2002Q2', '2003Q1']
	index = pd.PeriodIndex(values, freq='Q-DEC')
	
Quaterly Period: 
	
	# Fiscal year ending in Feb, Q4 runs from Nov to Feb, inclusive. 
	p = pd.Period('2012Q4', freq='Q-FEB')
	
**Timestamp to Periods**

*to_period*

	e.g. 
	rng = pd.date_range('1/29/2000', periods=6, freq='D')
	ts = Series(randn(6), index=rng)
	tp = ts.to_period('M') #the fre changes to Month 
*to_timestamp*

	tp.to_timestamp(how='end')
	
**Resampling**

- Timestamp

*resample(methods)*,  methods include freq, how( such as mean, ohlc, sum,etc), axis, fill_method, etc. 

*downsampling*: aggregation is needed.

*upsampling*: no aggregation is needed,missing values are filled. e.g. `frame.resample('D', fill_method='ffill', limit=2)`
	 - Periods

Same principles apply
 
  	e.g. 
  	annual_frame.resample('Q-DEC', fill_method='ffill', convention='start')'


END. 


