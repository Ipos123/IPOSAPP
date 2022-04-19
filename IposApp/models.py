# import timestamp as timestamp
from django.db import models
import datetime
from django import forms
from django.forms import DateField
from django.utils import timezone

#
# Create your models here.
from Ipos import settings


class Activation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    hardwareid = models.CharField(db_column='HardwareID', max_length=100)  # Field name made lowercase.
    activationid = models.CharField(db_column='ActivationID', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activation'
#
#
class Askadminpwd(models.Model):
    code = models.BigIntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    askpwd = models.BooleanField(db_column='AskPwd', blank=True, null=True)  # Field name made lowercase.
    nodekey = models.CharField(db_column='NodeKey', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AskAdminPwd'

#
class Brdish(models.Model):
    companyid = models.IntegerField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchID')  # Field name made lowercase.
    dishid = models.IntegerField(db_column='DishID')  # Field name made lowercase.
    dirate = models.FloatField(db_column='DIRate')  # Field name made lowercase.
    tarate = models.FloatField(db_column='TARate')  # Field name made lowercase.
    hdrate = models.FloatField(db_column='HDRate')  # Field name made lowercase.
    iseffect = models.BooleanField(db_column='IsEffect')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BrDish'
        unique_together = (('companyid', 'branchid', 'dishid'),)


class Branch(models.Model):
    companyid = models.IntegerField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId')  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100)  # Field name made lowercase.
    prefix = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Branch'
        unique_together = (('companyid', 'branchid'),)

#
class Category(models.Model):
    cat_id = models.AutoField(db_column='Cat_ID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=250)  # Field name made lowercase.
    categorynamelocal = models.CharField(db_column='CategoryNameLocal', max_length=250, blank=True, null=True)  # Field name made lowercase.
    vat = models.DecimalField(db_column='VAT', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    st = models.DecimalField(db_column='ST', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sc = models.DecimalField(db_column='SC', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    kitchen = models.CharField(db_column='Kitchen', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'

#
class Creditcustomer(models.Model):
    cc_id = models.IntegerField(db_column='CC_ID', primary_key=True)  # Field name made lowercase.
    creditcustomerid = models.CharField(db_column='CreditCustomerID', max_length=30)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    openingbalance = models.DecimalField(db_column='OpeningBalance', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    openingbalancetype = models.CharField(db_column='OpeningBalanceType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate', blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditCustomer'
#

class Creditcustomerledger(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    ledgerno = models.CharField(db_column='LedgerNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=200, blank=True, null=True)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    creditcustomer = models.ForeignKey(Creditcustomer, models.DO_NOTHING, db_column='CreditCustomer_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditCustomerLedger'


class Creditcustomerpayment(models.Model):
    t_id = models.IntegerField(db_column='T_ID', primary_key=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    creditcustomer = models.ForeignKey(Creditcustomer, models.DO_NOTHING, db_column='CreditCustomer_ID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250, blank=True, null=True)  # Field name made lowercase.
    paymentmodedetails = models.CharField(db_column='PaymentModeDetails', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditCustomerPayment'


class Currency(models.Model):
    currencycode = models.CharField(db_column='CurrencyCode', primary_key=True, max_length=10)  # Field name made lowercase.
    currencyname = models.CharField(db_column='Currencyname', max_length=200)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Currency'


class Dmfooter(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    btnbackcolor = models.CharField(db_column='BTNBACKCOLOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    btnforecolor = models.CharField(db_column='BTNFORECOLOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    footerimage = models.CharField(db_column='FooterImage', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DMFooter'


class Dmheader(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    btnbackcolor = models.CharField(db_column='BTNBACKCOLOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    btnforecolor = models.CharField(db_column='BTNFORECOLOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headerimage = models.CharField(db_column='HeaderImage', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DMHeader'


class Dmheadernew(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    btnbackcolor = models.CharField(db_column='BTNBACKCOLOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    btnforecolor = models.CharField(db_column='BTNFORECOLOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headerimage = models.CharField(db_column='HeaderImage', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DMHeaderNew'


class Datatransfer(models.Model):
    dine_in = models.IntegerField(db_column='Dine-in', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ta = models.IntegerField(db_column='TA', blank=True, null=True)  # Field name made lowercase.
    hd = models.IntegerField(db_column='HD', blank=True, null=True)  # Field name made lowercase.
    journalentry = models.IntegerField(db_column='JournalEntry', blank=True, null=True)  # Field name made lowercase.
    paymententry = models.IntegerField(db_column='PaymentEntry', blank=True, null=True)  # Field name made lowercase.
    reciptentry = models.IntegerField(db_column='ReciptEntry', blank=True, null=True)  # Field name made lowercase.
    purchaseentry = models.IntegerField(db_column='PurchaseEntry', blank=True, null=True)  # Field name made lowercase.
    voucherentry = models.IntegerField(db_column='VoucherEntry', blank=True, null=True)  # Field name made lowercase.
    stocktransfer = models.IntegerField(db_column='StockTransfer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataTransfer'


class Dish(models.Model):
    dishid = models.IntegerField(db_column='DishID', primary_key=True)  # Field name made lowercase.
    dishname = models.CharField(db_column='DishName', max_length=250)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dirate = models.DecimalField(db_column='DIRate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tarate = models.DecimalField(db_column='TARate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hdrate = models.DecimalField(db_column='HDRate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mi_status = models.CharField(db_column='MI_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dishnamelocal = models.CharField(db_column='DishNameLocal', max_length=250, blank=True, null=True)  # Field name made lowercase.
    photo = models.TextField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dish'


class Emailsetting(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=150)  # Field name made lowercase.
    smtpaddress = models.CharField(db_column='SMTPAddress', max_length=250)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=200)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    tls_ssl_required = models.CharField(db_column='TLS_SSL_Required', max_length=10)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=10)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmailSetting'


class Employeeregistration(models.Model):
    empid = models.IntegerField(db_column='EmpId', primary_key=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=50)  # Field name made lowercase.
    employeename = models.CharField(db_column='EmployeeName', max_length=150)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=150)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150)  # Field name made lowercase.
    dateofjoining = models.DateTimeField(db_column='DateOfJoining')  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    islogin = models.BooleanField(db_column='IsLogin', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeRegistration'


class Expense(models.Model):
    id = models.OneToOneField('self', models.DO_NOTHING, db_column='id', primary_key=True)
    expensename = models.CharField(db_column='ExpenseName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    expense_id = models.IntegerField(db_column='Expense_Id', blank=True, null=True)  # Field name made lowercase.
    expensetype = models.CharField(db_column='ExpenseType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    openingbal = models.DecimalField(db_column='OpeningBal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    crdr = models.CharField(db_column='CrDr', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Expense'


class Expensetype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200)  # Field name made lowercase.
    accgroup = models.CharField(db_column='Accgroup', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExpenseType'


class Finyear(models.Model):
    finyearid = models.IntegerField(db_column='FinyearID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinYear'


class Gridgrouping(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    col1 = models.CharField(db_column='Col1', max_length=250)  # Field name made lowercase.
    col2 = models.IntegerField(db_column='Col2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GridGrouping'


class Hdcustomer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HDCustomer'


class Hotel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    hotelname = models.CharField(db_column='HotelName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    localname = models.CharField(db_column='LocalName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    localaddress = models.CharField(db_column='LocalAddress', max_length=250, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tin = models.CharField(db_column='TIN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stno = models.CharField(db_column='STNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cin = models.CharField(db_column='CIN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    basecurrency = models.CharField(db_column='BaseCurrency', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ticketfootermessage = models.CharField(db_column='TicketFooterMessage', max_length=250, blank=True, null=True)  # Field name made lowercase.
    showlogo = models.CharField(db_column='ShowLogo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel'


class Journal(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    debitaccount = models.CharField(db_column='DebitAccount', max_length=200, blank=True, null=True)  # Field name made lowercase.
    creditaccount = models.CharField(db_column='CreditAccount', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Journal'


class Keyboardshortcut(models.Model):
    kid = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    sysbtncaption = models.CharField(db_column='SysBtnCaption', max_length=255, blank=True, null=True)  # Field name made lowercase.
    btncaption = models.CharField(db_column='BtnCaption', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyBoardShortCut'


class Keyboardshortcutmenu(models.Model):
    kid = models.IntegerField(db_column='ID')  # Field name made lowercase.
    menuname = models.CharField(db_column='MenuName', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyBoardShortCutMenu'


class Keyboardshortcutsubmenu(models.Model):
    kid = models.IntegerField(db_column='ID')  # Field name made lowercase.
    submenutext = models.CharField(db_column='SubMenuText', max_length=250)  # Field name made lowercase.
    submenuname = models.CharField(db_column='SubMenuName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    mainmenu = models.CharField(db_column='MainMenu', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyBoardShortCutSubMenu'


class Kitchen(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    kitchenname = models.CharField(db_column='Kitchenname', max_length=200)  # Field name made lowercase.
    printer = models.CharField(db_column='Printer', max_length=250)  # Field name made lowercase.
    isenabled = models.CharField(db_column='IsEnabled', max_length=10)  # Field name made lowercase.
    nbranchid = models.IntegerField(db_column='NbranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kitchen'


class Languagedata(models.Model):
    captionid = models.IntegerField(db_column='CaptionID')  # Field name made lowercase.
    systemcaption = models.CharField(db_column='SystemCaption', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lang1 = models.CharField(db_column='Lang1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lang2 = models.CharField(db_column='Lang2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lang3 = models.CharField(db_column='Lang3', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LanguageData'


class Languagemaster(models.Model):
    langid = models.IntegerField(db_column='LANGID', blank=True, null=True)  # Field name made lowercase.
    languagename = models.CharField(db_column='LANGUAGENAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LanguageMaster'


class Ledgerbook(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ledgerno = models.CharField(db_column='LedgerNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accledger = models.CharField(db_column='AccLedger', max_length=200, blank=True, null=True)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    partyid = models.CharField(db_column='PartyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    finid = models.IntegerField(db_column='FinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LedgerBook'


class Logs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=100)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=250)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logs'


class Loyaltymember(models.Model):
    memberid = models.IntegerField(db_column='MemberID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate', blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoyaltyMember'


class Loyaltymemberledgerbook(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    ledgerno = models.CharField(db_column='LedgerNo', max_length=50)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=200)  # Field name made lowercase.
    pointsearned = models.DecimalField(db_column='PointsEarned', max_digits=18, decimal_places=3)  # Field name made lowercase.
    pointsredeem = models.DecimalField(db_column='PointsRedeem', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    billamount = models.FloatField(db_column='BillAmount', blank=True, null=True)  # Field name made lowercase.
    loyaltystatus = models.CharField(db_column='LoyaltyStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Creditcustomer, models.DO_NOTHING, db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    dvprintedat = models.DecimalField(db_column='DVPrintedAt', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    loyaltyid = models.IntegerField(db_column='LoyaltyId')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoyaltyMemberLedgerBook'


class Loyaltysetting(models.Model):
    comapnyid = models.IntegerField(db_column='ComapnyID')  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandID')  # Field name made lowercase.
    outletid = models.IntegerField(db_column='OutletID')  # Field name made lowercase.
    loyaltyid = models.IntegerField(db_column='LoyaltyID', primary_key=True)  # Field name made lowercase.
    loyaltyname = models.CharField(db_column='LoyaltyName', max_length=150)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    basepoint = models.IntegerField(db_column='BasePoint')  # Field name made lowercase.
    basevalue = models.IntegerField(db_column='BaseValue')  # Field name made lowercase.
    ltype = models.CharField(db_column='LTYPE', max_length=10)  # Field name made lowercase.
    typeamount = models.FloatField(db_column='TYPEAMOUNT')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoyaltySetting'


class Loyaltysettingdetails(models.Model):
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandID')  # Field name made lowercase.
    outletid = models.IntegerField(db_column='OutletID')  # Field name made lowercase.
    loyaltyid = models.IntegerField(db_column='LoyaltyID')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=150)  # Field name made lowercase.
    amount1 = models.FloatField(db_column='Amount1')  # Field name made lowercase.
    amount2 = models.FloatField(db_column='Amount2')  # Field name made lowercase.
    points = models.IntegerField(db_column='Points')  # Field name made lowercase.
    baseamount = models.FloatField(db_column='BaseAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoyaltySettingDetails'


class Member(models.Model):
    memberid = models.IntegerField(db_column='MemberID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate', blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member'


class Memberledger(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    ledgerno = models.CharField(db_column='LedgerNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=200, blank=True, null=True)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='MemberID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberLedger'


class Modifiers(models.Model):
    mim_id = models.AutoField(db_column='MIM_ID', primary_key=True)  # Field name made lowercase.
    modifiername = models.CharField(db_column='ModifierName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modifiers'


class Modules(models.Model):
    dinein = models.BooleanField(db_column='DineIn', blank=True, null=True)  # Field name made lowercase.
    takeaway = models.BooleanField(db_column='Takeaway', blank=True, null=True)  # Field name made lowercase.
    homedelivery = models.BooleanField(db_column='HomeDelivery', blank=True, null=True)  # Field name made lowercase.
    expressbill = models.BooleanField(db_column='ExpressBill', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    stocktran2rmused = models.BooleanField(db_column='StockTran2RMUsed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modules'


class Notesmaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=250)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotesMaster'


class Othersetting(models.Model):
    oid = models.IntegerField(db_column='ID')  # Field name made lowercase.
    parcelcharges = models.DecimalField(db_column='ParcelCharges', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    homedeliverycharges = models.DecimalField(db_column='HomeDeliveryCharges', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vat = models.DecimalField(db_column='VAT', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    servicetax = models.DecimalField(db_column='ServiceTax', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    servicecharges = models.DecimalField(db_column='ServiceCharges', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ta = models.CharField(db_column='TA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hd = models.CharField(db_column='HD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eb = models.CharField(db_column='EB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kg = models.CharField(db_column='KG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    noofpax = models.CharField(db_column='NoOfPax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    askp = models.CharField(db_column='AskP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    printloyaltypoints = models.CharField(db_column='PrintLoyaltyPoints', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arabicmenu = models.BooleanField(db_column='ArabicMenu', blank=True, null=True)  # Field name made lowercase.
    shiftstart = models.IntegerField(db_column='ShiftStart', blank=True, null=True)  # Field name made lowercase.
    shiftend = models.IntegerField(db_column='ShiftEnd', blank=True, null=True)  # Field name made lowercase.
    tablelayout = models.BooleanField(db_column='TableLayout', blank=True, null=True)  # Field name made lowercase.
    menusound = models.BooleanField(db_column='MenuSound', blank=True, null=True)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.IntegerField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherSetting'


class Payment(models.Model):
    t_id = models.IntegerField(db_column='T_ID', primary_key=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250, blank=True, null=True)  # Field name made lowercase.
    paymentmodedetails = models.CharField(db_column='PaymentModeDetails', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'


class Pizzamaster(models.Model):
    pizza_id = models.IntegerField(db_column='Pizza_ID', primary_key=True)  # Field name made lowercase.
    pizzaname = models.CharField(db_column='PizzaName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pizzasize = models.ForeignKey('Pizzasize', models.DO_NOTHING, db_column='PizzaSize', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PizzaMaster'


class Pizzasize(models.Model):
    size = models.CharField(db_column='Size', primary_key=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PizzaSize'


class Pizzatopping(models.Model):
    t_id = models.IntegerField(db_column='T_ID', primary_key=True)  # Field name made lowercase.
    toppingname = models.CharField(db_column='ToppingName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pizzasize = models.ForeignKey(Pizzasize, models.DO_NOTHING, db_column='PizzaSize', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PizzaTopping'


class Posgrouping(models.Model):
    col1 = models.CharField(db_column='Col1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col2 = models.DecimalField(db_column='Col2', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col3 = models.IntegerField(db_column='Col3', blank=True, null=True)  # Field name made lowercase.
    col4 = models.DecimalField(db_column='Col4', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col5 = models.DecimalField(db_column='Col5', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col6 = models.DecimalField(db_column='Col6', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col7 = models.DecimalField(db_column='Col7', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col8 = models.DecimalField(db_column='Col8', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col9 = models.DecimalField(db_column='Col9', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col10 = models.DecimalField(db_column='Col10', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col11 = models.DecimalField(db_column='Col11', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col12 = models.DecimalField(db_column='Col12', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col13 = models.DecimalField(db_column='Col13', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col14 = models.TextField(db_column='Col14', blank=True, null=True)  # Field name made lowercase.
    col15 = models.IntegerField(db_column='Col15', blank=True, null=True)  # Field name made lowercase.
    col16 = models.CharField(db_column='Col16', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PosGrouping'


class Posgrouping1(models.Model):
    col1 = models.CharField(db_column='Col1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col2 = models.DecimalField(db_column='Col2', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col3 = models.IntegerField(db_column='Col3', blank=True, null=True)  # Field name made lowercase.
    col4 = models.DecimalField(db_column='Col4', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col5 = models.DecimalField(db_column='Col5', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col6 = models.DecimalField(db_column='Col6', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col7 = models.DecimalField(db_column='Col7', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col8 = models.DecimalField(db_column='Col8', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col9 = models.DecimalField(db_column='Col9', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col10 = models.DecimalField(db_column='Col10', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col11 = models.DecimalField(db_column='Col11', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col12 = models.DecimalField(db_column='Col12', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col13 = models.DecimalField(db_column='Col13', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col14 = models.TextField(db_column='Col14', blank=True, null=True)  # Field name made lowercase.
    col15 = models.IntegerField(db_column='Col15', blank=True, null=True)  # Field name made lowercase.
    col16 = models.CharField(db_column='Col16', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col17 = models.FloatField(db_column='Col17', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PosGrouping1'


class PosgroupingtabTb(models.Model):
    col1 = models.IntegerField(db_column='Col1', blank=True, null=True)  # Field name made lowercase.
    col2 = models.DecimalField(db_column='Col2', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col3 = models.CharField(db_column='Col3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col4 = models.DecimalField(db_column='Col4', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col5 = models.DecimalField(db_column='Col5', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col6 = models.DecimalField(db_column='Col6', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col7 = models.DecimalField(db_column='Col7', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col8 = models.DecimalField(db_column='Col8', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col9 = models.DecimalField(db_column='Col9', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col10 = models.DecimalField(db_column='Col10', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col11 = models.DecimalField(db_column='Col11', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col12 = models.DecimalField(db_column='Col12', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col13 = models.DecimalField(db_column='Col13', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col14 = models.DecimalField(db_column='Col14', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col15 = models.CharField(db_column='Col15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col16 = models.CharField(db_column='Col16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col17 = models.DecimalField(db_column='Col17', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cols18 = models.IntegerField(db_column='Cols18', blank=True, null=True)  # Field name made lowercase.
    cols19 = models.CharField(db_column='Cols19', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PosGroupingTAB_TB'


class Posprintersetting(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tillid = models.CharField(db_column='TillID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isenabled = models.CharField(db_column='IsEnabled', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cashdrawer = models.CharField(db_column='CashDrawer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customerdisplay = models.CharField(db_column='CustomerDisplay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdport = models.CharField(db_column='CDPort', max_length=20, blank=True, null=True)  # Field name made lowercase.
    callerid = models.CharField(db_column='CallerID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calleridport = models.CharField(db_column='CallerIDPort', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smii = models.CharField(db_column='SMII', max_length=20, blank=True, null=True)  # Field name made lowercase.
    printername2 = models.CharField(db_column='PrinterName2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    printer2check = models.CharField(db_column='Printer2Check', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kotsumrychkpr1 = models.CharField(db_column='kotSumryChkpr1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billsumrychkpr1 = models.CharField(db_column='billSumryChkpr1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kotsmrychkpr2 = models.CharField(db_column='kotSmrychkpr2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billsumrychkpr2 = models.CharField(db_column='billSumryChkpr2', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PosPrinterSetting'


class Printsettings(models.Model):
    kotprintconfirmation = models.BooleanField(db_column='KOTPrintConfirmation', blank=True, null=True)  # Field name made lowercase.
    billprintconfirmation = models.BooleanField(db_column='BillPrintConfirmation', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    dineinnokot = models.BooleanField(db_column='DineinNoKOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrintSettings'


class Product(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=50)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=150, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    unit = models.IntegerField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=3)  # Field name made lowercase.
    reorderpoint = models.IntegerField(db_column='ReorderPoint')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class ProductOpeningstock(models.Model):
    ps_id = models.AutoField(db_column='PS_ID', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_ID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=4)  # Field name made lowercase.
    hasexpirydate = models.CharField(db_column='HasExpiryDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product_OpeningStock'


class Promotionsetting(models.Model):
    comapnyid = models.IntegerField(db_column='ComapnyID')  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandID')  # Field name made lowercase.
    outletid = models.IntegerField(db_column='OutletID')  # Field name made lowercase.
    promotionid = models.IntegerField(db_column='PromotionID', primary_key=True)  # Field name made lowercase.
    promotionname = models.CharField(db_column='PromotionName', max_length=150)  # Field name made lowercase.
    fdate = models.DateTimeField(db_column='FDate', blank=True, null=True)  # Field name made lowercase.
    tdate = models.DateTimeField(db_column='TDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionSetting'


class Purchase(models.Model):
    st_id = models.IntegerField(db_column='ST_ID', primary_key=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=30)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    purchasetype = models.CharField(db_column='PurchaseType', max_length=20)  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_ID')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=18, decimal_places=3)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=2)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=18, decimal_places=3)  # Field name made lowercase.
    previousdue = models.DecimalField(db_column='PreviousDue', max_digits=18, decimal_places=3)  # Field name made lowercase.
    freightcharges = models.DecimalField(db_column='FreightCharges', max_digits=18, decimal_places=3)  # Field name made lowercase.
    othercharges = models.DecimalField(db_column='OtherCharges', max_digits=18, decimal_places=3)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=18, decimal_places=3)  # Field name made lowercase.
    roundoff = models.DecimalField(db_column='RoundOff', max_digits=18, decimal_places=3)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3)  # Field name made lowercase.
    totalpayment = models.DecimalField(db_column='TotalPayment', max_digits=18, decimal_places=3)  # Field name made lowercase.
    paymentdue = models.DecimalField(db_column='PaymentDue', max_digits=18, decimal_places=3)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    hst = models.DecimalField(db_column='HST', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hstper = models.DecimalField(db_column='HSTPer', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchase'


class Purchaseorder(models.Model):
    po_id = models.IntegerField(db_column='PO_ID', primary_key=True)  # Field name made lowercase.
    ponumber = models.CharField(db_column='PONumber', max_length=50)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supplier_ID', blank=True, null=True)  # Field name made lowercase.
    terms = models.TextField(db_column='Terms', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    potopur = models.BooleanField(db_column='POTOPUR')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrder'


class PurchaseorderJoin(models.Model):
    poj_id = models.AutoField(db_column='POJ_ID', primary_key=True)  # Field name made lowercase.
    purchaseorderid = models.IntegerField(db_column='PurchaseOrderID')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=2)  # Field name made lowercase.
    priceperunit = models.DecimalField(db_column='PricePerUnit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_ID')  # Field name made lowercase.
    unit_id = models.IntegerField(db_column='Unit_id', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrder_Join'


class PurchaseJoin(models.Model):
    sp_id = models.AutoField(db_column='SP_ID', primary_key=True)  # Field name made lowercase.
    purchaseid = models.ForeignKey(Purchase, models.DO_NOTHING, db_column='PurchaseID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=3)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3)  # Field name made lowercase.
    unit_id = models.IntegerField(db_column='Unit_Id', blank=True, null=True)  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_ID')  # Field name made lowercase.
    hasexpirydate = models.CharField(db_column='HasExpirydate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchase_Join'


class Rmcategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RMCategory'


class RmUsed(models.Model):
    rm_id = models.IntegerField(db_column='RM_ID', primary_key=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RM_Used'


class RmUsedJoin(models.Model):
    rmj_id = models.AutoField(db_column='RMJ_ID', primary_key=True)  # Field name made lowercase.
    rawmaterialid = models.ForeignKey(RmUsed, models.DO_NOTHING, db_column='RawMaterialID', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RM_Used_Join'

#
class RTable(models.Model):
    tableno = models.CharField(db_column='TableNo', primary_key=True, max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    bkcolor = models.IntegerField(db_column='BkColor')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    available = models.CharField(db_column='Available', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bgcolor = models.CharField(db_column='BGcolor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_Table'

    def __str__(self):
        return self.tableno
#
#
class Recipe(models.Model):
    r_id = models.IntegerField(db_column='R_ID', primary_key=True)  # Field name made lowercase.
    recipename = models.CharField(db_column='RecipeName', max_length=200)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id')  # Field name made lowercase.
    fixedcost = models.DecimalField(db_column='FixedCost', max_digits=18, decimal_places=3)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipe'


class RecipeJoin(models.Model):
    rj_id = models.AutoField(db_column='RJ_ID', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='RecipeID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costperunit = models.DecimalField(db_column='CostPerUnit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalitemcost = models.DecimalField(db_column='TotalItemCost', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unit_id = models.IntegerField(db_column='Unit_Id', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipe_Join'




class Register(models.Model):
    customername = models.CharField(db_column='CustomerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    noofperson = models.IntegerField(db_column='NoOfPerson', blank=True, null=True)  # Field name made lowercase.
    selecttable = models.CharField(db_column='SelectTable', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tokentime = models.DateTimeField(db_column='TokenTime', auto_now_add=True)  # Field name made lowercase.
    tokenin = models.DateTimeField(db_column='TokenIn', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Register'






class Registration(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=100)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.DateTimeField(db_column='JoiningDate')  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registration'


class RestaurantposBillinginfoeb(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=15)  # Field name made lowercase.
    odn = models.CharField(db_column='ODN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    ebdiscountper = models.DecimalField(db_column='EBDiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ebdiscountamt = models.DecimalField(db_column='EBDiscountAmt', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cash = models.DecimalField(db_column='Cash', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billnote = models.TextField(db_column='BillNote', blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=18, decimal_places=3)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eb_status = models.CharField(db_column='EB_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='Member_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eb_phoneno = models.CharField(db_column='EB_PhoneNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_BillingInfoEB'


class RestaurantposBillinginfohd(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=15)  # Field name made lowercase.
    odn = models.CharField(db_column='ODN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hddiscountper = models.DecimalField(db_column='HDDiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    hddiscountamt = models.DecimalField(db_column='HDDiscountAmt', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    homedeliverycharges = models.DecimalField(db_column='HomeDeliveryCharges', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employee = models.ForeignKey(Employeeregistration, models.DO_NOTHING, db_column='Employee_ID')  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=50)  # Field name made lowercase.
    billnote = models.TextField(db_column='BillNote', blank=True, null=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='Member_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hd_status = models.CharField(db_column='HD_Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_BillingInfoHD'


class RestaurantposBillinginfokot(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    odn = models.CharField(db_column='ODN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kotdiscountper = models.DecimalField(db_column='KOTDiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kotdiscountamt = models.DecimalField(db_column='KOTDiscountAmt', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cash = models.DecimalField(db_column='Cash', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='Member_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    waiter = models.CharField(db_column='Waiter', max_length=200, blank=True, null=True)  # Field name made lowercase.
    noofpax = models.IntegerField(db_column='NoOfPax', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(blank=True, null=True)
    dbillno = models.IntegerField(db_column='Dbillno', blank=True, null=True)  # Field name made lowercase.
    finid = models.IntegerField(db_column='FinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_BillingInfoKOT'


class RestaurantposBillinginfota(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=15)  # Field name made lowercase.
    odn = models.CharField(db_column='ODN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tadiscountper = models.DecimalField(db_column='TADiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tadiscountamt = models.DecimalField(db_column='TADiscountAmt', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    parcelcharges = models.DecimalField(db_column='ParcelCharges', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cash = models.DecimalField(db_column='Cash', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billnote = models.TextField(db_column='BillNote', blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='Member_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ta_status = models.CharField(db_column='TA_Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    finid = models.IntegerField(db_column='FinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_BillingInfoTA'


class RestaurantposOrderinfokot(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ticketno = models.CharField(db_column='TicketNo', max_length=15)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tableno = models.ForeignKey(RTable, models.DO_NOTHING, db_column='TableNo', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ticketnote = models.TextField(db_column='TicketNote', blank=True, null=True)  # Field name made lowercase.
    kot_status = models.CharField(db_column='KOT_Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    noofpax = models.IntegerField(db_column='NoOfPax', blank=True, null=True)  # Field name made lowercase.
    tillid = models.CharField(db_column='TillID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sostatus = models.CharField(db_column='SOStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderInfoKOT'


class RestaurantposOrderinfokotso(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ticketno = models.CharField(db_column='TicketNo', max_length=15)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate')  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tableno = models.CharField(db_column='TableNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ticketnote = models.TextField(db_column='TicketNote', blank=True, null=True)  # Field name made lowercase.
    kot_status = models.CharField(db_column='KOT_Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    noofpax = models.IntegerField(db_column='NoOfPax', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tillid = models.CharField(db_column='TillID', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderInfoKOTSO'


class RestaurantposOrderedproductbilleb(models.Model):
    op_id = models.AutoField(db_column='OP_ID', primary_key=True)  # Field name made lowercase.
    billid = models.ForeignKey(RestaurantposBillinginfoeb, models.DO_NOTHING, db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stper = models.DecimalField(db_column='STPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamount = models.DecimalField(db_column='STAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scper = models.DecimalField(db_column='SCPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamount = models.DecimalField(db_column='SCAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderedProductBillEB'


class RestaurantposOrderedproductbillhd(models.Model):
    op_id = models.AutoField(db_column='OP_ID', primary_key=True)  # Field name made lowercase.
    billid = models.ForeignKey(RestaurantposBillinginfohd, models.DO_NOTHING, db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stper = models.DecimalField(db_column='STPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamount = models.DecimalField(db_column='STAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scper = models.DecimalField(db_column='SCPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamount = models.DecimalField(db_column='SCAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderedProductBillHD'


class RestaurantposOrderedproductbillkot(models.Model):
    op_id = models.AutoField(db_column='OP_ID', primary_key=True)  # Field name made lowercase.
    billid = models.ForeignKey(RestaurantposBillinginfokot, models.DO_NOTHING, db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stper = models.DecimalField(db_column='STPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamount = models.DecimalField(db_column='STAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scper = models.DecimalField(db_column='SCPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamount = models.DecimalField(db_column='SCAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tableno = models.ForeignKey(RTable, models.DO_NOTHING, db_column='TableNo', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dishid = models.IntegerField(db_column='DishID', blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderedProductBillKOT'


class RestaurantposOrderedproductbillta(models.Model):
    op_id = models.AutoField(db_column='OP_ID', primary_key=True)  # Field name made lowercase.
    billid = models.ForeignKey(RestaurantposBillinginfota, models.DO_NOTHING, db_column='BillID', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stper = models.DecimalField(db_column='STPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamount = models.DecimalField(db_column='STAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scper = models.DecimalField(db_column='SCPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamount = models.DecimalField(db_column='SCAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_id', blank=True, null=True)  # Field name made lowercase.
    dishid = models.IntegerField(db_column='DishID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kottime = models.TimeField(db_column='KotTime', blank=True, null=True)  # Field name made lowercase.
    readytime = models.TimeField(db_column='ReadyTime', blank=True, null=True)  # Field name made lowercase.
    deliverdtime = models.TimeField(db_column='DeliverdTime', blank=True, null=True)  # Field name made lowercase.
    fdstatus = models.CharField(db_column='FdStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderedProductBillTA'


class RestaurantposOrderedproductkot(models.Model):
    op_id = models.AutoField(db_column='OP_ID', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey(RestaurantposOrderinfokot, models.DO_NOTHING, db_column='TicketID', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stper = models.DecimalField(db_column='STPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamount = models.DecimalField(db_column='STAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scper = models.DecimalField(db_column='SCPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamount = models.DecimalField(db_column='SCAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t_number = models.CharField(db_column='T_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    oquantity = models.FloatField(db_column='OQuantity', blank=True, null=True)  # Field name made lowercase.
    dishid = models.IntegerField(db_column='DishID', blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_id', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kottime = models.TimeField(db_column='KotTime', blank=True, null=True)  # Field name made lowercase.
    readytime = models.TimeField(db_column='ReadyTime', blank=True, null=True)  # Field name made lowercase.
    deliverdtime = models.TimeField(db_column='DeliverdTime', blank=True, null=True)  # Field name made lowercase.
    fdstatus = models.CharField(db_column='Fdstatus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderedProductKOT'


class RestaurantposOrderedproductkotso(models.Model):
    op_id = models.AutoField(db_column='OP_ID', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey(RestaurantposOrderinfokotso, models.DO_NOTHING, db_column='TicketID', blank=True, null=True)  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vatper = models.DecimalField(db_column='VATPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stper = models.DecimalField(db_column='STPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamount = models.DecimalField(db_column='STAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    scper = models.DecimalField(db_column='SCPer', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    scamount = models.DecimalField(db_column='SCAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    discountper = models.DecimalField(db_column='DiscountPer', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.DecimalField(db_column='DiscountAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    cat_id = models.IntegerField(db_column='Cat_Id', blank=True, null=True)  # Field name made lowercase.
    t_number = models.CharField(db_column='T_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    oquantity = models.FloatField(db_column='OQuantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantPOS_OrderedProductKOTSO'


class Smssetting(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    apiurl = models.TextField(db_column='APIURL')  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=10)  # Field name made lowercase.
    isenabled = models.CharField(db_column='IsEnabled', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSSetting'


class StockadjustmentStore(models.Model):
    sa_id = models.IntegerField(db_column='SA_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    adjustmenttype = models.CharField(db_column='AdjustmentType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockAdjustment_Store'


class StockadjustmentWarehouse(models.Model):
    sa_id = models.IntegerField(db_column='SA_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_ID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    adjustmenttype = models.CharField(db_column='AdjustmentType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    physicalstock = models.DecimalField(db_column='PhysicalStock', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockAdjustment_Warehouse'


class Stocktransfer(models.Model):
    st = models.OneToOneField('self', models.DO_NOTHING, db_column='ST_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    kitchen_id = models.IntegerField(db_column='Kitchen_Id')  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_Id')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockTransfer'


class StocktransferJoin(models.Model):
    stj_id = models.AutoField(db_column='STJ_ID', primary_key=True)  # Field name made lowercase.
    stocktransferid = models.IntegerField(db_column='StockTransferID')  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_ID')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockTransfer_Join'


class StockStore(models.Model):
    st_id = models.IntegerField(db_column='St_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock_Store'


class StockStoreJoin(models.Model):
    ssj_id = models.AutoField(db_column='SSJ_ID', primary_key=True)  # Field name made lowercase.
    stockid = models.IntegerField(db_column='StockID')  # Field name made lowercase.
    dish_id = models.IntegerField(db_column='Dish_Id')  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock_Store_Join'


class Supplier(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=30)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=150, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    tin = models.CharField(db_column='TIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stno = models.CharField(db_column='STNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=150, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ifsccode = models.CharField(db_column='IFSCCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    openingbalance = models.DecimalField(db_column='OpeningBalance', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    openingbalancetype = models.CharField(db_column='OpeningBalanceType', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'


class Supplierledgerbook(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    ledgerno = models.CharField(db_column='LedgerNo', max_length=50)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=200)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=18, decimal_places=3)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=18, decimal_places=3)  # Field name made lowercase.
    partyid = models.CharField(db_column='PartyID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierLedgerBook'


class Tablelayout(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    btnid = models.IntegerField(db_column='BtnID', blank=True, null=True)  # Field name made lowercase.
    btncaption = models.CharField(db_column='BtnCaption', max_length=20, blank=True, null=True)  # Field name made lowercase.
    btnname = models.CharField(db_column='btnName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    btnleft = models.IntegerField(db_column='btnLeft', blank=True, null=True)  # Field name made lowercase.
    btntop = models.IntegerField(blank=True, null=True)
    btncolor = models.IntegerField(db_column='btnColor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableLayout'


class Templedger(models.Model):
    expensename = models.CharField(db_column='ExpenseName', max_length=250)  # Field name made lowercase.
    expensetype = models.CharField(db_column='ExpenseType', max_length=200)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=38, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=38, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempLedger'


class TempStock(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.
    warehouse_id = models.IntegerField(db_column='Warehouse_ID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=2)  # Field name made lowercase.
    hasexpirydate = models.CharField(db_column='HasExpiryDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_Stock'


class TempStockRm(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_Stock_RM'


class TempStockStore(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    dish = models.CharField(db_column='Dish', max_length=250)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_Stock_Store'


class UisettingsTb(models.Model):
    menubtnhight = models.IntegerField(db_column='MenuBtnhight', blank=True, null=True)  # Field name made lowercase.
    menubtnwidth = models.IntegerField(db_column='MenuBtnWidth', blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='Branchid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UIsettings_Tb'


class Unitmaster(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnitMaster'


class Voucher(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', max_length=30)  # Field name made lowercase.
    expense_id = models.IntegerField(db_column='Expense_Id', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=150)  # Field name made lowercase.
    grandtotal = models.DecimalField(db_column='GrandTotal', max_digits=18, decimal_places=3)  # Field name made lowercase.
    vat = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Voucher'


class VoucherOtherdetails(models.Model):
    vd_id = models.AutoField(db_column='VD_ID', primary_key=True)  # Field name made lowercase.
    voucherid = models.ForeignKey(Voucher, models.DO_NOTHING, db_column='VoucherID')  # Field name made lowercase.
    particulars = models.IntegerField(db_column='Particulars')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    vat = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Voucher_OtherDetails'


class Wallet(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    wallettype = models.CharField(db_column='WalletType', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wallet'


class Warehouse(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    warehousetype = models.IntegerField(db_column='WarehouseType', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Warehouse'


class Warehousetype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WarehouseType'


class Workperiodend(models.Model):
    id = models. OneToOneField('Workperiodstart', models.DO_NOTHING, db_column='Id', primary_key=True)  # Field name made lowercase.
    wpend = models.DateTimeField(db_column='WPEnd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkPeriodEnd'


class Workperiodstart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    wpstart = models.DateTimeField(db_column='WPStart')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkPeriodStart'
#
#
class HistoryStore(models.Model):
    timemark = models.DateTimeField()
    table_name = models.CharField(primary_key=True, max_length=50)
    pk_date_src = models.CharField(max_length=400)
    pk_date_dest = models.CharField(max_length=400)
    record_state = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'history_store'
        unique_together = (('table_name', 'pk_date_dest'),)


class Ledgerbooknew(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accledger = models.CharField(db_column='AccLedger', max_length=200, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ledgerno = models.CharField(db_column='LedgerNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    partyid = models.CharField(db_column='PartyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.
    ledgergroup = models.CharField(db_column='LedgerGroup', max_length=150, blank=True, null=True)  # Field name made lowercase.
    finid = models.IntegerField(db_column='FinID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ledgerBookNew'


class Tblbillprinting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='BillDate', blank=True, null=True)  # Field name made lowercase.
    isprint = models.BooleanField(db_column='IsPrint', blank=True, null=True)  # Field name made lowercase.
    printedon = models.DateTimeField(db_column='PrintedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBillPrinting'


class Tblkotprinting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ticketno = models.CharField(db_column='TicketNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ticketdate = models.DateTimeField(db_column='TicketDate', blank=True, null=True)  # Field name made lowercase.
    isprint = models.BooleanField(db_column='IsPrint', blank=True, null=True)  # Field name made lowercase.
    printedon = models.DateTimeField(db_column='PrintedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblKOTPrinting'


class Tblorder(models.Model):
    od_id = models.AutoField(db_column='OD_ID', primary_key=True)  # Field name made lowercase.
    odno = models.IntegerField(db_column='ODNo')  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOrder'
#
#
class Tempexpense(models.Model):
    voucherno = models.CharField(db_column='VoucherNo', max_length=30)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    name = models.CharField(max_length=250)
    total = models.DecimalField(max_digits=18, decimal_places=3)
    vat = models.DecimalField(db_column='Vat', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(max_digits=19, decimal_places=3, blank=True, null=True)
    expensetype = models.CharField(db_column='ExpenseType', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempExpense'
#
#
class Temppayment(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='PaymentMode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=3)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempPayment'
#

class Temppurchase(models.Model):
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=30)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=30)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=18, decimal_places=3)  # Field name made lowercase.
    vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    invoicetotal = models.DecimalField(db_column='invoiceTotal', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempPurchase'
#
#
class Tempstockadjmntwarehos(models.Model):
    sa_id = models.IntegerField(db_column='SA_ID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    warehouse = models.IntegerField(db_column='Warehouse', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    adjustmenttype = models.CharField(db_column='AdjustmentType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branchid = models.IntegerField(db_column='BranchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempStockAdjmntWarehos'

#
