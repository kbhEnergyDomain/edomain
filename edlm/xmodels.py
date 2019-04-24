# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assetinformation(models.Model):
    asset_id = models.AutoField(db_column='ASSET_ID', primary_key=True)  # Field name made lowercase.
    atype = models.IntegerField(db_column='ATYPE')  # Field name made lowercase.
    asset_no = models.IntegerField(blank=True, null=True)
    beg_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    well_id = models.IntegerField(blank=True, null=True)
    tract_id = models.IntegerField(blank=True, null=True)
    mineral_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assetinformation'


class Assetname(models.Model):
    asset_name_id = models.AutoField(db_column='Asset_name_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    asset_no = models.IntegerField(db_column='ASSET_NO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assetname'


class Assettype(models.Model):
    asset_type_id = models.AutoField(primary_key=True)
    asset_type = models.IntegerField()
    asset_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assettype'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bid(models.Model):
    bid_id = models.AutoField(db_column='BID_ID', primary_key=True)  # Field name made lowercase.
    oid = models.ForeignKey('Ownership', models.DO_NOTHING, db_column='oid')
    sdate = models.DateTimeField()
    sexpire = models.DateTimeField()
    svalue = models.FloatField(blank=True, null=True)
    state = models.IntegerField()
    bidder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bid'


class Customer(models.Model):
    cust_id = models.AutoField(db_column='CUST_ID', primary_key=True)  # Field name made lowercase.
    cust_fname = models.CharField(db_column='CUST_FNAME', max_length=50)  # Field name made lowercase.
    cust_lname = models.CharField(db_column='CUST_LNAME', max_length=50)  # Field name made lowercase.
    cust_no = models.CharField(db_column='CUST_NO', max_length=50)  # Field name made lowercase.
    sign_date = models.DateField(db_column='SIGN_DATE', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='CREDIT', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cust_address1 = models.CharField(db_column='CUST_ADDRESS1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cust_address2 = models.CharField(db_column='CUST_ADDRESS2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cust_city = models.CharField(db_column='CUST_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cust_zipcode = models.CharField(db_column='CUST_ZIPCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_state = models.CharField(db_column='CUST_STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=16, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Dblistings(models.Model):
    sale_id = models.AutoField(db_column='SALE_ID', primary_key=True)  # Field name made lowercase.
    oid = models.ForeignKey('Ownership', models.DO_NOTHING, db_column='oid')
    ondate = models.DateField()
    sexpire = models.DateField()
    askvalue = models.FloatField(blank=True, null=True)
    state = models.IntegerField()
    bidid = models.IntegerField(blank=True, null=True)
    soldvalue = models.FloatField(blank=True, null=True)
    solddate = models.DateField(blank=True, null=True)
    soldto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dblistings'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Leasestable(models.Model):
    id = models.IntegerField(primary_key=True)
    tract_id = models.CharField(db_column='Tract ID', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lease = models.CharField(db_column='Lease', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tract_name = models.CharField(db_column='Tract Name', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    partial = models.CharField(db_column='Partial', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gross_acres = models.IntegerField(db_column='Gross Acres', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_acres = models.IntegerField(db_column='Net Acres', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    legal_description = models.CharField(db_column='Legal Description', max_length=106, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    county = models.CharField(db_column='County', max_length=9, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=9, blank=True, null=True)  # Field name made lowercase.
    township = models.CharField(db_column='Township', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lrange = models.CharField(db_column='LRange', max_length=10, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quarter_call = models.CharField(db_column='Quarter Call', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abstract = models.CharField(db_column='Abstract', max_length=10, blank=True, null=True)  # Field name made lowercase.
    block = models.CharField(db_column='Block', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='Lot', max_length=10, blank=True, null=True)  # Field name made lowercase.
    survey = models.CharField(db_column='Survey', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leasestable'


class Minerallocations(models.Model):
    wid = models.AutoField(primary_key=True)
    mtype = models.IntegerField(blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    x_latt = models.FloatField(blank=True, null=True)
    x_long = models.FloatField(blank=True, null=True)
    x_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minerallocations'


class Ownership(models.Model):
    owner_id = models.AutoField(db_column='OWNER_ID', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    aid = models.ForeignKey(Assetinformation, models.DO_NOTHING, db_column='aid', blank=True, null=True)
    puch_date = models.DateField()
    sold_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ownership'


class Royalties(models.Model):
    rid = models.AutoField(db_column='Rid', primary_key=True)  # Field name made lowercase.
    operator_name = models.CharField(db_column='Operator_Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    owner_name = models.CharField(db_column='Owner_Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    owner_number = models.IntegerField(db_column='Owner_Number', blank=True, null=True)  # Field name made lowercase.
    check_number = models.CharField(db_column='Check_Number', max_length=32, blank=True, null=True)  # Field name made lowercase.
    check_date = models.DateField(db_column='Check_Date', blank=True, null=True)  # Field name made lowercase.
    check_amount = models.FloatField(db_column='Check_Amount', blank=True, null=True)  # Field name made lowercase.
    operator_cc = models.CharField(db_column='Operator_CC', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=128, blank=True, null=True)  # Field name made lowercase.
    product_code = models.CharField(db_column='Product_Code', max_length=32, blank=True, null=True)  # Field name made lowercase.
    interest_type = models.CharField(db_column='Interest_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    owner_percent = models.FloatField(db_column='Owner_Percent', blank=True, null=True)  # Field name made lowercase.
    dist_pct = models.FloatField(db_column='Dist_pct', blank=True, null=True)  # Field name made lowercase.
    prod_date = models.DateField(db_column='Prod_Date', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    btu_factor = models.FloatField(db_column='BTU_Factor', blank=True, null=True)  # Field name made lowercase.
    gross_volume = models.FloatField(db_column='Gross_Volume', blank=True, null=True)  # Field name made lowercase.
    gross_value = models.FloatField(db_column='Gross_Value', blank=True, null=True)  # Field name made lowercase.
    gross_taxes = models.FloatField(db_column='Gross_Taxes', blank=True, null=True)  # Field name made lowercase.
    gross_deducts = models.FloatField(db_column='Gross_Deducts', blank=True, null=True)  # Field name made lowercase.
    net_value = models.FloatField(db_column='Net_Value', blank=True, null=True)  # Field name made lowercase.
    owner_volume = models.FloatField(db_column='Owner_Volume', blank=True, null=True)  # Field name made lowercase.
    owner_value = models.FloatField(db_column='Owner_Value', blank=True, null=True)  # Field name made lowercase.
    owner_taxes = models.FloatField(db_column='Owner_Taxes', blank=True, null=True)  # Field name made lowercase.
    owner_deducts = models.FloatField(db_column='Owner_Deducts', blank=True, null=True)  # Field name made lowercase.
    owner_net_value = models.FloatField(db_column='Owner_Net_Value', blank=True, null=True)  # Field name made lowercase.
    tax_type_1 = models.CharField(db_column='Tax_Type_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    gross_tax_1 = models.FloatField(db_column='Gross_Tax_1', blank=True, null=True)  # Field name made lowercase.
    net_tax_1 = models.FloatField(db_column='Net_Tax_1', blank=True, null=True)  # Field name made lowercase.
    document  = models.FileField(db_column='Document', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(max_length=32, blank=True, null=True) # Field name made lowercase


    class Meta:
        managed = True
        db_table = 'royalties'


class Tractlocations(models.Model):
    tid = models.AutoField(primary_key=True)
    tract_id = models.IntegerField(blank=True, null=True)
    x_latt = models.FloatField(blank=True, null=True)
    x_long = models.FloatField(blank=True, null=True)
    x_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tractlocations'


class Tractnames(models.Model):
    tid = models.AutoField(primary_key=True)
    tract_id = models.IntegerField(blank=True, null=True)
    tract_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tractnames'


class Tractstable(models.Model):
    id = models.IntegerField(primary_key=True)
    tract_id = models.CharField(db_column='Tract ID', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gross_acres = models.DecimalField(db_column='Gross Acres', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_mineral_acres = models.DecimalField(db_column='Net Mineral Acres', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_interest_decimal = models.DecimalField(db_column='Net Interest Decimal', max_digits=6, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_fractional_interest = models.CharField(db_column='Net Fractional Interest', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_royalty_acres = models.DecimalField(db_column='Net Royalty Acres', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    legal_description = models.CharField(db_column='Legal Description', max_length=298, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    county = models.CharField(db_column='County', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=12, blank=True, null=True)  # Field name made lowercase.
    township = models.CharField(db_column='Township', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trange = models.CharField(db_column='tRange', max_length=4, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=3, blank=True, null=True)  # Field name made lowercase.
    quarter_call = models.CharField(db_column='Quarter Call', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    abstract = models.CharField(db_column='Abstract', max_length=10, blank=True, null=True)  # Field name made lowercase.
    block = models.CharField(db_column='Block', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='Lot', max_length=10, blank=True, null=True)  # Field name made lowercase.
    survey = models.CharField(db_column='Survey', max_length=14, blank=True, null=True)  # Field name made lowercase.
    abbreviated_legal_description = models.CharField(db_column='Abbreviated Legal Description', max_length=33, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.CharField(db_column='Comments', max_length=274, blank=True, null=True)  # Field name made lowercase.
    interest_type = models.CharField(db_column='Interest Type', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    all_depths = models.CharField(db_column='All Depths', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    depth_notes = models.CharField(db_column='Depth Notes', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    leased = models.CharField(db_column='Leased', max_length=1, blank=True, null=True)  # Field name made lowercase.
    surface_ownership = models.CharField(db_column='Surface Ownership', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deed_doc_name_1 = models.CharField(db_column='Deed Doc Name #1', max_length=13, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deed_doc_name_2 = models.CharField(db_column='Deed Doc Name #2', max_length=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tractstable'


class Welllocations(models.Model):
    wid = models.AutoField(primary_key=True)
    well_id = models.IntegerField(blank=True, null=True)
    x_latt = models.FloatField(blank=True, null=True)
    x_long = models.FloatField(blank=True, null=True)
    x_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'welllocations'


class Wellnames(models.Model):
    wid = models.AutoField(primary_key=True)
    well_id = models.IntegerField(blank=True, null=True)
    well_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellnames'


class Wells(models.Model):
    wid = models.AutoField(primary_key=True)
    well_api = models.CharField(max_length=16, blank=True, null=True)
    well_type = models.IntegerField(blank=True, null=True)
    well_long = models.FloatField(blank=True, null=True)
    well_latt = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wells'
