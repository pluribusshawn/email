# Depends on ExchangePowerShell Module

# param(
# [Paramater(Mandatory=$true)]
# [string] $username
# [Paramater(Mandatory=$true)]
# [string] $domain
# )

Connect-ExchangeOnline -UserPricipalName $username

New-DkimSigningConfig -DomainName $domain -Enabled $false
