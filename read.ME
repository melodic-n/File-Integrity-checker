# File integrity checker 

A simple but interesting project to make, you get to see how simple lines of code (for now) can help you keep your files tidy and most importantly keeps them _untempered_ which is very important in todya's age.


## How it works 
### initliazing databse 
If we want to make sure nothing has been tampered with, we need first something to compare it, a reference, in our case it's going to be a simple text file that contains every file's hash using SHA256 algorithm , for my test i picked one directory (~/Desktop/testfolder) and stored all the files's hashs within it , and to add security becuase obviously we can't keep them accessible to anyone to read so we encrypt the db file using **Fernet algorithm** with passphrase.

#### Fernet algorithm :
It is a symetric key algorithm, it includes two part :  generatekey() and encrypt() 

Since we are using passphrase, if we didn't we would have to store the key and frankly haven't thought where i would hide it, so i chose passphrase since you don't have to hide anywhere (besides your brain), it derives the key from the passphrase + randomly generated salt (16 byte) and we use the derivation function **_Argonid()_** and finally we encypt with **_encpryt()_** that takes the ey and what we want to encrypt 
Decryption goes similar just reverse , first we remove the salt (first 16 byte) and store it then this part is the same we use the Argonid() to derive teh key form the passphrse (that you must be remebering) and then we decypt with the key **_decrypt()_** 


To read more baout here where i read it from : https://cryptography.io/en/latest/fernet/


### File check
Afer creating our reference, we cna now compare any file we have stored its hash before, we simply take the file name as input , find it  and calculate its current hash and then look through our db by file name and comapre the hash, the stored and the just-now calculated , if its the same then the file hasnt been changed, but if its not then it has changed 



## imporvements

(to be written)
