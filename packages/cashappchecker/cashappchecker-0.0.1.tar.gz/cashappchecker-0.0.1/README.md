# CashappChecker - DOCUMENTATION


## How to use

### GETTING STARTED

Import the module

```
import cashapp_checker as check
```
Get the ID of your cashapp invoice URL

```
check.id("https://cash.app/payments/4xxx8z1q1cisxxxxxxxxxx/receipt?utm_source=activity-item")
```
*example response: 4xxx8z1q1cisxxxxxxxxxx*

Get the amount sent

```
amt = check.amount("YOUR_ID")
```
*example value of variable **amt**: $5.50*

Get the note for the transaction

```
note = check.note("YOUR_ID")
```
*example value of variable **note**: For babysitting ❤*

Get the receiver of the transaction

```
cashtag = check.cashtag("YOUR_ID")
```
*example value of variable **cashtag**: $wahrs (my cashtag, feel free to donate if the module helped you 😊)*

Get the sender of the transaction

```
coming in v2
```

