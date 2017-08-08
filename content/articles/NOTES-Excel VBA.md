Title:Notes:Excel VBA 
Date: 2015-08-14 20:40
Modified: 2015-08-14 21:10
Tags: tech-iT 
Category: Blog/English
Slug: notes-excel-vba
Author: JIN Lin
[TOC]

### 1. Macros vs. VBA 
- VBA- Visual Basic Applications 
- Essentially, both are realised by some codes except that Macros requires only a few clikcs while VBA requires requires  you to type down the codes. 
- It is faster and easier to create Macros but it also means less flexibility. VBA in this case offers much flexibile and powerful options through which you can call APIs, read and write all kinds of files, access other databases, and create dashboards or userforms etc. 
- It is probably enough to eliminate minor repetitions by just using Macros,or functions. Of course VBA is cooler. 


###2. Terminology 
- **"Procedure"**: Procedures, which might include multiple actions, is to do one task. *Sub* and *Functions* are used most often. 
- **"Module"**: A module is where the procedures are stored. 
- **"Object"**: Objects are the items to be controlled. They include *Workbook*,*Worksheet*,*Range*,*Cell*,*Charts* etc. 
- **"Property"**: Properties are the characteristics of an Objects which can be measured and quantified.e.g. Range("A1").Value, here *value* is the property of *Range("A1")*. A property could become an object. e.g. Range("A1").Font.Size. *Font* is the property of *Range* meanwhile the object of its property *Size*.
- **"Method"**:Methods are the actions that can be performed by an Object or on an Object.e.g.Range("A1").Select. *Select* is the action on *Range*. Obejects, and their Methods and Properties could be browsed in the VBE (integrated VB Editor).
- **"Event"**Events are actions performed by users which trigger Excel VBA to execute code. 

###3. VBE 
Just an example window. It can be adjusted to suit your favor. This is where codes are written and editted. 
  

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/19923031923/in/dateposted-public/" title="vbe-init"><img src="https://farm6.staticflickr.com/5689/19923031923_f355f31837_n.jpg" width="279" height="320" alt="vbe-init"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

It includes:

- Menu bar  
- Tool bar 
- Project window:including *Excel Objects*(Sheets and ThisWorkbook),*Forms*, *Modules* and 
- Properties window: press F4 to open. 
- Code window
- Immdiate window. CTRL + ALT + I to open. Write code and press Return to excute. 
- F1: HELP. Who knows better than those developed the VBA? 

###4. Basics

####4.1 Varaibles 
##### 4.1.1 Variables: Name Convention
- Less than 255 characters;
- No spacing;
- It must not begin with a number;
- Period is not permitted;
- Do not use key syntax defined by VBA, e.g. Workbook, Range


##### 4.1.2 Variables: Data Types

Excel is like a grocery store where all types of things are sold. To lump the same types of things under one label is easier to manage and search. 

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/20518360866/in/dateposted-public/" title="Excel-VBA-Variable-Types"><img src="https://farm6.staticflickr.com/5697/20518360866_2e9a660209.jpg" width="500" height="443" alt="Excel-VBA-Variable-Types"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

By default, the type is *Variant*.

##### 4.1.3 Variables: Declaration

**Syntax**:

	Dim (Variable_Name) As (Data Type)
	e.g.
		Dim str As String
		Dim Birthdate As Date
		Dim x As Integer 
	or multiple variables 
		Dim str As String, x As Integer  'in one line 
		

 **Option Explicit**

	Option Explicit { On | Off } 
	
	'by default is On. Force explicit delcaration of all variables. 

Since it is more efficient if EXCEL knows exactly what type of the variable is, you can force to declare the data types(in case you forget) rather than use the default one by turning on the *option explicit*.It can be set in the tool bar.

**Scope** 

	Public (Variable_Name) As (Data_Type) 
		'used across all modules 
		
	Private (Variable_Name) As (Data_Type)
		'used in single module,(Dim does so)
		
	Static (Variable_Name) As (Data_Type)
		'used in single procedure such as *Sub* or *Functions* (as Dim) 

**Assignment**


