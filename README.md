# ATM
implementation of basic ATM functionalities using python classes,methods and unittest

To clone this repository use the following command:

git clone https://github.com/sandeepsrikonda/ATM.git

To run tests using the unittest module, navigate to the ATM folder to find the file test.py which contains all the tests.

Run the script test.py or use the command "python test.py" on the command line to execute all the tests and obtain the results.



#########Details about the ATM implementation#########

atm_flow sub-directory has the main file ATM_features.py which implements the basic ATM functionalities

Core interface for the ATM is implemented inside ATM() function and it utilizes the account class to manage various functionalities like checking balance, withdrawing cash and depositing cash.

The account class is initialized by an account number, account_type and starting balance. Starting balance value is set to $1000 by default but once the ATM machine is integrated with bank servers, accurate balance information can be obtained. In addition to that, bank servers can also verify the login inside verifyPin() function instead of using its default value True.

Integration with ATM machine hardware can be also implemented inside card_reader(), dispense_cash() and verifyDeposit() functions. 

Therefore, this repository provides a flexible implementation of basic ATM functionalities that can be integrated with bank's software APIs and ATM's hardware API to provide more comprehensive features.
