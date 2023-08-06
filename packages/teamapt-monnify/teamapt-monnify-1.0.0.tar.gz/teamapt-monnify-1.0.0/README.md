                                  MONNIFY PYTHON LIBRARY USER GUIDE
                                            Version 1.0.0

Monnify is one of the products of TeamApt <https://www.teamapt.com/> . Monnify empowers businesses in the formal & informal sectors with the right tools & solutions to manage their finances and grow their businesses. Businesses in the formal economy benefit from our payment infrastructure that simplifies how they accept, manage and make payments. While smaller-scale businesses and entrepreneurs benefit from our market-community focused products that give them accessible, affordable and convenient short term working capital.

                                  MONNIFY PYTHON LIBRARY USER GUIDE

Before you can start integrating to Monnify, you will need to sign up on Monnify. Click <https://app.monnify.com/create-account> to sign up. After successful registration, login and for your credentials. 

                                            CREDENTIAL NEEDED

1. API KEY
2. SECRET KEY
3. CONTRACT
4. WALLET ID

All this can be seen on the setting area when you login to you logged in.


                                            API ENDPOINT IN THE LIBRARY
                                            
1. monnifyCredential
2. get_token
3. verify_account
4. reserve_account
5. add_link_account
6. update_bvn_reserve
7. deallocate_account
8. reserve_account_transactions
9. tranfer
10. authorize_tranfer
11. resend_otp
12. get_transfer_details
13. get_all_single_transfer
14. get_wallet_balance
15. create_invoice
17. initiate_refund
18. get_refund_status
19. get_all_refund
20. create_sub_account
21. get_sub_account
22. update_sub_account
23. delete_sub_account
24. one_time_payment

                                            HOW TO USE THE LIBRARY
To use the library, we have to use package installer (pip) by running: pip install teamapt-monnify

After successfull installation, we can now use the package in our development by importing it in our script


            from monnify.monnify import monnifyCredential, get_token, Monnify

            monnify = Monnify()

            api_key = "MK_TEST_8UBXGKTYYYWB"
            secret_key = "ENRC4FDYYYETKA53YPXBFLUFXWYHG2"
            contractCode = '2917634883'
            walletId = '654CAB211YY36760A659C787B2AA38E8'

            merchant_credential = monnifyCredential(
              api_key, 
              secret_key, 
              contractCode, 
              walletId, 
              is_live=False
              )

            token = get_token(merchant_credential)

NOTE: If you are in sandbox please is_live = False and can only be set to True when you are in production and make sure you change credentials to live credentials



1.VERIFY BANK ACCOUNT - This allows you check if an account number is a valid NUBAN, get the account name if valid.

            bank = monnify.verify_account(
              merchant_credential, 
              accountNumber='2213324087', 
              bankCode='057'
              )
            print(bank)

            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'accountNumber': '2213324087', 
                'accountName': 'SAMSON   ILEMOBAYO', 
                'bankCode': '057'
              }
            }
          
2 INVOICE - Monnify invoicing allows you generate invoices via APIs. For each invoice, a virtual account number will be generated and tied to that invoice so your customers can simply transfer to that account number to pay

            create_invoice = monnify.create_invoice(
              merchant_credential, 
              amount='1000', 
              invoiceReference='uueyyws', 
              description='test invoice', 
              customerEmail='test@gmail.com', 
              customerName='Samson', 
              expiryDate='2021-04-30 12:00:00', 
              paymentMethods=['CARD', 'ACCOUNT_TRANSFER'], 
              redirectUrl='http://abc.com'
              )
            print(create_invoice)

            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'amount': 1000, 
                'invoiceReference': 'uueyyws', 
                'invoiceStatus': 'PENDING', 
                'description': 'test invoice', 
                'contractCode': '2917634883', 
                'customerEmail': 'test@gmail.com', 
                'customerName': 'Samson', 
                'expiryDate': '2021-04-30 12:00:00', 
                'createdBy': 'MK_TEST_8UBXGKTFSB', 
                'createdOn': '2021-04-14 15:18:31', 
                'checkoutUrl': 'https://sandbox.sdk.monnify.com/checkout/MNFY|63|20210414151813|000197', 
                'accountNumber': '3000041788', 
                'accountName': 'tes', 
                'bankName': 'Wema bank', 
                'bankCode': '035', 
                'redirectUrl': 'http://abc.com'
              }
            }