LET 

	[Let] Variable_Name = data 
		'Let could be implicit
		'data are mumberic such as date, integer
	e.g.
		[Let] str = "Hello, World!" 
		Range("A1").Value = str  
SET

	Set Variable_Name = data 
		' Set is a must
		' data is Object such Range,Cells etc.
	e.g.
	Sub ass1()
		Dim rng As Range
		Set rng = Worksheets("sheet1").Range("A1")
		rng.value = "Welcome to My Blog!"
	End Sub
	
**Constant**


Constants like pi, tax rate are better represented by a constant variable.

	Const 	(Variable_Name) As (Data_Type) = data
	e.g.
		Const pi As Single = 3.14
		' either declare within a procedure or a module
		
**Array**

This is where a matrix of different types of data could be manipulated. 

Declaration
 

	Public|Dim (Array_Name(a to b)) As (Data_Type) 
		'either use Public or Dim
		'a to b is the starting and ending index number; or use one number to indicate the largest index number
		'Option Base {0 | 1} by default the numbering starts from 0
	e.g.
		Dim Class1(1 To 50) As String
		
Assignment

	Class1(1) = "David"
	.
	.
	.
	Class1(50) = "Lily"
	
Dimension

	Dim Dim (Array_Name(a to b, c to d)) As (Data_Type)
		' a to b - rows 
		' c to d - columns
		' could expand to even more dimensions
		
Dynamic Array

	Dim arr() As String 
		'together with ReDim to better accommondate unknown number of data
	e.g.
	Sub countempty()
		Dim arr() As String
		Dim n As Long
		n = Application.WorksheetFunction.CountA(Range("A:A"))
		ReDim arr(1 To n) As String
	End Sub
	
Other Ways to Create Array

*Array* Function


	Dim arr As Variant 
	arr = Array(1,3,4,5,7)

*Split* Function

	Dim arr As Variant 
	arr = Array("David,Tony,Tome,Lily,Lucy",",")
	
*Range* Object

	Dim arr As Variant
	arr = Range("A1:G3").Value
		
*Bound*

	UBound(arr) ' return maximum index number 
	LBound(arr) ' return minimum index number 
	
	the number of elements in the array is therefore 
	UBound(arr) - LBound(arr) +1 
	
*Joint*

	e.g.
		arr = (1,3,5)
		txt = Joint(arr,"@")
		
	return 
		txt = (1@3@5)
		
		
*Write into Cells* 

	e.g.
		arr = Array(1,3,5,7,9)
		Range("A1:A5")= Application.WorksheetFunction.Transpose(arr)
		'size and dimension of the range should be the same as the array


####4.2 Objects/Properties/Methods 

Obejcts

	e.g.
		Application.Workbooks("Book1").Worksheets("sheet1").Range("A2")
	If sheet1 is the active worksheet,simply write the relative address
		Range("A2") 
		

Properties

	Application.Workbooks("Book1").Worksheets("sheet1").Range("A2").Font.Color
	
Methods

	Methods are about what is done by the object or to the object, properties are about what the object has/includes. 
	
	
####4.3 Operators

