Title:Notes: Python for Data Analysis (Part 1)
Date: 2015-10-12 20:40
Modified: 2015-10-12 21:10
Tags: tech-iT 
Category: Blog/English
Slug: notes python for data analysis 
Author: JIN Lin
[TOC]

Finished reading the book *Python for Data Analysis*. The review notes are just for my quick reference of available data processing tools with the focus on NumPy and Pandas. 

###Essential Libraries

- NumPy 

> ndarray; element-wise computation; `

- pandas

> DataFrame (time-series for financial data; reshape, slice, dice, aggregation etc.)

- matplotlib 

> Plots. 2D data visulization; interactive within IPython

- IPython 

> Terminal-based or HTML-based notebook 

- SciPy 

> packages for various scientific computing: scipy.integrate; linalg,optimize, signal,sparse,special,stats, weave, etc. 

###IPython
- Tab completion (methods,file directories etc.);

- Introspection (xx?: show general info,docstring; xx?? show source code if any; together with *,e.g. np.*load*?)

- %run: run the script; ctrl-c interrupt running code

- %pase, %cpase 

- short cuts 
- magic commands: %magic, %quickref

- matplotlib integration: ipython --pylab 

- command history: up-arrow key 

- input and output variables: _ or ___ / _iX (input) _X (output)

- %hist: print input history; 

- logging the input/output: %logstart; %logstop

- interacting with OS: shell commands, %alias, 

- %bookmark: pin the directory 

- interactive debugger: %debug 

- timecode: %timeit and %time; %prun, %run -p 

- ipython notebook --pylab=inline

- profiles and configuration: cd  ~/.config/ipython/


###NumPy

**ndarray**

- multidimensional homogeneoys data: shape; dtype (arrayd.shape; arrayd.dtype)
- creating array: np.array(data) / np.zeros; np.ones; np.empty; np.arange, np.eye 
- data types: int8/16/32/64, float16/32/64/128,complex64/128/256, bool, object, string_, unicode_ (e.g. np.float64)

- convert dtype: *astype* method ,creating a new array
- vectorization: element-wise, broadcasting 
- indexing,slcing: single element: [1,2,...,n] for n-dimension arrays; rows; columns; boolean indexing: ==, <,>, etc; fancy indexing: alter the row/column order, copying the data to new array 
- transposing: e.g np.arange(15).reshape((3,5)); arr.T; arr.transpose 
- inner product: np.dot(a,b)
- swapaxes: arr.swapaxes()
- ufunc: universal functions, e.g. np.sqrt(arr), np.exp(arr),np.maximum(x,y),abs, fabs, square, exp, log, log10,log2,sign,ceil,floor, rint, modf, isnan,isfinte, isinf, cos, sosh,sin,sinh,tan, tanh,arccos,logical_note;  add, subtract, multiply,divide,floor_divide,power, maximum, fmin, mod, copysign, 
- stats: arr.mean(axis=1), np.mean(arr),  sum, std, var, min, max, argmin, argmax, cumsum, cumprod, 
- methods of boolean arrays: arr.any(), arr.all()
- sorting: arr.sort()
- unique: np.unique(arr);
- np.save, np.load ; np.loadtxt('filepath',delimiter=',')
- np.linalg: diag, dot, trace, det, eig, inv, pinv, qr, svd, solve, lstsq 
- random number generation: np.random.seed/permutation,shuffle, rand, randint, randn, binominal, normal, beta, chisquare, gama, uniform, 


###pandas

**Series**

---
A Series is a one-dimensional array-like object containing an array of data (of any NumPy data type) and an associated array of data labels, called its index.

---

- Series (array, index)
- convert dict to Series: Series(dict)
- pd.isnull(series),pd.notnull(series)
- obj.name = '' / obj.index.name = ' '

**DataFrame**

---
A DataFrame represents a tabular, spreadsheet-like data structure containing an or- dered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dict of Series 

---

- DataFrame(data, columns,index): df.a /df['a'] ; df.ix[x]
- Convert dic to DataFrame: DataFrame(dict)
- df.values, df.index 
- pd.Index: create index; pd.Int64Index/MultiIndex/DatetimeIndex/PeriodIndex
- Index methods: append, diff, intersection, union, isin, delete,drop,insert, is_monotoinc/is_unique/unique

**Essential Functionality**

- reindex: df.reindex([],method='ffill/pad/bfill/backfill')
- drop entries: obj.drop('x'),x could be from either axis 
- indexing, selection, slicing: obj[value],obj.ix[value]
- arithmetic and data aignment: df1.add(df2,fill_value=x), add, sub, div, mul
- operations betwen DataFrame and Series 
- functions： e.g. np.abs(df); df.apply(f,axis=1)
- df.applymap(f)
- sorting: obj.sort_index(axis=1,ascending=False,by=[value])
- Ranking; obj.order(); obj.rank(ascending=False,method='max/average/min/first')
- axis indexes with duplicate values: obj.index.is_unique
- reductions/ summary statistics: *e.g.* count,describe,min,max,sum,mean,median, mad, var, std, skew,kurt, cumsum, cummin,cummax,cumprod,diff,pct_change, *methods*:axis, skipna, level(MultiIndex), 
- df.idxmax(); df.cumsum(); df.describe();
- correlation, covariance: Series: a.corr/cov(b);DataFrame: df.corr() ; df.corrwith(df.x) 
- unque values: obj.unique()
- values count: obj.value_counts(); pd.value_counts(obj.values,sort=False)
- handling missing data: dropna, fillna, isnull, notnull
- filtering missing data: obj.dropna(how='all')
- filling missing data: df.fillna({1: 0.5, 3: -1}) or df.fillna(method='ffill/')
- hierarchical indexing: 
- reording/sorting levels: df.swaplevel(leve1,level2)
- summary sttats by level: e.g. df.sum(level='xx')

**Data Loading/Storage,File Formats**

- reading: read_csv/table/fwf/clipboard/(sep='x')
- reading fraction of files: nrows, chunksize, 
- writing data to text format: to_csv
- csv module: 
- JSON data: *json* module, json.loads(obj), json.dumps(obj),
- XML,HTML web scraping: from lxml.html import parse, from urllib2 import urlopen,
- binary data formats: 
- MS Excel: xls_file = pd.ExcelFile('xx.xls'); table = xls_file.parse('sheet1')
- Interacting with HTML / Web APIs: import *requests*
- interacting with DataBases:SQL, NoSQL, 

### Data Wrangling: clean,transform, merge, reshape

**Rearranging**

- combining& merging: pandas.merge/concat
- pd.merge(df1,df2,how='inner/outter/left/right'); other arguments: left, right, on, left_on, right_on, left_index,right_index, sort, suffixes, copy
- *concat*: e.g. pd.concat([S1,S2,S3],axis=1); other arguments: objs, axis, join, join_axes, keys, levels, names, verify_integrity, ignore_index; when axis=1, *keys* becomes column headers  
- combing data with overlap: *where*:e.g np.where(pd.isnull(a),b,a); *combine_first* :e.g. a.combine_first(b)
- reshape: stack/unstack,By default the innermost level is unstacked (same with stack). 
- pivot: e.g.  pivoted = ldata.pivot('date', 'item', 'value')

**Transformation**

- removing duplicates: e.g. data.drop_duplicates();
- functions/map: e.g.  data['animal'] = data['food'].map(str.lower).map(meat_to_animal) or  data['food'].map(lambda x: meat_to_animal[x.lower()]) /useful for categorizing/ 
- replacing values: e.g data.repalce(a,b) #replace a with b;
- renaming axis index: e.g. data.index = data.index.map(str.upper)
- discretization and binning: e.g. cats= pd.cut(data,bins), methods: *lables,levels*; pd.value_counts(cats); e.g. pd.qcut(data,4) #cut througn quantile 
- detecting and filtering outliers: 
- permutation and random sampling: np.random.permutation, e.g. df.take(np.random.permutation(len(df)))
- string manipulation: more on *regex*

--to be continued--