3 RESERVE ACCOUNT - Reserved account APIs enable merchants create accounts that can be dedicated to each of their customers. Once any payment is done to that account, we notify your webhook with the payment information


            reserve_account = monnify.reserve_account(
              token, 
              merchant_credential, 
              accountReference='tw663552ppw', 
              accountName='Test Account', 
              customerEmail='test2@gmail.com', 
              customerName="Test Account", 
              customerBvn='66377273233', 
              availableBank=True
              )
            print(reserve_account)

            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'contractCode': '2917634883', 
                'accountReference': 'tw663552ppw', 
                'accountName': 'Tes', 
                'currencyCode': 'NGN', 
                'customerEmail': 
                'test2@gmail.com', 
                'customerName': 'Test Account', 
                'accountNumber': '3000041799', 
                'bankName': 'Wema bank', 
                'bankCode': '035', 
                'collectionChannel': 'RESERVED_ACCOUNT', 
                'reservationReference': 'CHVQBNP3DRTGU6CZFXQW', 
                'reservedAccountType': 'GENERAL', 
                'status': 'ACTIVE', 
                'createdOn': '2021-04-14 15:29:51.976', 
                'incomeSplitConfig': [], 
                'bvn': '66377273233', 
                'restrictPaymentSource': False
              }
            }

NOTE: When the availableBank is set to True,random account number amount there partner bank will be reserved. if you want to reserved you choice of bank e.g WEMA, you have to set the availableBank to the code of the bank you wish to reserve i.e availableBank='035'. available partner bank codes are (Rolez MFB = 50515, Wema Bank = 035, Sterling Bank = 232)

          
4 ADD LINK ACCOUNT - This API allows you to add accounts with another partner bank and link to an existing customer with the customer's account reference.


            link_account = monnify.add_link_account(
              token, 
              merchant_credential, 
              accountReference='tw663552', 
              getAllAvailableBanks=True, 
              preferredBanks=['035']
              )
            print(link_account)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                  "contractCode": "915483727511",
                  "accountReference": "121615386005862",
                  "accountName": "reservedAccountName",
                  "currencyCode": "NGN",
                  "customerEmail": "nnaemekapaschal@gmail.com",
                  "customerName": "Pascool",
                  "accounts": [
                      {
                        "bankCode": "035",
                        "bankName": "WEMA Bank",
                        "accountNumber": "XXXX123456"
                      },
                      {
                        "bankCode": "50515",
                        "bankName": "ROLEZ MFB",
                        "accountNumber": "XXXX123456"
                      },
                      {
                        "bankCode": "123",
                        "bankName": "Bank 3",
                        "accountNumber": "XXXX123456"
                      }
                  ],
                  "collectionChannel": "RESERVED_ACCOUNT",
                  "reservationReference": "8MHKXZS8GCEPVXB59ML6",
                  "reservedAccountType": "GENERAL",
                  "status": "ACTIVE",
                  "createdOn": "2021-03-10 15:20:07.0",
                  "restrictPaymentSource": false
              }
            }

NOTE: If getAllAvailableBanks is set to true, then an account with all available banks not yet linked will be added. Set getAllAvailableBanks to false if you want to specify preferred banks to reserve accounts with. set to true if you want to add all other available partner bank accounts to your reserved account.

5 UPDATE BVN FOR RESERVE ACCOUNT - This Function is to be used to update a customer's BVN mapped to a Reserved Account.

            update_bvn = monnify.update_bvn_reserve(
              token, 
              merchant_credential, 
              bvn='66377283884', 
              accountReference='635525663623'
              )
            print(update_bvn)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                "contractCode": "2917634883",
                "accountReference": "635525663623",
                "currencyCode": "NGN",
                "customerEmail": "testuser@test.com",
                "customerName": "Test Oj",
                "accountNumber": "4290733572",
                "bankName": "Wema Bank",
                "bankCode": "035",
                "collectionChannel": "RESERVED_ACCOUNT",
                "reservationReference": "R8J4LCW3P82WN4X6LQCW",
                "reservedAccountType": "GENERAL",
                "status": "ACTIVE",
                "createdOn": "2021-02-01 21:40:55.0",
                "bvn": "66377283884",
                "restrictPaymentSource": false
              }
           }
          