The precedence of all these operators is the same as other language such as Python. A full list could be found here [VBA Operators Summary](http://onlinelibrary.wiley.com/store/10.1002/9781118390405.app4/asset/app4.pdf?v=1&t=idbb6bev&s=faca84fd5f25030d9d227a960f362715cc8093d9). 

*Arithmetic*
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/19938771784/in/dateposted-public/" title="VBA-arithmetic operators"><img src="https://farm6.staticflickr.com/5758/19938771784_e6e0824144.jpg" width="500" height="481" alt="VBA-arithmetic operators"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

*Comparison*

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/19940509343/in/dateposted-public/" title="VBA-comparison operators"><img src="https://farm6.staticflickr.com/5668/19940509343_03790c7ea7.jpg" width="500" height="467" alt="VBA-comparison operators"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


*Logical*

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/19938771584/in/dateposted-public/" title="VBA-logic operators 1"><img src="https://farm6.staticflickr.com/5689/19938771584_bd8d791d9b.jpg" width="500" height="258" alt="VBA-logic operators 1"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/20373375110/in/dateposted-public/" title="VBA-logic operators 2"><img src="https://farm6.staticflickr.com/5788/20373375110_4a5db544a4.jpg" width="500" height="188" alt="VBA-logic operators 2"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


*Others*

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/20373375120/in/dateposted-public/" title="VBA-Miscellaneous Operators"><img src="https://farm6.staticflickr.com/5625/20373375120_e9601d5e82.jpg" width="500" height="442" alt="VBA-Miscellaneous Operators"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

  
####4.4 Built-in Functions

Employ these readily available functions to save time. 


	e.g. 
		Time() ' return system time
		Date()	' return system date
		Abs(a) ' return the absolute number 
	more on HELP


####4.5 Syntaxes

#####4.5.1 If...Then

	If (conditional statement) Then (action) Else (xx)
	e.g.
		If Time<0.5 Then MsgBox "Good Morning!" Else MsgBox "Good afternoon"
	
	OR In block form 
		If Time<0.5 Then
		MsgBox "Good Morning!"
		Else
		MsgBox "Good afternoon"
		End If     'must end with End If
 
 
 multiple choices

	If ... Then
	...
	ElseIf... Then
	...
	Else 
	...
	End If 

#####4.5.2 Select...Case

This is more suitable when more than 3 choices are to be determined. Once Select finds the matched condition, it will executes under that condition and jump off the the Select process. Put the most likely condition foremost to increase efficiency.  

	Select Case (Variable_Name)
		Case <condition1>
			...
		Case <condition2>
			...
		...
	End Select
	
#####4.5.3 For...Next

	For (iteration_variable=<initial value> To <end value>)[Step size]
		...
		[Exit For]  'when encounter this sentence, exit the loop. 
	 	...
	Next [iteration_variable]
	
	e.g. write 1 to 100 to column A
	Sub ex2()
		Dim i As Integer
		xrow = 1
		For i = 1 To 100  'by default, step size is 1
			Cells(xrow,"A").Value = i 
			xrow = xrow + 1
		Next              'iteration_variable can be ignored 
	End Sub

#####4.5.4 Do... While

	Do <While logical statements>    ' when True,execute until it returns False
		...
		[Exit Do]
		...
	Loop 

OR 


	Do 
		...
		[Exit Do]
		...
	Loop <While logical statements>  ' When False exit the iteration
	
#####4.5.5 Do...Until

Contrary to Do...While, Do Until executes when the Logical statement is False, and exits when it is True. 

	Do <Until logical statements>    ' when False,execute until it returns True
		...
		[Exit Do]
		...
	Loop 
OR

	Do 
		...
		[Exit Do]
		...
	Loop <Until logical statements>  ' When True exit the iteration
	
#####4.5.6 For Each...Next

When the number of iterations is unknown, For... Next is a bit problematic. 

	For Each (variable) In (objects/arrays)
		...
		[Exit For]
		...
	Next <variable>

e.g.

	Sub ex3()
		Dim sht As Worksheet, i As Integer
		i = 1
		For Each sht In Worksheets 'all worksheets in current workbooks 
			Cells(i,"A")=sht.Name 'write the sheet name to cell (1,A)
			i = i +1
		Next sht
	End Sub

#####4.5.7 Other Common Syntaxes

**GoTo** 

	e.g.
	
	Sub he()
	Dim mysum as long, i as integer 
	i = 1 
	X: mysum = mysum + 1  'X label
		i = i + 1
		If i<=100 Then GoTo X  'when i<=100, go back to X label
		MsgBox "sum of natural number 1 to 100" & mysum
	End Sub

**With**

It helps remove the repetition of the codes with the same structure.

e.g.

	With Worksheet("sheet1").Range("A1").Font
		.Name = "Times"
		.Size = 12
		.ColorIndex = 3
		.Bold = True
	End With 
	
####4.6 Procedures
#####4.6.1 Sub
Sub is a set of actions to do certain task. When recording a Macro, it creates a Sub procedure which is stored in a moudule.

Declare a Sub 

	[Public|Private|Static] Sub sub_name()
		...
		[Exit Sub]
		...
	End Sub
	
	'Private Subs can only be used within in the same Module

Run Sub_a in Sub_b

	Sub Sub_b()
		Call Sub_a[(variable1,variable2...)]
		'or Application.Run "Sub_a[(variable1,variable2...)]"
	End Sub  
	

#####4.6.2 Function

Excel has quite a lot basic yet powerful functions but still might not solve particular problems faced with. For instance, counting the yellow box in one sheet. The customer function could be used in either VBA or Excel Spreadsheets.

Declare a Function 
	
	[Public|Private|Static] Function function_name([variable list])[As data type] 'returned data type
		...
		[Exit Function]
		...
		function_name = results 'a must
	End Function


####4.7 Better Code

- Indent properly
- Avoid long sentence
- Combine trivial lines
- Write clear comments 

###5. Objects

The following chapters expand above subjects with more details.

####5.1 Common Objects

Object Hierarchy

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/108107823@N04/20563347155/in/dateposted-public/" title="excelobjectchart"><img src="https://farm6.staticflickr.com/5637/20563347155_9d5876520b.jpg" width="500" height="183" alt="excelobjectchart"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

#####5.1.1 Application
Property: `ScreenUpdating`

	Application.ScreenUpdating = True | False 
	'by default True, results will be shown on screen.
	
	e.g.
	Sub ex4()
		Cells.ClearContents
		Application.ScreenUpdating = False
		Range("A1:A10") = 100            ' intermediate results won't be shown on screen.
		MsgBox "can you see the results?"
		Range("B1:B10") = 200
		MsgBox "can you see the results?" 
		Application.ScreenUpdating = True
	End Sub

Property: `DisplayAlerts`

	Application.DisplayAlerts = True | False

Property: `EnableEvents`

Event, e.g. open/close the workbook,select a cell etc.

	e.g.
	Private Sub Workbook_SelectionChange(ByVal,Target As Range)
		Target.Value = Target.Address
	End Sub
	'select one cell and it will automatically reutrn the cell address.

Disable an Event


	Private Sub Workbook_SelectionChange(ByVal,Target As Range)
		Target.Value = Target.Address
		Target.Offset(1,0).Select    'it will again return an address and select another cell, resulting an endless process. 
	End Sub

To prevent this:


	Private Sub Workbook_SelectionChange(ByVal,Target As Range)
		Target.Value = Target.Address
		Application.EnableEvents = False  'it will offset by one cell but wont return an address and offset onemore time
		Target.Offset(1,0).Select    
		Application.EnableEvents = True
	End Sub
	
Property: `WorksheetFunction`

In VBA, there is no COUNTIF,SUMIF,TRANSPOSE,or VLOOKUP etc. To use them, call them by using the following syntax:

	Application.WorksheetFunction.CountIf(...)
	
	'if VBA already has the function,say fun_a, same as that in Excel, use fun_a() instead of WorksheetFunction.fun_a()
	
Other Properties:


	Application
		.Caption          'Excel title
		.DisplayFormulaBar'
		.StatusBar      (True|False)
		.DisplayHeadings 
	
		.ActiveCell    'Application can be ignored
		.ActiveChart
		.ActiveSheet
		.ActiveWindow
		.ActiveWorkbook
		.Charts   'all charts in the active window
		.Selection
		.Sheets
		.Worksheets
		.Workbooks
		
#####5.1.2 Workbook

Call Workbook

	Workbooks.Item(1)
	Workbooks(1)
	Workbooks("Book1.xls")
	
Create Workbook

	Workbooks.Add 'blank excel'
	Workbooks.Add("full name")
	Workbooks.Add xlWBATCHART
	
Open Workbook

	Workboos.Open Filename :="E:\Book1.xls"
	or 
	Workboos.Open "E:\Book1.xls"
	
Acitivate Workbook

	Workbooks("Book1.xls").Active
	
Save Workbook

	Workbooks("Book1").Save
	Workbooks("Book1").SaveAs Filename :="full name" 'close original file,open new
	Workbooks("Book1").SaveCopyAs Filename :="full name" 'keep original file,do not open new'
	
Close Workbook

	Workbooks.Close  'close all files
	Workbooks("Book1").Close
	Workbooks("Book1").Close savechanges :=True
	
	
#####5.1.3 Worksheet

Call Worksheet

	Worksheets.Item()
	Worksheets()
	Worksheets("")
	
Create Worksheet

	Worksheets.add
	Worksheets.add Before := Worksheets(1) 'insert one before sheet1'
	Worksheets.add After := Worksheets(1)
	Worksheets.add Count:=3 'inset 3 worksheets'
	Worksheets.add After := Worksheets(1),Count := 3 'inset 3 after sheet1
	
Edit Worksheet Name

	Worksheets(1).Nmae = "salary sheet"
	ActiveSheet.Name = "salary sheet"
	Worksheets.add(Before := Worksheets(1)).Name = "salary sheet"
	
Delete Worksheet

	Worksheets(1).Delete
	
Activate Worksheet

	Worksheets(1).Activate
	Worksheets(1).Select
	
Copy Worksheet

	Worksheets(1).Copy 
	
Move Worksheet

	Worksheets(1).Move before := Worksheets("salary sheet")
	
Display Worksheet

	Worksheets(1).Visible = True 
	
Count Worksheets

	Worksheets.Count 			

Sheets vs. Worksheets

	Sheets: include all types of worksheets, charts,macro,normal
	Worksheets: normal spreadsheet

#####5.1.4 Range (essential)

Basic actions

	e.g.
	
	Worksheets("Sheet1").Range("A1").Value = 50 
    Range("A1:B10").Value = 100
    Range("date").Value =100   'Define date as A1:B10'
    Range("A1:B10,E1:F5").Select
    
    Range("A1:B10 B1:F5").Select 
    	'choose the common area
    
    Range("B6:B10","D2:D8").Select  
    	'return the smallest rectangle encompassing both regions.
Cells 

	e.g.
	
	ActiveSheet.Cells(3,4).Value = 100  'row 3 column 4/D
	ActiveSheet.Cells(3,"D").Value = 100
	...................
	Range("B3:F9").Cells(2,3).Value = 100 	.................
	
	Rnage(Cells(1,1),Cells(10,5)).Select   
	=
	Range("A1","E10").Select 
	=
	Range(Range("A1"),Range("E10")).Select 
	
Rows

	e.g.
	
	ActiveSheet.Rows("3:5").Select 'row3 to row5'
	ActiveSheet.Rows.Select  
	Rows("3:10").Rows(1).Select    'row3
	
Columns 

	e.g. 
	ActiveSheet.Columns("E:F").Select
	
Union

	Application.Union(Range("A1:A10"),Range("e1:e5")).Select 
	'link discrete sections and select together 

Offset 

	e.g.
	Range("A1").Offset(2,3).Value = 50 'down 2 rows, right 3 columns'
	
	Range("A1").Offset(-2,3).Value = 50  'up 2 rows
Resize

	e.g.
	Range("A1").Resize(5,4).Select  'expand one cell to one region 
	Range("B2:E6").Resize(2,1).Select 'contract one region to one cell

UsedRange

	e.g.
	Worksheets.UsedRange.Select 
	'return one rectangle box including all  used region including empty rows or columns if regions are seperated. 
	
CurrentRegion

	Worksheets.Range("A1").CurrentRegion.Select 
	'bordered with empty rows or columns, A1 is in the region.F5
	
End

	return the end cell in the specified direction of current region. It is very useful when we need to append / replace data to current table.
	e.g.
	Range("C5").End(xlUP/xlDown/xlToLeft/xlToRight)
	
	Range("A6536").End(xlUP).Offset(1,0).Value="Tom" 
		'Range("A6536").End(xlUP) goes to last filled cell  
		'append new data 'Tom' to current table, 
	
Value

	value is the default property of Range, so 
	Range("A1") = "SB" is valid.
	
Count

	ActiveSheet.UsedRegion.Rows.Count
	ActiveSheet.UsedRegion.Columns.Count
	
Address

	e.g.
	Selection.Address
	
Select & Activate

	Range("A1:A10").Select
		equivalent to
	Range("A1;A10").Activate

Clear 

	A cell contains data,format,comments etc.
	Range("A1").Clear 'clear all, contents, formats,and comments
			   .ClearComments
			   .ClearContents
			   .ClearFormats
Copy

	e.g. 
	Range("A1").Copy [Destination :=] Range("C1") 
		'[] could be ignored.
	
	Range("A1").CurrentRegion.Copy Range("C1')
		'C1 is the upper left corner of the region
Cut
	
	e.g.
	Range("A1").Cut [Destination :=] Range("C1")
	
Delete

	Different from clear, delete remove the cells rather than only the contents etc.
	e.g.
	
	Range("A5").Delete Shift:= xlToLeft  'delete A5 and shift to left'
	Range("A5").Delete Shift:= xlUp  'delete A5 and cells move up'
	Range("A5").EntireRow.Delete  
	Range("A5").EntireColumn.Delete 
	
Names

	e.g.
	ActiveWorkbook.Names.Add Name := "date" , RefersToR1C1 := "=Sheet1!R5C[-2]" 
		'R-ROW;C-COLUMN, [] indicates relative position,no [] means absolute position.
	
	OR A1 format
	
	ActiveWorkbook.Names.Add Name := "date" , RefersTo := "=Sheet1!$B$4"

	OR Simply
	
	Range("A1:A10").Name = 'date'
	
Comment

	e.g.
	Range("A1").AddComment Text := "This is cool!"
	OR
	Range("A1").Comment.Text = "comment" 
	
	Range("A1").Comment.Visible = False 
	Range("A1").Comment.Delete 

Font

	e.g.
	With Range("A1").Font
 		.Name = "宋体"
 		.Size = 12 
 		.Color = RGB(225,225,0)
 		.Bold = True 
 		.Italic = True
 		.Underline = xlUnderlineStyleDouble 
 	End With
 	 
Interior

	e.g.
	Range("A1").Interior.Color = RGB(225,225,0)

Border

	e.g.
	With Range("A1").CurrentRegion.Borders
 		.LineStyle = xlContinuous 
 		.Color = RGB(0,0,225)
 		.Weight = xlHairline
 	End With 
 
 Others	on HELP
 
 
	
###6. Events

Automatic response to some actions.

Worksheet_Change() 

	When data in cells are changed,Return message
	e.g.
	Private Sub Worksheet_Change(ByVal Target As Range)
		Application.EnableEvents = False
		MsgBox Target.Value =  "version1：" & Target.Value 
		Application.EnableEvents = True
	End Sub
	
Worksheet_SelectionChange()

	e.g.
	Private Sub Worksheet_SelectionChange(ByVal Target As Range)

		If Target.column <> 1 Then
			Cells(Target.Row,"A").Select   
		End If 
	End Sub

Worksheet_Activate()

	e.g. show worksheet name 
	
	Private Sub Worksheet_Activate(ByVal Target As Range)
		MsgBox "the current worksheet name is：" & ActiveSheet.Name
	End Sub	
	
Worksheet_Deactivate()

	e.g. deactivate other sheets except Sheet1
	
	Private Sub Worksheet_Deactivate(ByVal Target As Range)
		MsgBox "choose only sheet1！"
		Worksheets("Sheet1").Select
	End Sub
Other events:

	Worksheet_BeforeDoubleClick
	Worksheet_Calculate 
	Worksheet_BeforeRightClick
	Worksheet_FollowHyperlink
	Worksheet_PivotTableUpdate
	...
	
Workbook Events (Just some examples)

	Workbook_Open
	Workbook_BeforeClose
	Workbook_SheetChange
	Workbook_AddinInstall
	Workbook_AddinUnstall
	Workbook_AfterXmlImport
	Workbook_BeforePrint
	Workbook_BeforeSave
	Workbook_BeforeXmlExport
	Workbook_NewSheet
	Workbook_PivotTableCloseConnection
	Workbook_PivotTableOpenConnection
	
###7. Next
	
Here comes the end of some basics of the Excel VBA. What follows is one or more projects that build upon these basics and the **Interatice UserForm** as well. 








