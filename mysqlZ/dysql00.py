from mysqlZ.quanhtest import qhmysql

sq2="SELECT account_id,user_name,mobile_no,open_id,wechat_app_id FROM sys_account WHERE mobile_no =13066875865;"
sq3="SELECT * FROM sys_account"

qhmysql(sq2,sq3)

