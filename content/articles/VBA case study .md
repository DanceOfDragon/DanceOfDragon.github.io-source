Title: VBA-case study 1
Date: 2015-08-30 18:40
Modified: 2015-08-30 18:50
Tags: tech-iT
Category:Blog/English
Slug: vba case study 1
Author: JIN Lin

This is the case study I was given at an interview with [Mars Singapore](http://www.mars.com/global/index.aspx). Only in real fight does the truth be revealed. Obviously, ~~I need to practice more, much more~~ Practicing!

**Objective** 

> At the end of the 1 hr, you should have created a chart to display **retention rate** per quarter, and you will also be asked to explain your steps / logic. May ignore quarters that aren't complete (e.g. Q3 2013)

**Definition**

- Retention rate is calculated for experience entrepreneurs (EE) only.
- Experienced entrepreneur (EE): Entrepreneur who has at least 3 months of sales data (i.e. He/She becomes EE at the end of the 3rd months with sales). Entrepreneurs with less than 3 months of experience are considered as new entrepreneurs (NE).
- Retention rate for EE: Out of all the EE that started a period, how many % ended that period. Calculation of retention rate = (EE at start of period - EE dropped during period) / EE at start of period
- EE at start of period + EE joined during period - EE dropped during period = EE at end of period
- How does an EE drop out? When there are 3 consecutive months of no sales (i.e. drops at the end of the 3rd month without sales)
- After an EE dropped and joins again, he is an EE immediately.


**Examples**

![example](https://dl.dropboxusercontent.com/u/18094167/BlogImages/VBA%20Examples1.png)

sample retention rate for Q2, Q3

Q2: month4 - month6 

EE at start of the period: 7

EE dropped out during the period: 3

retention rate:  4/7x100%  =  57%

Q3:moth7 - month9

EE at start of the period: 5

EE dropped out during the period: 3

retention rate: 40%


**Full Dataset**

Download full dataset [here @ VBA-case study 1](https://dl.dropboxusercontent.com/u/18094167/VBA%20case%20study%201.xlsx).

**My Approach**

*Analysis*

- Q1 starts from January and ends in March,rigorously. The same logic applies to Q2,Q3,Q4. ( Each company has its own fisical year, define in this way to avoid complexity coming from random starting of a quarter. Otherwise, a more complex model to calcualte retention rate per month).
- Algorithm:
	1. Convert sales data to rating of the entrepreneurs (NE,EE or dropout). All data needed to calculate the retention rate should be by far ready.
	2. Count the EE at the start of each quater, N1_start;
	3. Count the EE dropouts within each quarter,N1_dropuouts; 
	4. Count the newly joined EE during the period,N1_new;
	5. Calculate the retention rate for each quater,(N1_start -N1_dropuouts)/N1_start.  


- divide and conquer the essential first step

	- EE: 
		- at least 3 months of sales data (no need to be consecutive; 0 could indicate no sale, in Excel it will be empty cell);
		- returning EE dropouts become EE immediately; 
	- NE: less than 3 months' sales; 
	- Dropuouts: 3 or more consecutive months of no sales;
	- Entrepreneurs are independent from each other, so the method of converting sales data to rating will be apply to each one repeatedly.(Iteration) 

	
**Note**
After checking abnormal results calculated from the codes, I found that some "empty-appearing" cells are actually not empty, which causes big problems. One way to solve the problem is to *clear contents* of those "empty cells". 


	sample code to clear contents of 'empty cell'
		
		For Each c In Selection
     		If Len(c) = 0 Then c.ClearContents
		Next c

Algorithm:


	1) Conversion
	
	  matrix consisting of four different status: 
	 	Empty
	 	NE
	 	EE
	 	Dropout 
	 	
	 a counts Number of EE; b counts number of empty cells
	 
	 a = 0: empty
	 a = 1, 2: NE
	 	b < 3 NE
	 	b = 3 (consecutive, no data+1,data reset to 0):dropuout;
	 	b >= 4 empty
	 	
	 a >= 3: EE
	 	b < 3 EE
	 	b = 3 (consecutive, no data+1,data reset to 0):dropuout;
	 	b >= 4 empty
	 
	 2)Calculation
	 
	 for Quater k (row i, column j,j+1,j+2)
	 
	 	retented EE: (i,j)&(i,j+1)&(i,j+2) true 
	 	EE at the start: All EE at column j
	 	retention rate:   
	 
	 
	
**Code**


	Option Explicit	Sub RetentionRate()    Dim xrow, xcol, x, y, i, j As Integer    'xrow: number of rows    'xcol: number of columns    'x-rowl;y -col    'i count NE/EE    'j count dropout    Dim sht, shtB, shtC As Worksheet    Dim rng As Range        Set sht = ThisWorkbook.Sheets(2)    Set shtB = ThisWorkbook.Sheets(3) ' storing output of converted data    Set shtC = ThisWorkbook.Sheets(4) ' tracking the change of counters, for debugging    Set rng = sht.UsedRange        xrow = rng.Rows.Count    'count the rows in the usedrange, rng.row returns the first row number        xcol = rng.Columns.Count    'count the columns in the used range        'copy table titles        sht.Columns("A:B").Copy Destination:=shtB.Columns("A:B")    sht.Rows(1).Copy Destination:=shtB.Rows(1)        ' convert raw data'        'clear fake empty cells        For Each rng In sht.UsedRange        If Len(rng) = 0 Then rng.ClearContents    Next rng            For x = 2 To xrow   'by default starting from 0, starting from the second row                 i = 0        j = 0                For y = 3 To xcol ' col0-area officer; col1-entrepreneur                    If IsEmpty(sht.Cells(x, y).Value) = False Then  'test if the cells contain data                i = i + 1                j = 0                shtC.Cells(x, y) = i                    Select Case i                        Case 1                        shtB.Cells(x, y).Value = "NE"                        Case 2                        shtB.Cells(x, y).Value = "NE"                        Case Is >= 3                        shtB.Cells(x, y).Value = "EE"                    End Select            Else                j = j + 1                shtC.Cells(x, y) = i                                Select Case i                    Case Is >= 3                        If j < 3 Then                            shtB.Cells(x, y).Value = "EE"                        ElseIf j = 3 Then                            shtB.Cells(x, y).Value = "dropout"                        Else                            shtB.Cells(x, y).Value = " "                        End If                     Case 2                         If j < 3 Then                            shtB.Cells(x, y).Value = "NE"                        ElseIf j = 3 Then                            shtB.Cells(x, y).Value = "dropout"                        Else                            shtB.Cells(x, y).Value = " "                        End If                    Case 1                        If j < 3 Then                            shtB.Cells(x, y).Value = "NE"                        ElseIf j = 3 Then                            shtB.Cells(x, y).Value = "dropout"                        Else                            shtB.Cells(x, y).Value = " "                        End If                    Case 0                        shtB.Cells(x, y).Value = ""                End Select                                      End If            Next y           Next x            'Calcualte retention rate            For y = 3 To xcol        i = 0        j = 0        If (y - 1) Mod 3 = 0 Then                        For x = 2 To xrow                 'sum up all EE at the start of each quater                If shtB.Cells(x, y).Value = "EE" Then i = i + 1                'sum up the dropouts of EE within each quater                If shtB.Cells(x, y).Value = "EE" And shtB.Cells(x, y + 1).Value = "EE" And shtB.Cells(x, y + 2).Value = "EE" Then j = j + 1                            Next x                    shtB.Cells(xrow + 1, y).Value = i                        shtB.Cells(xrow + 2, y).Value = j                            'calculate retention rate            If i <> 0 And j <> 0 Then                shtB.Cells(xrow + 3, y).Value = j / i                shtB.Cells(xrow + 4, y).Value = sht.Cells(1, y).Value            Else                shtB.Cells(xrow + 3, y).Value = "N.A."            End If        Else        End If    Next y
 End Sub**Here's [the code](https://dl.dropboxusercontent.com/u/18094167/vba-case%20study%201-Code.bas) **

There's more could be done with this set of data. For example, evaluate the performance of the area officers based on the retention rate of the entrepreneurs.Or evaluate the performance of the entrepreneurs. 

         