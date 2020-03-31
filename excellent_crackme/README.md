# Excellent Crackme
We know one can do pretty much everything in Excel spreadsheets, but this...

[excel_crackme](VolgaCTF_excel_crackme.xlsm)

Open the excel file:
![Capture](Capture.PNG)

```vb6
Private Sub VolgaCTF()
Dim input As String
Dim fpqigdwkxf As Long
Dim hiedpuxyvs As Long
Dim CLAO4r As Long
input = Range("L15")
For i = 1 To Len(input)
	fpqigdwkxf = 0
	For j = 1 To Len(input)
		hiedpuxyvs = CInt(Cells(99 + i, 99 + j).Value)
		c = Mid(input, j, 1)
		fpqigdwkxf = fpqigdwkxf + hiedpuxyvs * Asc(c)
	Next j
	CLAO4r = CLng(Cells(99 + i, 99 + Len(input) + 1).Value)
	If (CLAO4r <> fpqigdwkxf) Then
		MsgBox "Wrong Flag!"
		Exit Sub
	End If
Next i
MsgBox "Congratz"
End Sub
```