6 DEALLOCATE RESERVE ACCOUNT: This is used to deallocate/delete reserved account.

            delete_account = monnify.deallocate_account(
              token, 
              merchant_credential, 
              accountNumber='3000041799'
              )
            print(delete_account)


            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                  "contractCode": "797854529434",
                  "accountReference": "reference12345#",
                  "accountName": "Test Reserved Account",
                  "currencyCode": "NGN",
                  "customerEmail": "test@tester.com",
                  "accountNumber": "3000041799",
                  "bankName": "Wema bank",
                  "bankCode": "035",
                  "reservationReference": "NRF72EMEBCGNN6WUKD35",
                  "status": "ACTIVE",
                  "createdOn": "2021-04-14 17:05:50.0"
                }
            }

NOTE: Any Account deallocated/delete can not be reversed.
          
7 TRANSFER: This is use to initiate transfer to bank

            transfer = monnify.tranfer(
              merchant_credential, 
              amount='1000', 
              reference='66635525', 
              narration='Test Transfer', 
              bankCode='044', 
              accountNumber='0020657659'
              )
            print(transfer)


            {
              "amount": 1000,
              "reference":"66635525",
              "narration":"Test Transfer",
              "destinationBankCode": "044",
              "destinationAccountNumber": "0020657659",
              "currency": "NGN",
              "sourceAccountNumber": "9624937372"
            }

8. AUTHORIZE TRANSFER: To authorize a transfer, you will need to call the following function. If the merchant does not have Two Factor Authentication (2FA) enabled, the transaction will be processed instantly and the response will be as follows:

            authorize = monnify.authorize_tranfer(
              merchant_credential, 
              reference='66635525', 
              authorizationCode='725006'
              )
            print(authorize)


            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                  "amount": 10,
                  "reference": "66635525",
                  "status": "SUCCESS",
                  "dateCreated": "15/04/2021 09:34:32 PM"
                }
            }

9. RESEND OTP: This is function to resend OTP if 2FA is enable for transfer

            resendOtp = monnify.resend_otp(
              merchant_credential, 
              reference='66635525'
              )
            print(resendOtp)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                "message": "Authorization code will be processed and sent to predefined email addresses(s)"
              }
            }

10. GET TRANSFER DETAILS: To get the details of a single transfer,  you will need to call the endpoint below:

            get_transfer = monnify.get_transfer_details(
              merchant_credential, 
              reference='66635525'
              )
            print(get_transfer)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0",
              "responseBody": {
                "amount": 1000.00,
                "reference": "66635525",
                "narration": "Test Payment",
                "currency": "NGN",
                "fee": 20.00,
                "twoFaEnabled": false,
                "status": "SUCCESS",
                "transactionDescription": "Approved or completed successfully",
                "transactionReference": "MFDS2020080523"
                "destinationBankCode": "058",
                "destinationAccountNumber": "0111946768",
                "destinationAccountName": "MEKILIUWA, SMART CHINONSO",
                "destinationBankName": "GTBank",
                "createdOn": "15/04/2021 09:34:32 PM"
              }
            }

