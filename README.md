## IPAY ODOO MODULE

### Requirements:
It's important to note that this module has only been tested on odoo 14

1. Python and Pip pre installed.
2. An installation/ working instance of postgres.
3. An installaion of odoo 14 server. You can find out how to intsall odoo [here](https://www.odoo.com/documentation/11.0/setup/install.html) for your OS or find an installation script (Linux-Debian users).

### Installing:
1. Extract the zipped file into the odd addons folder (usually odoo12/odoo/addons)
    NOTE: Ensure the addons folder is listed in the odoo configuration file (usually at etc/odoo.conf) as an addons path
2. Restart the odoo intsance by runing ``` sudo systemctl restart odoo ``` or ``` sudo systemctl restart odoo12 ``` depending on how the service instance is listed on your machine on linux-Debian. On windows, open ```Services``` and search for odoo and restart the server. 
3. Open ``` localhost:8069 ``` (or check odoo logs to see what port the server started on) on your browser.
4. Go to the apps menu and select "update app list".
5. On the same menu search for the module "ipay" and install it.

### Configuration
1. Navigate to Invoicing->Configuration->Payment Acquirers.
2. Look for ipays payment acquirer, click on activate, you'll be redirected to the payment acquirers
   configuration page.
3. There edit the Vendor ID and Key fields to those assigned to you by ipay and either check or uncheck the live, autopay and payment chanel checkboxes.

### Testing:
The easiest way to test is using the website module, therefore youll need to install it by  simply searching for it in the apps menu and activating the store (you'll need to be in developer mode to activate this)

Buy a product in the shop, in the checkout menu choose ipay as your payment gateway and click pay now, you''ll be redirected to ipays payment gateway


### Other Sources:
Check odoos docummentation on [activating developer mode](https://www.odoo.com/documentation/user/14.0/general/developer_mode/activate.html) and [installation of apps](https://www.odoo.com/forum/help-1/how-to-install-a-new-module-app-in-odoo-12-community-on-windows-10-150960) for reference. 

