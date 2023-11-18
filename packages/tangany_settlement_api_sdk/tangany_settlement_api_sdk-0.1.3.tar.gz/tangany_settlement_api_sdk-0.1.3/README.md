# Tangany Settlement API Python SDK

Unofficial Python SDK for consuming Tangany Settlement API.

## Installation

To install the SDK, you can use pip:

```bash
pip install tangany_settlement_api_sdk
```

## Usage

### Initialization

First, import the SDK:
```python
from tangany_settlement_api_sdk import SettlementClient
from tangany_settlement_api_sdk.auth import Credentials

```

Initialize the SDK by providing API credentials and create a Settlement API client:

```python
credentials = Credentials(client_id="xxx", client_secret="yyy")
api = SettlementClient(credentials=credentials)
```

## Examples

There is a [jupyter notebook file](./examples.ipynb) with all examples, here is an excerpt of some examples to demonstrate how to use the SDK:

### Accounts

#### Create accounts
```python
api.accounts.create(id="00000001", label="Satoshi Nakamoto's account", type="internal")
```


#### Update account label 
```python
api.accounts.update(id="00000001", op="replace", path="/label", value="Satoshi Nakamoto's HODL account")                                   
```

#### List all account ids 
```python
account_ids = []
next_page_token = ""

while next_page_token != None:
    results = api.accounts.list(next_page_token) 
    next_page_token = results['nextPageToken'] 
    for result in results['items']:
        account_ids.append(result['id'])
```

#### Delete accounts
```python
api.accounts.delete(id="00000001")
```

### Assets

#### Get all asset ids 
```python
api = SettlementClient(credentials=credentials)
asset_ids = []
for asset in api.assets.list()['items']:
    asset_ids.append(asset['id'])
```

#### Get a specific asset 
```python
result = api.assets.get(id="BTC")
```

### Ledgers 

#### Create ledger 
```python
api.ledgers.create("Test", "My test ledger")
```

#### List ledgers 
```python
result = api.ledgers.list()
```

#### Get a specific ledger 
```python
result = api.ledgers.get(id="Test")
```

### Transactions 

#### Create a virtual transaction 
```python
api.transactions.create(
    ledger_id="Test",
    transaction_id="TX_SAMPLE",
    from_account_id="00000001",
    to_account_id="00000002",
    value_date="2023-11-11T15:00:00.000Z",
    asset_id="BTC",
    value="1.0",
    fiat_currency="EUR",
    fiat_value="30000.00",
    reference="BTC-REF",
    trade_info_fill_date="2023-11-10T15:00:00.000Z",
    trade_info_market_maker_tx_id="123456789"    
)
```

#### Get a single transaction 
```python
result = api.transactions.get(ledger_id="Test", transaction_id="TX_SAMPLE")
```

#### Get all transactions for a specific account id 
```python
transactions = []
next_page_token = ""

while next_page_token != None:
    results = api.transactions.list(ledger_id="Test", involving_account_id="00000001", next_page_token=next_page_token)
    next_page_token = results['nextPageToken'] 
    for result in results['items']:
        transactions.append(result)
```

#### Get all transactions after a specific booking date 
```python
transactions = []
next_page_token = ""

while next_page_token != None:
    results = api.transactions.list(ledger_id="Test", booking_date_after="2023-11-11", next_page_token=next_page_token)
    next_page_token = results['nextPageToken'] 
    for result in results['items']:
        transactions.append(result)
```

#### Delete a single transaction (mark as cancelled) 
```python
api.transactions.delete(ledger_id="Test", transaction_id="TX_SAMPLE")

```
### Fundings
#### Sync on-chain deposit as virtual transaction (create deposit) 
```python
api.funding_deposits.create(
    ledger_id="Test",
    transaction_id=f"TX_GENESIS",
    to_account_id="00000001",
    value_date="2023-11-11T15:00:00.000Z",
    asset_id="BTC",
    value="1.0",
    fiat_currency="EUR",
    fiat_value="30000.00",
    reference="BTC-REF",
    txHash="0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
)
```

#### List fundings 
```python
transactions = []
next_page_token = ""

while next_page_token != None:
    results = api.fundings.list(ledger_id="Test", next_page_token=next_page_token)
    next_page_token = results['nextPageToken'] 
    for result in results['items']:
        transactions.append(result)
```

### Balances

#### List all account balances 
```python
account_balances = []
next_page_token = ""

while next_page_token != None:
    results = api.account_balances.list(ledger_id="Test", valuta_date="2023-11-12", next_page_token=next_page_token)
    next_page_token = results['nextPageToken'] 
    for result in results['items']:
        account_balances.append(result)
```

#### Get single account balance 
```python
result = api.account_balances.get(ledger_id="Test", account_id="00000001")
```

#### Get ledger balance of all assets 
```python
result = api.asset_balances.get(ledger_id="Test")
```

### Reports

#### Create immediate report 
```python
api.reports.create(id="report1", type="account_balances_v1", format="csv", ledger_id="Test", date="2023-11-13")
```

#### List all reports 
```python
result = api.reports.list()
```

#### Get a single report 
```python
result = api.reports.get(id="report1")
```

#### List report results 
```python
result = api.report_results.list("report1")
```


#### Download a report 
```python
result = api.report_results.get(report_id="report1", result_id="2023-11-17T12:07:00Z")
```


#### Delete report 
```python
result = api.reports.delete(id="report1")
```

## Changelog
All notable changes to this project are documented in the [changelog](./CHANGELOG.MD)

## Testing
For testing provide your credentials to [examples.ipynb](./examples.ipynb) and run the notebook.

## Deployment
To release a new version of this SDK please update the version contained in the [pyproject.toml](./pyproject.toml) file.
After testing just use _poetry_ to build and publish a new version to [pypi.org](https://pypi.org/project/tangany_settlement_api_sdk/):

```
poetry build
poetry publish
```

## API documentation
Full API documentation is available at https://docs.tangany.com

<img src="https://cwstorecdn0.blob.core.windows.net/web/stoplight/TanganySettlementAPI.png"  width="50%" alt="Tangany"  align="middle" />
<br><br>

***

<br><br>
<div align="center"><img src="https://cwstorecdn0.blob.core.windows.net/web/tangany_logo_wordmark_on_dark.png"  width="50%" alt="Tangany"  align="middle" />
<p>

</p>
<p>
© 2023 <a href="https://tangany.com">Tangany GmbH</a>
</p>
<p>
 <a href="https://tangany.com/imprint/">Imprint</a>
• <a href="https://tangany.com/legal-privacy/">Legal & privacy</a>
• <a href="https://tangany.com#newsletter">Newsletter</a>
• <a href="https://twitter.com/tangany">Twitter</a>
• <a href="https://www.facebook.com/tanganywallet">Facebook</a>
• <a href="https://www.linkedin.com/company/tangany/">LinkedIn</a>
• <a href="https://www.youtube.com/channel/UCmDr1clodG1ov-iX_GMkwMA">YouTube</a>
• <a href="https://github.com/Tangany/">Github</a>
</p>
</div>