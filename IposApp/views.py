import os
import tempfile
from datetime import datetime
from this import s
from tkinter.tix import PopupMenu
from turtle import pd
from urllib import response
from xmlrpc.client import DateTime
from.models import Register
from .forms import ProfileForm
from django.conf import settings
from django.db.backends import mysql
from django.shortcuts import render
import pyodbc
from django.contrib import messages
from django.contrib.sites import requests
from django.db import connections
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect
from datetime import datetime

from django.template.loader import get_template
# from easy_pdf.rendering import render_to_pdf_response
# from xhtml2pdf import pisa
from fpdf import FPDF, fpdf
# import PyPDF2
# from easy_pdf.views import PDFTemplateView

# import reportlab
import io
from django.http import FileResponse
# from reportlab.pdfgen import canvas


from IposApp.utils import render_to_pdf

conn = pyodbc.connect(
    'Driver={SQL Server Native Client 10.0};'
    f'Server=SUMMIT-6\SQLEXPRESS;'
    f'Database=SummitIPOSNEW;'
    f'UID=sa;'
    f'PWD=123;'
    'Mars_Connection=Yes;'
)
def Reg(request):
    s='pending'
    if request.method == "POST":
        CustomerName=request.POST['CustomerName']
        MobileNumber = request.POST['MobileNumber']
        NoOfPerson = request.POST['NoOfPerson']
        SelectTable = request.POST['SelectTable']
        TokenTime = request.POST['TokenTime']
        cursor = conn.cursor()
        TokenTime = datetime.now()
        query = "INSERT INTO Register(CustomerName,MobileNumber,NoOfPerson,SelectTable,TokenTime,Status) VALUES(?,?,?,?,?,?)"
        cursor.execute(query, (CustomerName, MobileNumber, NoOfPerson,SelectTable,TokenTime,s))
        conn.commit()
        # messages.success(request,'Successfully Registered...')
        

        cursor = conn.cursor()
        user = "SELECT * FROM Register WHERE id = (SELECT MAX(id)FROM Register);"
        cursor.execute(user)
        user = cursor.fetchall()
        cursor.commit()
        pdf = FPDF('P', 'mm', 'A5')
        pdf.add_page()
        pdf.set_font('Times', '',size=25)
        pdf.cell(40, 10, "Arakkal Palace", 0, 1)
        pdf.line(1, 20, 85, 20)
        pdf.line(1, 70, 85, 70)
        pdf.cell(40, 10, '', 0, 1)
        pdf.set_font('Times', '', 10)

        for line in user:
            pdf.cell(20, 8, 'CustomerName :    ' + line.CustomerName, 0, 1, '\t')
            pdf.cell(20, 8, 'MobileNumber :    ' + line.MobileNumber, 0, 1)
            pdf.cell(20, 8, 'NoOfPerson   :      ' + str(line.NoOfPerson), 0, 1)
            pdf.cell(20, 8, 'Table        :           ' + line.SelectTable, 0, 1)
            pdf.cell(20, 8, 'TokenTime    :       ' + str(line.TokenTime), 0, 1)
            pdf.cell(20, 8, 'TokenNumber      :         ' + str(line.id), 0, 1)

        filename = tempfile.mktemp('.pdf')
        open(filename, "w").readable()
        pdf.output('report.pdf', 'F')
        messages.success
        return FileResponse(open('report.pdf', 'rb'))
        # return redirect('/Reg')
    tb = conn.execute("select * from R_Table")
    return render(request, 'Registration.html',{'tb':tb})
    


def report(request,id):
    cursor=conn.cursor()
    user="SELECT * FROM Register WHERE id ="+str(id)
    cursor.execute(user)
    user=cursor.fetchall()
    cursor.commit()
    pdf = FPDF('P', 'mm', 'A5')
    pdf.add_page()
    pdf.set_font('Times', 'B', 18)

    pdf.cell(40, 10,"Arakkal Palace", 0, 1)
    pdf.line(1, 20, 80, 20)
    pdf.line(1, 70, 80, 70)
    # pdf.cell(40, 10, '', 0, 1)
    pdf.set_font('Times', 'B', 10)

    for line in user:
        pdf.cell(20, 8,'CustomerName :    ' + line.CustomerName, 0, 1,'\t')
        pdf.cell(20, 8,'MobileNumber :    ' + line.MobileNumber, 0, 1)
        pdf.cell(20, 8,'NoOfPerson   :      ' + str(line.NoOfPerson), 0, 1)
        pdf.cell(20, 8,'Table        :           ' + line.SelectTable, 0, 1)
        pdf.cell(20, 8,'TokenTime    :       ' + str(line.TokenTime), 0, 1)
        pdf.cell(20, 8,'TokenNumber      :         ' + str(line.id), 0, 1)

    filename = tempfile.mktemp('.jpg')
    open(filename, "w").readable()
    pdf.output('report.pdf', 'F') 
    return FileResponse(open('report.pdf', 'rb'))
   
   
   


def Display(request):
    cursor = conn.cursor()
    cursor.execute("select * from Register where Status='pending' order by id ASC")
    result = cursor.fetchall()
    return render(request, 'index.html', {'result': result})
k=''
def update(request,id):
    global k
    a = 'Approved'
    key = request.POST.getlist("arr[]")
    num = request.GET.dict()
    print(num)
    for k in num.values():
        print("ans:", k)
    cursor=conn.cursor()
    time="'"+str(datetime.now())+"'"
    # res="UPDATE Register SET TokenIn=CONVERT(DATETIME,getdate()) WHERE id = "+str(id)
    cursor.execute("UPDATE Register SET TokenIn=CONVERT(DATETIME,getdate()),SelectTable = ?,Status=? WHERE id ="+str(id),k,a)
    cursor.commit()
    return redirect('/Display')

k=''

def updt(request,id):
    global k
    a = 'Approved'
    key = request.POST.getlist("arr[]")
    num = request.GET.dict()
    print(num)
    for k in num.values():
        print("ans:",k)
    cursor = conn.cursor()
    cursor.execute("UPDATE Register SET Status=? SelectTable = ?  WHERE id = ?",a,k,id)
    cursor.commit()
    return redirect('/')




def show(request,id):
    cursor=conn.cursor()
    user=("Select * from Register where id="+str(id))
    cursor.execute(user)
    user=cursor.fetchone()
    tb = conn.execute("select TableNo from R_Table")
    return render(request,'Edit.html',{'user':user,'tb':tb})




m='Cancel'
def Stat(request,id):
    cursor=conn.cursor()
    cursor.execute("UPDATE Register SET Status = ? WHERE id = ?",m,id)
    conn.commit()
    # st=cursor.fetchall()
    return redirect('/Display')


def Home(request):
    return render(request,'Home.html')

def FinalReports(request):
    cursor=conn.cursor()
    cursor.execute("select * from Register order by id ASC ")
    user=cursor.fetchall()
    conn.commit()
    return render(request,'FinalReports.html',{'user':user})


























