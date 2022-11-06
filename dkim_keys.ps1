# Depends on ExchangePowerShell Module

[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [string] $username
  [Parameter(Mandatory=$true)]
  [string] $domain
)

Connect-ExchangeOnline -UserPricipalName $username

New-DkimSigningConfig -DomainName $domain -Enabled $false
