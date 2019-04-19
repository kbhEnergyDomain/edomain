from django import forms 
from .models import Customer, Bid, Royalties, Dblistings

CustomerFields = ( 'title', 'cust_fname', 'cust_lname', 'cust_no', 'email' , 'phone', 'mobile', 
			'cust_address1', 'cust_city', 'cust_zipcode', 'cust_state' )
class CustomerForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args,**kwargs)
		#self.fields['cust_id'].widget.attrs['readonly'] = True
	
	class Meta: 
		model = Customer 
		#fields  =  CustomerFields
		exclude  = ('image', 'sign_date','credit')


class RoyaltiesForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(RoyaltiesForm, self).__init__(*args,**kwargs)
		#self.fields['cust_id'].widget.attrs['readonly'] = True
		self.fields['check_date'] = forms.DateTimeField(label="Check Date", initial="1999-03-10",
					widget=forms.SelectDateWidget(years=YEARS))
	class Meta: 
		model = Royalties 
		fields  = [ 'user_name', 'check_amount', 'check_date', 'check_number', 'document']
		#exclude  = ('image', 'sign_date','credit')



YEARS = [ x for x in range(1960,2020)]
class BidForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BidForm, self).__init__(*args,**kwargs)
		#self.fields['cust_id'].widget.attrs['readonly'] = True
		self.fields['sdate'] = forms.DateTimeField(label="Date of Bid", initial="1999-03-10",
					widget=forms.SelectDateWidget(years=YEARS))
		self.fields['sexpire'] = forms.DateTimeField(label="Bid Expires", initial="1999-05-10",
					required=False, 
					widget=forms.SelectDateWidget(years=YEARS))

	class Meta: 
		model = Bid 
		#fields  =  CustomerFields
		exclude  = ('state',)


 # 	  oid = models.ForeignKey('Ownership', models.DO_NOTHING, db_column='oid')
 #    sdate = models.DateTimeField()
 #    sexpire = models.DateTimeField()
 #    svalue = models.FloatField(blank=True, null=True)
 #    state = models.IntegerField()
 #    bidder = models.IntegerField(blank=True, null=True)


class DblistingsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DblistingsForm, self).__init__(*args,**kwargs)
		#self.fields['oid'].widget.attrs['readonly'] = True
		self.fields['state'].widget.attrs['readonly'] = True
		self.fields['state'].initial = 1
		self.fields['ondate'] = forms.DateTimeField(label="Date of Dblistings", initial="1999-03-10",
					widget=forms.SelectDateWidget(years=YEARS))
		self.fields['sexpire'] = forms.DateTimeField(label="Dblistings Expires", initial="1999-05-10",
					required=False, 
					widget=forms.SelectDateWidget(years=YEARS))


	class Meta: 
		model = Dblistings	
		#fields  =  CustomerFields
		exclude  = ('oid', 'bidid', 'soldvalue', 'solddate', 'soldto')
		#fields  = [ 'state', 'ondate', 'askvalue']