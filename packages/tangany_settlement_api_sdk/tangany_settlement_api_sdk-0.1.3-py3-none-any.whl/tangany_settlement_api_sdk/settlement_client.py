from attr import define
from .auth import Authenticator, Credentials
from .endpoints import AccountBalances, Accounts, AssetBalances, Assets, FundingDeposits, FundingWithdrawals, Fundings, Ledgers, ReportResults, Reports, Transactions

@define
class SettlementClient:
    _authenticator: Authenticator
    account_balances: AccountBalances
    accounts: Accounts
    asset_balances: AssetBalances
    assets: Assets
    funding_deposits: FundingDeposits
    funding_withdrawals: FundingWithdrawals
    fundings: Fundings
    ledgers: Ledgers
    report_results: ReportResults
    reports: Reports
    transactions: Transactions
    
    def __init__(self, credentials: Credentials):
        self._authenticator = Authenticator(credentials=credentials) 
        self.account_balances = AccountBalances(authenticator=self._authenticator)  
        self.accounts = Accounts(authenticator=self._authenticator)   
        self.asset_balances = AssetBalances(authenticator=self._authenticator)    
        self.assets = Assets(authenticator=self._authenticator)    
        self.funding_deposits = FundingDeposits(authenticator=self._authenticator)    
        self.funding_withdrawals = FundingWithdrawals(authenticator=self._authenticator)    
        self.fundings = Fundings(authenticator=self._authenticator)    
        self.ledgers = Ledgers(authenticator=self._authenticator)    
        self.report_results = ReportResults(authenticator=self._authenticator)   
        self.reports = Reports(authenticator=self._authenticator) 
        self.transactions = Transactions(authenticator=self._authenticator)  