11. GET ALL SINGLE TRANSFER

            get_all_single = monnify.get_all_single_transfer(
              merchant_credential, 
              pageSize=5, 
              pageNo=1
              )
            print(get_all_single)


            {
              'requestSuccessful': True, 
              'responseMessage': 'success', 
              'responseCode': '0', 
              'responseBody': {
                'content': [
                  {
                    'amount': 40.0, 
                    'reference': 'TX634636', 
                    'narration': 'USSD', 
                    'bankCode': '044', 
                    'accountNumber': '0020903879', 
                    'currency': 'NGN', 
                    'accountName': 'TEST ACCOUNT', 
                    'bankName': 'Access bank', 
                    'fee': 35.0, 
                    'twoFaEnabled': False, 
                    'status': 'SUCCESS', 
                    'walletId': '654CAB266255344760A659C787B2AA38E8', 
                    'transactionDescription': 'Success', 
                    'transactionReference': 'MFDS|20210310150110|000037', 
                    'createdOn': '2021-03-10T14:01:10.000+0000'
                  }, 
                  {
                    'amount': 1000.0, 
                    'reference': 'TX673137', 
                    'narration': 'USSD', 
                    'bankCode': '044', 
                    'accountNumber': '0020903879', 
                    'currency': 'NGN', 
                    'accountName': 'TEST ACCOUNT', 
                    'bankName': 'Access bank', 
                    'fee': 35.0, 
                    'twoFaEnabled': False, 
                    'status': 'SUCCESS', 
                    'walletId': '654CAB266255344760A659C787B2AA38E8', 
                    'transactionDescription': 'Success', 
                    'transactionReference': 'MFDS|20210225043544|000069', 
                    'createdOn': '2021-02-25T03:35:45.000+0000'
                    }, 
                    
                      
                ], 
                'pageable': {
                          'sort': {
                            'sorted': True, 
                            'unsorted': False, 
                            'empty': False}, 
                            'pageSize': 5, 
                            'pageNumber': 1, 
                            'offset': 5, 
                            'paged': True, 
                            'unpaged': False
                          }, 
                          'totalElements': 113, 
                          'totalPages': 23, 
                          'last': False, 
                          'sort': {
                            'sorted': True, 
                            'unsorted': False, 
                            'empty': False
                          }, 
                          'first': False, 
                          'numberOfElements': 5, 
                          'size': 5, 
                          'number': 1, 
                          'empty': False
                      }
            }

12. GET WALLET BALANCE: This allows you to get the available balance in your monnify wallet.

              walletBal = monnify.get_wallet_balance(merchant_credential)
              print(walletBal)

              {
                "requestSuccessful": true,
                "responseMessage": "success",
                "responseCode": "0",
                "responseBody": {
                  "availableBalance": 378.93,
                  "ledgerBalance": 378.93
                }
              }

13. INITIATE REFUND: This function enables you process refund to a customer for a transaction.

                refund_money = monnify.initiate_refund(
                  token, 
                  merchant_credential, 
                  refundReference='6637whhhwe', 
                  transactionReference='MNFY|63|20210413134205|000113', 
                  refundAmount='1000.0', 
                  refundReason='Order cancelled!', 
                  customerNote='Canceled'
                  )

                print(refund_money)


                {
                  "requestSuccessful": true,
                  "responseMessage": "success",
                  "responseCode": "0",
                  "responseBody": {
                    "transactionReference": "MNFY|63|20210413134205|000113",
                    "paymentReference":"J_12312_122",
                    "transactionAmount": 5000,
                    "refundAmount": 1200,
                    "refundStatus": "IN_PROGRESS",
                    "refundReason": "Order was cancelled",
                    "customerNote": "Refund for order J1110",
                    "refundType": "FULL_REFUND",
                    "createdOn": "15/12/2020 09:38:13 AM",
                    "completedOn": "15/12/2020 12:20:23 PM",
                    "comment": "Refund processed successfully."
                  }
                }

14. GET REFUND STATUS: This function can be used to get status of an initiated refund.

                get_refund_status = monnify.get_refund_status(
                  token, 
                  merchant_credential, 
                  transactionReference='MNFY|63|20210413134205|000113'
                  )
                print(get_refund_status)


                {
                  "requestSuccessful": true,
                  "responseMessage": "success",
                  "responseCode": "0",
                  "responseBody": {
                    "transactionReference": "MNFY|63|20210413134205|000113",
                    "paymentReference":"J_12312_122",
                    "transactionAmount": 5000,
                    "refundAmount": 1200,
                    "refundStatus": "IN_PROGRESS",
                    "refundReason": "Order was cancelled",
                    "customerNote": "Refund for order J1110",
                    "refundType": "FULL_REFUND",
                    "createdOn": "15/12/2020 09:38:13 AM",
                    "completedOn": "15/12/2020 12:20:23 PM",
                    "comment": "Refund processed successfully."
                  }
                }


