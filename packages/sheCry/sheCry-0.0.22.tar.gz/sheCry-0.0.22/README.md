**SHE Cryptography**
========================
The expansion of SHE is **Secure Hybrid Encryption**. It is a cryptographic system that transforms plaintext into ciphertext so that secret communication is ensured through insecure channels like the Internet.

--------------------
**Preface**
--------------------
SHE is a hybrid and lightweight cryptographic concept that ensures faster processing speed along with better security. Theoretically, a hacker needs to go for 2^256 = 1.16e+77 possible ways in terms of finding the correct key to decrypt the ciphertext if the secret key is 256 bits long and secure with a hashing function. It is by far impossible for a regular user device to solve the math. It will be needed a supercomputer to do the computation. However, a low computational powered device (e.g. IOT device) can easily handle it because of its symmetric and stream cipher architecture. Thus, it makes the algorithm faster. Also, SHE is a software and hardware-independent cryptography. Last but not least, as technology is getting revolutionized day by day, it is embracing lightweight and low-powered systems. As a matter of fact, today's cryptography also needs to be lightweight and ensure better security and performance. This is why this new innovation, SHE Cryptography can make a fruitful impact in today’s security epidemic.

--------------------------------
**Project Scenario Problem**
--------------------------------
Nowadays, security has become one of the most burning and sensitive issues. Confidential data is being stolen by malicious attackers rapidly. To prevent this kind of act, many security measures have been established. But “Cryptography” plays the most crucial part when we call for security. This is so because cryptography is used to protect enterprise information and communication from cyber threats through the use of codes. For example, AES and RSA are the gold standards. They are very popular and still vastly used in many renowned organizations as well as in the government. But the drawback is, AES is hardware and software dependent. So, we need to design it according to hardware and software systems. As a result, this implementation increases time and cost. Also, the attacker uses a “Side Channel Attack” to break AES. As a result, it becomes vulnerable. AES performs great in 256 bits keys and is faster in powerful devices. But if it is used in a low computational powered device then we have to use fewer bits (e.g. 64 bits), or the device could not handle the calculation of larger numbers. Thus, AES performs badly in this criterion. If we use fewer bits in AES, then a “Correlation Power Analysis Attack” is possible. So, it is not worth using AES in low computational powered devices. Whereas, RSA is slow due to its large mathematical calculation with large numbers and asymmetric mechanism. As a result, RSA fails to perform in terms of speed and low computational power. Also, the world is switching to lightweight technology day by day. IOT is the best example of it. But to secure those less powerful electronics, there is no such effective cryptographic system yet. Also, breaching the confidential data of the government and the corporate world is a very old topic and it still remains a rapid concern. So, we really need to innovate a new cryptographic algorithm that gives better results in low-power electronics and performs faster, and gives better security in sharing data. This is where lightweight cryptography SHE comes to play.

----------------------------
**Solution Statement**
----------------------------
* **Environment Independency:** SHE is reliable on any platform weather it is for software or hardware. So, developer does not need to hassle with cryptographic system while designing a software or hardware. Thus, it decreases a developer's production time as well.

* **Cost Effectiveness**: In 2007, about 10% of the average IT budget was spent on energy, and energy costs for IT were expected to rise to 50% by 2010. However, the cost of power supply generally depends on the maximum possible power that could be used at any one time. If a CPU needs to calculate a larger number for a cryptographical system, it needs more power and more efficiency to compute in a very short time. As a result, this increases costs most of the time. To reduce cost, many electronic products choose to use a much lighter system. This is where the SHE cryptographic system plays a major role. It reduces the clock rate when it processes large numbers of cryptographical computations. Thus, it reduces cost.

* **Better Security**: No doubt SHE gives better security. It encrypts and decrypts with ChaCha20 algorithm, checks integrity with Poly1305 algorithm and authenticates user with ECDH key exchange protocol. In short, SHE Cryptography completely satisfies the CIA triad of a security system.

* **Faster Speed & Low Latency**: SHE is a stream cipher version of symmetric cryptography. As a result, it encrypts and decrypts the message instantaneously after doing XOR. It can calculate 128 bits and 256 bits easily or sometimes even larger. So, a user should not face any problem if he wants to communicate with others, or wants to download and upload a content.

