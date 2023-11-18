# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


# NMI Gateway 

## Examples 


### Customer Vault methods

#### Create customer vault
```python
from nmigate.lib.customer_vault import CustomerVault

secret_key = 'your secret key'
org = 'your org'

customer_vault = CustomerVault(secret_key, org)
        result = customer_vault.create_customer_vault({
            "id": "51asdfsf234asdfasfasfsa", 
            "token": "00000000-000000-000000-000000000000", 
            "billing_id": "51asdfsf234asdfasfasfsa", 
            "billing_info": {
                "first_name": "1", 
                "last_name": "1", 
                "address1": "1", 
                "city": "1", 
                "state": "1", 
                "zip": "1", 
                "country": "1", 
                "phone": "1", 
                "email": "1"
            }
        })
```

#### Create customer vault