15. GET ALL REFUNDS: This function enables you process refund to a customer for a transaction.

              get_refund_status = monnify.get_refund_status(
                token, 
                merchant_credential, 
                transactionReference='MNFY|63|20210413134205|000113'
                )
              print(get_refund_status)


              {
                "requestSuccessful":true,
                "responseMessage":"success",
                "responseCode":"0",
                "responseBody":{
                    "content":[
                      {
                          "transactionReference":"MNFY|0111231|123412342",
                          "paymentReference":"J_12312_122",
                          "transactionAmount":5000,
                          "refundAmount":1200,
                          "refundStatus":"IN_PROGRESS",
                          "refundReason":"Order was cancelled",
                          "customerNote":"Refund for order J1110",
                          "refundType":"FULL_REFUND",
                          "createdOn":"15/12/2020 09:38:13 AM",
                          "completedOn":"15/12/2020 12:20:23 PM",
                          "comment":"Refund processed successfully."
                      },
                      {
                          "transactionReference":"MNFY|0111231|123412342",
                          "paymentReference":"J_12312_122",
                          "transactionAmount":5000,
                          "refundAmount":1200,
                          "refundStatus":"IN_PROGRESS",
                          "refundReason":"Order was cancelled",
                          "customerNote":"Refund for order J1110",
                          "refundType":"FULL_REFUND",
                          "createdOn":"15/12/2020 09:38:13 AM",
                          "completedOn":"15/12/2020 12:20:23 PM",
                          "comment":"Refund processed successfully."
                      }
                    ],
                    "last":false,
                    "totalElements":258,
                    "totalPages":129,
                    "first":true,
                    "numberOfElements":2,
                    "size":2,
                    "number":0,
                    "empty":false
                }
              }
  

16. CREATE SUB-ACCOUNT: Creates a sub account for a merchant. Allowing the merchant split transaction settlement between the main account and one or more sub account(s)

              create_sub_account = monnify.create_sub_account(
                merchant_credential, 
                bankCode='044', 
                accountNumber='0020677362', 
                email='test@gmail.com', 
                splitPercentage='20'
                )
              print(create_sub_account)


              {
                "requestSuccessful": true,
                "responseMessage": "success",
                "responseCode": "0",
                "responseBody": [
                    {
                        "subAccountCode": "MFY_SUB_319452883328",
                        "accountNumber": "0123456789",
                        "accountName": "JOHN, DOE SNOW",
                        "currencyCode": "NGN",
                        "email": "tamira1@gmail.com",
                        "bankCode": "058",
                        "bankName": "GTBank",
                        "defaultSplitPercentage": 20
                    }
                  ]
              }

17. DELETE SUB-ACCOUNT: Deletes a merchant's sub account.

            delete_sub_account = monnify.delete_sub_account(
              merchant_credential, 
              subAccountCode='MFY_SUB_248731941563'
              )
            print(delete_sub_account)

            {
              "requestSuccessful": true,
              "responseMessage": "success",
              "responseCode": "0"
            }

18. GET ALL SUB-ACCOUNTS: Returns a list of sub accounts previously created by the merchant.

            get_sub_account = monnify.get_sub_account(merchant_credential)
            print(get_sub_account)


            {
                "requestSuccessful": true,
                "responseMessage": "success",
                "responseCode": "0",
                "responseBody": [
                    {
                        "subAccountCode": "MFY_SUB_319452883219",
                        "accountNumber": "0123456789",
                        "accountName": "JOHN, DOE SNOW",
                        "currencyCode": "NGN",
                        "email": "tamira1@gmail.com",
                        "bankCode": "058",
                        "bankName": "GTBank",
                        "defaultSplitPercentage": 20.00
                    },
                    {
                        "subAccountCode": "MFY_SUB_8838656722391",
                        "accountNumber": "9876543210",
                        "accountName": "JANE, DOE SNOW",
                        "currencyCode": "NGN",
                        "email": "tamira2@gmail.com",
                        "bankCode": "057",
                        "bankName": "Zenith bank",
                        "defaultSplitPercentage": 20.00=
                    }
                ]
            }

