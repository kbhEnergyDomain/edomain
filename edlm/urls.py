from django.urls import path 

from . import views 

urlpatterns = [ 
	path('', views.homePageView.as_view(), name ='home'),
	path('home', views.homePageView.as_view(), name ='hem2'),
	path('sellers', views.sellersPageView.as_view(), name ='sellers'),
	path('buyers', views.buyersPageView.as_view(), name ='buyers'),
	path('brokers', views.brokersPageView.as_view(), name ='brokers'),
	path('assets', views.assetsPageView.as_view(), name ='assets'),
	#path('signup', views.signupPageView.as_view(), name ='signup'),

	path(r'details/<str:ID>', views.detailedPageView.as_view(), name ='details'),
	#path(r'showdetails', views.showdetails, name ='showdetails'),
	path('reports', views.reportsPageView.as_view(), name ='reports'),
	path('maps', views.mapsPageView.as_view(), name ='maps'),
	path('listings', views.listingsPageView.as_view(), name ='listings'),
	path('forsale', views.mapsPageView.as_view(), name ='forsale'),
	path('bidform', views.bidformPageView.as_view(), name ='bidform'),
	path('bidaccept', views.bidacceptPageView.as_view(), name ='bidaccept'),
	path('bidstatus', views.bidstatusPageView.as_view(), name ='bidstatus'),
	path('confirmsale', views.confirmsalePageView.as_view(), name ='confirmsale'),
	path('api/getRoyaltyOwners', views.get_Royalty_Owners, name ='getRoyaltyOwners'),
	path('linechart', views.LineChartJSONView.as_view(), name ='linechart'),
	path('customer/new/', views.customer_new, name='customer_new'),
	path('royalties/new/', views.royalties_new, name='royalties_new'),
	path('bid/new/', views.bid_new, name='bid_new'),
	path('dblistings/new/', views.dblistings_new, name='dblistings_new'),
	path(r'dblistings/edit/', views.dblistings_edit, name='dblistings_edit'),
	path(r'dblistings/edit/(?P<pk>\d+)/', views.dblistings_edit, name='dblistings_edit'),
	path(r'dblistings/new/(?P<pk>\d+)/', views.dblistings_new, name='dblistings_new'),
	path('getMWdata/', views.getMWdata, name='getMWdata'),
	path('setMWdata/', views.setMWdata, name='setMWdata'),
	path(r'royalties/edit/(?P<pk>\d+)/', views.royalties_edit, name='royalties_edit'),
	path(r'royalties/delete/(?P<pk>\d+)/', views.RoyaltiesDelete.as_view(), name='royalties_delete'),
	#path(r'royalties/delete/(?P<pk>\d+)/$', views.royalties_delete, name='royalties_delete'),

]