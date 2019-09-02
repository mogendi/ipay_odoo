## IPAY ODOO MODULE

### Requirements:
It's important to note that this module has only been tested on odoo 12

1. Python and Pip pre installed
2. An installaion of odoo 12 server. You can find out how to intsall odoo [here](https://www.odoo.com/documentation/11.0/setup/install.html) for your OS or find an installation script (Linux users)

### Installing:
1. Extract the zipped file into the odd addons folder (usually odoo12/odoo/addons)
    NOTE: Ensure the addons folder is listed in the odoo configuration file (usually at etc/odoo.conf) as an addons path
2. Restart the odoo intsance by runing ''' sudo systemctl restart odoo ''' or ''' sudo systemctl        restart odoo12 ''' depending on how the service instance is listed on your machine 
3. Open ''' localhost:8069 ''' on your browser and navigate to odoo settings and activate developer     mode
4. Go to the apps menu and select "update app list"
5. On the same menu search for the module "ipay" (ensure the app selection has been removed) and        install it

### Configuration
1. Navigate to Invoicing->Configuration->Payment Acquirers
2. Look for ipays payment acquirer, click on activate, you'll be redirected to the payment acquirers
   configuration page
3. There edit the Vendor ID and Key fields to those assigned to you by ipay and check the live          checkbox

### Testing:
The easiest way to test is using the website module, therefore youll need to install it by  simply searching for it in the apps menu

Buy a product in the shop, in the checkout menu choose ipay as your payment gateway and click pay now, you''ll be redirected to ipays payment gateway

