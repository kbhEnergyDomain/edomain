# coding: utf-8
k = Royalties.objects.all()
len(k) 
rt = Royalites.objects.all().values('owner_name')
rt = Royalties.objects.all().values('owner_name')
rt
rt = Royalties.objects.all().values('owner_name')
rt.keys()
rt[0].keys()
rt[0]
rt = Royalties.objects.all().values('owner_name').distinct()
rt
rt = Royalties.objects.all().values_list('owner_name').distinct()
rt
b = [ i for i in rt ] 
b
from django.db.models import Counnt
from django.db.models import Count
rt2 = Royalties.objects.all().values('owner_name').annotate(total=Count('owner_name')).order_by('total') 
rt2
rt2 = Royalties.objects.all().values('owner_name', 'operator_name').annotate(total=Count('owner_name')).order_by('total') 
rt2
rt2 = Royalties.objects.all().values('owner_name', 'operator_name', 'net_value').annotate(total=Count('owner_name')).order_by('total') 
rt2
rt2 = Royalties.objects.all().values('owner_name', 'operator_name', 'prod_date').annotate(total=Count('owner_name')).order_by('total') 
rt2
len(rt2)
rt3 = Royalties.objects.all().values('owner_name', 'operator_name', 'check_number').annotate(total=Count('owner_name')).order_by('total') 
len(rt3)
rt3 = Royalties.objects.all().values('owner_name', 'operator_name', 'check_amount').annotate(total=Count('owner_name')).order_by('total') 
rt2
len(rt3)
rt3 = Royalties.objects.all().values('owner_name', 'operator_name', 'price').annotate(total=Count('owner_name')).order_by('total') 
len(rt3)
rt3
rt3 = Royalties.objects.all().values('owner_name', 'operator_name', 'gross_volume').annotate(total=Count('owner_name')).order_by('total') 
len(rt3)
rt3 = Royalties.objects.all().values('owner_name', 'operator_name', 'interest_type').annotate(total=Count('owner_name')).order_by('total') 
len(rt3)
rt3
for x in rt3: 
    print(x)
    
get_ipython().run_line_magic('save', '')
