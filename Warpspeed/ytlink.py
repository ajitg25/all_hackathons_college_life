text = '''
Sure, here's a roadmap for learning Blockchain in steps, along with some YouTube video links for each step:

Step 1: Introduction to Blockchain

What is Blockchain? (https://www.youtube.com/watch?v=_160oMzblY8)
How does Blockchain work? (https://www.youtube.com/watch?v=SSo_EIwHSd4)
Types of Blockchain (https://www.youtube.com/watch?v=SSo_EIwHSd4)
Step 2: Cryptography

Introduction to Cryptography (https://www.youtube.com/watch?v=GSIDS_lvRv4)
Public Key Cryptography (https://www.youtube.com/watch?v=GSIDS_lvRv4)
Hash Functions (https://www.youtube.com/watch?v=0WiTaBI82Mc)
Step 3: Smart Contracts

What are Smart Contracts? (https://www.youtube.com/watch?v=ZE2HxTmxfrI)
Smart Contracts on Ethereum (https://www.youtube.com/watch?v=ZE2HxTmxfrI)
Smart Contracts on Solidity (https://www.youtube.com/watch?v=ipwxYa-F1uY)
Step 4: Blockchain Development

Blockchain Development Basics (https://www.youtube.com/watch?v=-8Y2CcFZp8M)
Building a Blockchain in JavaScript (https://www.youtube.com/watch?v=zVqczFZr124)
Building a Blockchain in Python (https://www.youtube.com/watch?v=b81Ib_oYbFk)
Step 5: Decentralized Applications (DApps)

What are DApps? (https://www.youtube.com/watch?v=Zwq9FkUBjFM)
Introduction to Web3.js (https://www.youtube.com/watch?v=Vt0zCfNdpHw)
Building a DApp with Ethereum and React (https://www.youtube.com/watch?v=8rhueOcTu8k)
Step 6: Blockchain Use Cases

Blockchain Use Cases in Supply Chain (https://www.youtube.com/watch?v=xz7qVYZtTu8)
Blockchain Use Cases in Healthcare (https://www.youtube.com/watch?v=8nNkXEEAOUM)
Blockchain Use Cases in Finance (https://www.youtube.com/watch?v=EmkX9y9ls2s)
I hope these resources will help you learn Blockchain effectively. Good luck with your learning journey!
'''

t=  text.split('\n')
# print(t)

dict = {}
steps = []
for i in t:
    # print(i)
    if 'step' in i.lower()[0]:
        # print(i)
        steps.append(i)
        dict[steps[-1]] = []
    if 'https' in i.lower():
        dict[steps[-1]].append(i)

print(dict)

