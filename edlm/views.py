from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.views.generic import TemplateView , DeleteView
from django.db.models import Count
# Create your views here.
from edlm.models import Wells, Customer, Assetinformation, Ownership, Assettype 
from edlm.models import Tractstable, Leasestable, Royalties, Bid
from chartjs.views.lines import BaseLineChartView
from .forms import CustomerForm, CustomerFields, BidForm, RoyaltiesForm, DblistingsForm	
from django.views.decorators.csrf import csrf_exempt
# Approach #1
#import json
# def return_json_data(query,cursor, )
#    cur = mysql.connection.cursor()
#    cur.execute('''SELECT * FROM Users WHERE id=1''')
#    row_headers=[x[0] for x in cur.description] #this will extract row headers
#    rv = cur.fetchall()
#    json_data=[]
#    for result in rv:
#         json_data.append(dict(zip(row_headers,result)))
#    return json.dumps(json_data)

# Approach 2: 
# def some_view(request):
#     data = list(SomeModel.objects.values())
#     return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})

# Approach 3: 
# # sfrom django.core import serializers
# from django.http import HttpResponse

# def some_view(request):
#     qs = SomeModel.objects.all()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')

def setMWdata(request):

	r = request.POST.get("sell")
	print(r)
	return HttpResponse("Hello World")

@csrf_exempt
def getMWdata(request):
	print(request.POST.keys())
	r = request.POST.get('mdata')
	print(request.body)

	return HttpResponse("Hello World")


def dblistings_new(request):
	#mybid = Bid.objects.get()

	if request.method == 'POST':
		form = DblistingsForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'dblistings_edit.html', 
					{'form':form});
	else:
		form = DblistingsForm(); 
	return render(request, 'dblistings_edit.html', {'form': form , 'saved' : '....'})


def dblistings_edit(request, pk=None):
	print("Request to list asset ID = ", pk)
	try:
		asset =  Assetinformation.objects.get(rid=pk) 
	except: 
		asset = None

	whoami = Customer.objects.get(user_name=self.request.user)
	oid    = whoami.cust_id	 

	# Ownership record --- pk
	

	owner_info = Ownership.objects.get(aid=pk)
	print("Customer	ID", owner_info.cid)
	cust = owner_info.cid; 
	owner_str = "%s %s" % (cust.cust_fname, cust.cust_lname)
	asset = owner_info.aid
	asset_str = "%d - " % asset.asset_no
	print("Owner ", owner_str)
	print("Asset Info", asset_str)
	if item: item.oid = owner_info
	if request.method == 'POST':
		form = DblistingsForm(request.POST, instance=item)
		if form.is_valid():
			print(form)
			form.save() 
		return render(request, 'dblistings_edit.html', {'form': form , 
					'owner' : owner_str, 'asset' : asset_str, 
					'saved' : 'saved'})
	else:
		if not item:
			form = DblistingsForm()
		else:
			form = DblistingsForm(instance=item)
	return render(request, 'dblistings_edit.html', {'form': form , 
						'owner' : owner_str, 'asset' : asset_str, 
						'saved' : '....'})



def bid_new(request):
	#mybid = Bid.objects.get()

	if request.method == 'POST':
		form = BidForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'bid_edit.html', 
					{'form':form});
	else:
		form = BidForm(); 
	return render(request, 'bid_edit.html', {'form': form , 'saved' : '....'})

def royalties_edit(request, pk):
	print("request", pk)
	try:
		item = Royalties.objects.get(rid=pk) 
	except: 
		item = None

	if request.method == 'POST':
		form = RoyaltiesForm(request.POST, instance=item)
		if form.is_valid():
			#user = form.save(commit=False)
			#form = CustomerForm(instance=myuser[0])
			form.save() 
		return render(request, 'royalties_edit.html', {'form': form , 'saved' : 'saved'})
	else:
		if not item:
			form = RoyaltiesForm()
		else:
			form = RoyaltiesForm(instance=item)
	return render(request, 'royalties_edit.html', {'form': form , 'saved' : '....'})


class RoyaltiesDelete(DeleteView):
	template_name='deleteConfirmation.html'
	model=Royalties
	success_url='/home'

