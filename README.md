# Hungr.ai Hungr.ai Hippos

Our HackWestern IV project which makes hungry hungry hippo even cooler. 

## Milestones

![](https://lh3.googleusercontent.com/3aMNhTYf4PS7WqzfnF7ixc37c_hb3r4TDMSZnRqgkkCNj00AA2hKiXUqApAv69C9i-EuR_52UAPToIpQL9bsYZ3tguoEmxKOdraIXiF9DlQdlILbEJ4cS0uSlXioLNpztL2Uau0jUwukjCiu0v81DM7GftLWO3qoh7flAKmGXkJuPMPR_objm9oEYEtHmrUcNcQpKCqbH6PrxDdlKqCfRmu49J2j7NmZ2eOq1dCGjZW9YsVd231aUoHwcgjELQe-wTwNPcUPyiUXfdiW76nbzaxdA2wqTmSSemUKevO8a1F87n8rfFM2pvMZj9KXiDhAasWNYdFk_LXhEYCynV6yqZ5eX2erRTH7MI3j0kdNnjoz2VGv-_qNlz4bLioJyLsDLPLtB5o7QviekSKecPmia1yH3c852j_5sOTs-GpKGljcwyWuIBmqYr5iqwNyFV1bNZMU4JcTVkR_NSBTSloYJsm5KLfA1sE9mtpgcx23vMkp4_ymWfOvhU9RKOYoHM1Wtwxo17sqD79ysdmUHDPcOuOEAW9Gy0jVahzpeLd0s6fza6SNJ22v6DanYS9q1n4zrf9g0ZtdZ2bYHmr87mTfccgid_VKyzz0adsMWgKoX2aHKh3MOjRp6Dg9gv02Ua_ts2sL-aI-c54AUBzhm12tE9R2yX2QnXT2UQIDoLrqiheKQ2jisqOYWfPrALp8=w892-h668-no)

![](https://lh3.googleusercontent.com/loOI5W2EKDSdmqNiBMP-3ZAaLGAArS_c9VySHEdPT2ajWtkKVfbIaW93VTh4aSu9htMTUcBmMbB_m4E4uoRd6qx2YgsTO-5mHLfyPeh34ayauUK2UDE4X0tvrrWLSCulDbFG6H83HcXEgt2THMtwP5ePX63ROLFonCfEGKjVwokDoHYT-0kXSkcR0ZPPW6G1X0UzATSAUpkG05bKApx8-u-abHWgBPux5fnf8tfyglyY9RZjOq9_dnodhcd1DmrvR9QNNpTswePfEnTl_Oe7COjj16EP0ALUhaKl1lDCF5FN0CzzF-R2DIR0P4b2rzGy2oO3b6Mx2aR39iiokU9A6exurnwePGnmwj-uu3BnQQEpVrCPGV4tNfxF5394BXukpFzPVYlgGXr4nrU0eLlCYoz_qheKp0FhDV9inns80MmRxpto2M_FU3Nt7m_aL3WdLftYzxLwrA5hojBUqmxFvu05lQV7zsTojjqM9Nu77MoQzOr1ZuXkghqQFmaL8wjFblTSAXdxff38pqNcr01L9D64SMMmUyzVI3sdygQKjGM3bI_YJ-F2LTZ8cSqtsjtU4y_c7-MKw42PSkH_kBTSyO4NP1lq_BPVVh0XGMqInbIj_r1g3WZNokXCswRrpfob1mbbADPkHkSSJMo_yiE6RmWB3f67u88zHg5adleJULEXl1EXl7tDNLGpOUBt=w892-h668-no?authuser=0)

## Inspiration
Metaphysically speaking, we didn't find the idea, it found us. 

## What it does
A multiplayer game which allows player to play against AI(s) (one for each hippo) while controlling the physical hippos in the real world. 

## How we built it
Once, we knew we wanted to do something fun with hungry hungry hippos, we acquired the game through Kijiji #CanadianFeels. We deconstructed the game to understand the mechanics of it and made a rough plan to use servos controlled through Raspberry Pi 3 to move the hippos. We decided to keep most of our processing on a laptop to not burden the Pi. Pi served as a end point serving video stream through **web sockets**. **Multithreading** (in Python) allowed us to control each servo/hippo individually through the laptop with Pi always listening for commands. **Flask** framework help us tie in the React.js frontend with Python servers and backends. 

## Challenges we ran into
Oh dear god, where do we begin?
* The servos we expected to be delivered to us by Amazon were delayed and due to the weekend we never got them :( Fortunately, we brought almost enough backup servos
* Multithreading in python!!
* Our newly bought PiCamera was busted :( Fortunately, we found someone to lend us their's.
* CNN !!
* Working with Pi without a screen (it doesn't allow you to ssh into it over a public wifi. We had to use ethernet cable to find a workaround)

## Accomplishments that we're proud of
Again, oh dear god, where do we begin?
* The hardware platform (with complementing software backend) looks so elegant and pretty 
* The front-end tied the whole thing really well (elegantly simplying the complexity behind the hood)
* The feed from the Picamera to the laptop was so good, much better than we expected.

## What we learned
And again, oh dear god, where do we begin?
* Working with Flask (great if you wanna work with python and js)
* Multithreading in Python
* Working with websockets (and, in general, data transmission between Pi and Laptop over ethernet/network)

## What's next for Hungr.ai
* A Dance Dance Revolution starring our hippo stars (a.k.a Veggie Potamus, Hungry Hippo, Bottomless Potamus and Sweetie Potamus)
* Train our AI/ML models even more/ Try new models

## How do we feel?
In a nutshell, we had a very beneficial spectrum of skills. We believe that the project couldn't have been completed if any of the members weren't present. The learning curve was challenging, but with time and focus, we were able to learn the required skills to carry this project.

# Dev Setup
*Make sure you have Python3*
1. `npm run venv`
2. `./env/Scripts/activate` to activate virtualenv
3. Run `npm run build`
4. Run `npm start`
5. Go to <a href="http://localhost:5000/" target="_blank">http://localhost:5000/</a>
6. `deactivate` to get out of virtualenv