19. UPDATE SUB-ACCOUNT: Updates the information on an existing sub account for a merchant.

             update_sub_account = monnify.update_sub_account(
               merchant_credential, 
               subAccountCode='MFY_SUB_248731941563', 
               bankCode='057', accountNumber='2211333471', 
               email='TEST@gmail.com', 
               splitPercentage='23'
               )
            print(update_sub_account)


            {
                "requestSuccessful": true,
                "responseMessage": "success",
                "responseCode": "0",
                "responseBody": [
                    {
                        "subAccountCode": "MFY_SUB_319452883328",
                        "accountNumber": "0123456789",
                        "accountName": "JOHN, DOE SNOW",
                        "currencyCode": "NGN",
                        "email": "tamira1@gmail.com",
                        "bankCode": "058",
                        "bankName": "GTBank",
                        "defaultSplitPercentage": 20
                    }
                ]
            }


20. ONE TIME PAYMENT: Allows you initialize a transaction on Monnify and returns a checkout URL which you can load within a browser to display the payment form to your customer.

              one_time_payment = monnify.one_time_payment(
                merchant_credential, 
                amount='1000', 
                customerName='Test Payment', 
                customerEmail='test@gmail.com', 
                paymentReference='77uuuwyyq', 
                paymentDescription='Test Payment', 
                redirectUrl='http://test.com', 
                paymentMethods=['ACCOUNT_TRANSFER', 'CARD']
                )
              print(one_time_payment)


              {
                "amount": 1000.00,
                "customerName": "Test Payment",
                "customerEmail": "test@gmail.com",
                "paymentReference": "77uuuwyyq",
                "paymentDescription": "Test Payment",
                "currencyCode": "NGN",
                "contractCode":"32904827738",
                "redirectUrl": "http://test.com",
                "paymentMethods":["CARD","ACCOUNT_TRANSFER"]
              }


21. GET RESERVE ACCOUNT TRANSACTIONS: You can get a paginated list of transactions processed to a reserved account by calling the endpoint below and by specifying the accountReference as a query parameter. You can also specify the page number and size (number of transactions) you want returned per page.


                alltrans = monnify.reserve_account_transactions(
                  token, 
                  merchant_credential, 
                  accountReference='7737762h', 
                  page=0, size=10)
                print(alltrans)

                {
                  "requestSuccessful": true,
                  "responseMessage": "success",
                  "responseCode": "0",
                  "responseBody": {
                      "content": [
                          {
                              "customerDTO": {
                                  "email": "test@tester.com",
                                  "name": "Test Reserved Account",
                                  "merchantCode": "ALJKHDALASD"
                              },
                              "providerAmount": 0.21,
                              "paymentMethod": "ACCOUNT_TRANSFER",
                              "createdOn": "2019-07-24T14:12:27.000+0000",
                              "amount": 100.00,
                              "flagged": false,
                              "providerCode": "98271",
                              "fee": 0.79,
                              "currencyCode": "NGN",
                              "completedOn": "2019-07-24T14:12:28.000+0000",
                              "paymentDescription": "Test Reserved Account",
                              "paymentStatus": "PAID",
                              "transactionReference": "MNFY|20190724141227|003374",
                              "paymentReference": "MNFY|20190724141227|003374",
                              "merchantCode": "ALJKHDALASD",
                              "merchantName": "Test Limited"
                              "payableAmount": 100.00,
                              "amountPaid": 100.00,
                              "completed": true
                          }
                      ],
                      "pageable": {
                          "sort": {
                              "sorted": true,
                              "unsorted": false,
                              "empty": false
                          },
                          "pageSize": 10,
                          "pageNumber": 0,
                          "offset": 0,
                          "unpaged": false,
                          "paged": true
                      },
                      "totalElements": 2,
                      "totalPages": 1,
                      "last": true,
                      "sort": {
                          "sorted": true,
                          "unsorted": false,
                          "empty": false
                      },
                      "first": true,
                      "numberOfElements": 2,
                      "size": 10,
                      "number": 0,
                      "empty": false
                  }
              }


These are the endpoint for casual transactions and some of endnpoint are yet to developed which i will included in next version. i will also be including some new enhancement to the library for smooth financial transactions.