* **Power Loss Reduction**: CPU gets always hot for its cryptographic system, because this kind of system does massive mathematical computation. As a result, sometimes PSU (Power Supply Unit) could not supply such power that required to perform the task efficiently. So, overloading power causes the systems goes down sometimes or burns the CPU circuit. But the lightweight architecture of SHE, it requires less power to perform its mathematical computation and reduce power loss problems.

--------------------------------
**Ideal Applications To Use**
--------------------------------
* **Low Power Electronics**: Networking devices like PAN, LAN, WAN devices can use this system easily. Not only Mobile but also Watches can use this cryptography efficiently. However, technology like IOT which is one of the most booming electronics nowadays, is also a less power consumption tech product. As a result, it must need lightweight cryptography like SHE to perform securely, faster, and more efficiently without any interruption.

* **Government and Business Communication**: SHE cryptography is applicable to sharing confidential data between government and business agents. This cryptography ensures the total CIA triad (Confidentiality, Integrity and Availability) of security. Also, SHE gives strong protection against malicious attacks (e.g. MITM Attack) because of its ECDH (Elliptic Curve Diffie-Hellman) key exchange protocol. So, this cryptography is reliable in government and business communication.

* **Database Encryption**: In database systems, governments and organizations rely on vendors, but there is no guarantee that the data is protected. SHE can be implemented to store data into ciphertext with the ECDH protocol. As a result, any unauthorized person or third party organization won’t be able to use our confidential data unethically.

* **Banking**: Many online banking and payment applications require the verification of personally identifiable information before proceeding with their transactions. It helps in predicting the correct information to prevent fraudulent activities and cybercrime. This is where SHE can easily authenticate users in the money transaction system, such as credit or debit card transactions or online banking sessions.

----------------------------
**Installation**
----------------------------
To install this project in your local server -

    pip install sheCry

----------------------------
**Usage / Example**
----------------------------
This is an example how you can write your code so that it runs successfully.

    # We will fetch crypto class from sheCry package

    from sheCry import crypto

    
    # We will input the length of the shared key that the sender and receiver will share with each other for communication

    sharedKey = int(input("Key length for shared key value: "))

    
    # We will input the length of the private key which must remain secret

    privateKey = int(input("Key length for private key: "))

    
    # We will enter the message to send it to the receiver

    message = input("Enter message: ")
    

    # Now we will call crypto() and make it a class variable

    she = crypto()
    

    # We will call key() method and insert our sharedKey and privateKey

    she.key(sharedKey, privateKey)
    

    # Now, it's time to encrypt the message and print the ciphertext

    ciphertext = she.encrypt(message)

    print("Ciphertext:", ciphertext)

    # In authentication, the sender key and receiver key must be matched

    if she.auth() is True:

        # Plaintext will be revealed if the sender key and receiver key are matched

        plaintext = she.decrypt()

        print("Plaintext:", plaintext)

        # show() method will present all the execution steps

        she.show()

    else:

        print("Authentication failed!")

----------------------------
**Program Utilization**
----------------------------
* A user inputs the length of private keys and generated shared keys.
* A user inputs message.
* Generates prime number according to Fermat Prime Number Theorem.
* Generates private key.
* Generates public key according to private key.
* Diffie-Hellman key exchange protocol is used for authenticity checking, where a sender locks the message with a receiver's public key and the receiver unlocks it with his private key.
* The message is encrypted and decrypted by ChaCha20 algorithm.
* Poly1305 algorithm has been used for integrity checking.

--------------------------------
**Caution**
--------------------------------
* Know SHE Cryptography properly through the documentation before using it.
* Anyone can use this cryptography for free only for education, research, and development purpose.
* SHE is absolutely not for unethical motives. Creator will not be found guilty if anyone uses this for illegal purpose.

--------------------------------
**Do You Want To Know Me?**
--------------------------------
* **Call**: +8801818832925
* **Email**: tahsin.ahmed@g.bracu.ac.bd
* **Social Media**: https://www.facebook.com/ahmedinsider