def royalties_delete(request,pk):

	obj = get_object_or_404(Royalties, pk=pk).delete()
	print("obj", obj)

	response = redirect("/home")
	return response
	#return render(request, 'royalties_edit.html')


def royalties_new(request):
	myroyalty = None

	if request.method == 'POST':
		form =  RoyaltiesForm(request.POST, instance = myroyalty)
		if form.is_valid():
			#user = form.save(commit=False)
			#form = CustomerForm(instance=myuser[0])
			form.save() 
			print("Collected ...", request.user.username, request.POST)
			#myuser.save()
			return render(request, 'royalties_edit.html', {'form': form , 'saved' : 'saved'})
	else: 
		form = RoyaltiesForm()

	return render(request, 'royalties_edit.html', {'form': form , 'saved' : '....'})


def customer_new(request ):
	myuser = Customer.objects.get(user_name=request.user.username)
	
	if request.method == 'POST':
		form = CustomerForm(request.POST, instance = myuser)
		if form.is_valid():
			#user = form.save(commit=False)
			#form = CustomerForm(instance=myuser[0])
			form.save() 
			print("Collected ...", request.user.username, request.POST)
			#myuser.save()
			return render(request, 'customer_edit.html', {'form': form , 'saved' : 'saved'})
	else: 
		if myuser: 
			form = CustomerForm(instance=myuser)
		else: 
			form = CustomerForm()


	return render(request, 'customer_edit.html', {'form': form , 'saved' : '....'})


#--------------------------------------------------------------
class homePageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'index.html'

	def getAssetTabData(self):
		listings = [] 
		# From ownership 
		try:
			whoami = Customer.objects.get(user_name=self.request.user)
		except: 
			response = redirect("/login")
			return response

		print("Who am I?", whoami.cust_id, self.request.user)
		mystuff = Ownership.objects.filter(cid=whoami.cust_id)
		print(mystuff)
		for stuff in mystuff: 
			print(stuff.aid, stuff.cid)
			otype = Assettype.objects.get(asset_type_id=stuff.aid.atype)
			
			item = { 'AID': stuff.aid.asset_id, 
					'Atype': otype.asset_name, 'WELL' : stuff.aid.well_id } 
			listings.append(item)

		return listings


	def getBidData(self,**kwargs):
		bs  = Bid.objects.all() 
		listings = [] 
		# self.request.user ... is the user name 
		for bid in bs:
			bidder = Customer.objects.get(cust_id = bid.bidder)
			name = "%s,%s" % ( bidder.cust_lname, bidder.cust_fname)
			listings.append(
 				{ 'id' : bid.bid_id, 'who': name,  'Amount' : bid.svalue },	
				)
		return listings


	def getPaymentData(self, **kwargs):
		payments = [ ] 

		rt2 = Royalties.objects.filter(user_name=self.request.user) 
		print(rt2)
		for rt in rt2[:10]:
			payments.append( { 'check_date': rt.check_date, 
								'check_amount': rt.check_amount, 
								'rid': rt.rid, 
								'check_number': rt.check_number})

		return payments

	def get_context_data(self, **kwargs):
		tabData = { } 

		# customers = Customer.objects.all() 
		# print(customers)

		assetData = self.getAssetTabData(); 
		bidData = self.getBidData(); 
		paymentData = self.getPaymentData();

		listingData = [  
				{ 'id' : 'ID 1',  'where': 'Yonder', 'Amount' :1000.00 },
				{ 'id' : 'ID 2', 'where': 'Over there',  'Amount' : 2000.00 },
				{ 'id' : 'ID 3', 'where': 'Here',  'Amount': 1300.00 },
				  ]

		tabData['assets'] = assetData; 
		tabData['bids'] =   bidData; 
		tabData['listings'] = listingData; 
		tabData['payments'] = paymentData; 


		return tabData; 


class listingsPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'listings.html'


	def getListingData(self):
		listings = [] 

		# customers = Customer.objects.all() 
		# print(customers)
		tracts  = Tractstable.objects.all()
		for tract in tracts: 
			print(tract)
			listings.append({ 'ID': tract.tract_id, 
				'acres': tract.gross_acres, 
				'legal': tract.legal_description, 
				'county': tract.county })
		return listings


	def get_context_data(self, **kwargs):
		listings = 	self.getListingData() 
		return { 'listings' : listings }




