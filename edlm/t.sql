
create table royalties (
Rid				int not null auto_increment,
Operator_Name	varchar(64), 
Owner_Name	    varchar(64),
Owner_Number	int,
Check_Number	varchar(32), 
Check_Date	    date, 
Check_Amount	float, 
Operator_CC	    varchar(32),
Description	    varchar(128),
Product_Code    varchar(32), 
Interest_Type	varchar(32),
Owner_Percent	float, 
Dist_pct		float, 
Prod_Date		date, 
Price			float, 
BTU_Factor		float, 
Gross_Volume	float, 
Gross_Value		float,
Gross_Taxes		float,
Gross_Deducts	float, 
Net_Value		float,
Owner_Volume	float, 
Owner_Value		float, 
Owner_Taxes	    float, 
Owner_Deducts	float,
Owner_Net_Value	float, 
Tax_Type_1	varchar(16), 
Gross_Tax_1	float, 
Net_Tax_1	float, 
PRIMARY KEY(RID)
);

/* 
myColumns = (

'Operator_Name' , 'Owner_Name', 'Owner_Number', 'Check_Number', 
'Check_Date' ,'Check_Amount','Operator_CC', 'Description', 
'Product_Code', 'Interest_Type', 'Owner_Percent','Dist_pct', 
'Prod_Date', 'Price', 'BTU_Factor',  'Gross_Volume', 'Gross_Value', 
'Gross_Taxes',  'Gross_Deducts', 'Net_Value', 'Owner_Volume', 'Owner_Value',
'Owner_Taxes', 
'Owner_Deducts', 'Owner_Net_Value',
 'Tax_Type_1',
 'Gross_Tax_1', 'Net_Tax_1')

*/