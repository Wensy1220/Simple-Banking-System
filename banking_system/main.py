from banking_system.bank import Bank

def main():
    bank = Bank()
    
    # Load existing accounts
    bank.load_from_csv("accounts.csv")
    
    # Create new accounts
    account1 = bank.create_account("1001", "Wensy", 500.0)
    account2 = bank.create_account("1002", "Haitao", 300.0)
    
    # Transactions
    bank.deposit("1001", 200.0)
    bank.withdraw("1002", 100.0)
    bank.transfer("1001", "1002", 150.0)
    
    # Display all accounts
    print("\nAll accounts:")
    for account in bank.get_all_accounts():
        print(f"  {account.account_id}: {account.name} - ${account.balance:.2f}")
    
    # Save to CSV
    bank.save_to_csv("accounts.csv")

if __name__ == "__main__":
    main()