class assetsPageView(TemplateView):

	template_name = 'assets.html'


	def getListingData(self):
		listings = [] 
		rt2 = Royalties.objects.all().values('owner_name', 'operator_name', 'interest_type').annotate(total=Count('owner_name')).order_by('total')
	#{'owner_name': 'ALFSON ANDERSON INVESTMENTS LLC', 'operator_name': 'CONOCOPHILLIPS COMPANY', 'interest_type': 'NORTH DAKOTA WITHHOLDING TAX', 'total': 1}
		for owner in rt2:
			listings.append(owner)
		return listings


	def get_context_data(self, **kwargs):
		listings = 	self.getListingData() 
		return { 'listings' : listings }




class buyersPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'buyers.html'
	model = Wells 

class sellersPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'sellers.html'
	model = Wells 

class brokersPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'brokers.html'
	model = Wells 

class mapsPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'maps.html'
	model = Wells 

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:100]
		mapData = {}
		mapData['allwells'] =  allwells
		mapData['shortlist'] =  allwells[:30]
		mapData['centerY']  =  allwells[0].well_latt
		mapData['centerX']  =  allwells[0].well_long

		return mapData; 
			


	


class reportsPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'reports.html'
	model = Wells 
	#allwells = Wells.objects.all() 
	#print(allwells)

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:25]
		return { 'allwells' : allwells}

class forsalePageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'forSale.html'
	model = Wells 
	#allwells = Wells.objects.all() 
	#print(allwells)

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:25]
		return { 'allwells' : allwells}

class bidformPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'bidForm.html'
	model = Wells 
	#allwells = Wells.objects.all() 
	#print(allwells)

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:25]
		return { 'allwells' : allwells}


class bidacceptPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'bidAccept.html'
	model = Wells 
	#allwells = Wells.objects.all() 
	#print(allwells)

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:25]
		return { 'allwells' : allwells}

class bidstatusPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'bidStatus.html'
	model = Wells 
	#allwells = Wells.objects.all() 
	#print(allwells)

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:25]
		return { 'allwells' : allwells}


class confirmsalePageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'confirmSale.html'
	model = Wells 
	#allwells = Wells.objects.all() 
	#print(allwells)

	def get_context_data(self, **kwargs):
		allwells = Wells.objects.all()[:25]
		return { 'allwells' : allwells}

#========================= Data ==================================
def get_Royalty_Owners(request, *args, **kwargs): 
	myowners = Royalties.objects.values('owner_name').distinct()
	data = {
		'owners': [ x['owner_name'] for x in myowners ]
	}
	return JsonResponse(data)

# Examples include: 
# data = list(SomeModel.objects.values())
# return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})


class LineChartJSONView(TemplateView):
	template_name = 'line_chart.html'

	def get_context_data(self, **kwargs):
		context = super(LineChartJSONView, self).get_context_data(**kwargs)
		context['gas_revenue'] = self.revenue_data('GAS')
		context['oil_revenue'] = self.revenue_data('OIL')
		context['labels'] = [ x for x in range(50)]
		return context

	def revenue_data(self,code):
		final_data = []
		rg = Royalties.objects.filter(product_code=code)
		rlen = len(rg)
		for day in range(1, rlen):
			date = rg[day].check_date; 
			count = rg[day].owner_net_value;
			final_data.append(count)

		return final_data




class detailedPageView(TemplateView):
	#return HttpResponse("Hello World")
	template_name = 'details.html'
	model = Wells 
	allwells = Wells.objects.all() 
	#print(allwells)


		
	def get_context_data(self, *args, **kwargs):
		context = super(detailedPageView, self).get_context_data(**kwargs)
		context['gas_revenue'] = self.revenue_data('GAS')
		context['oil_revenue'] = self.revenue_data('OIL')
		context['labels'] = [ x for x in range(50)]

		print(kwargs.get('ID'))
		context['owner'] = kwargs.get('ID')
	
		return context

	def revenue_data(self,code):
		final_data = []
		rg = Royalties.objects.filter(product_code=code)
		rlen = len(rg)
		for day in range(1, rlen):
			date = rg[day].check_date; 
			count = rg[day].owner_net_value;
			final_data.append(count)

		return final_data
