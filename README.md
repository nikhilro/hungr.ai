# Hungr.ai Hungr.ai Hippos

Our HackWestern IV project which makes hungry hungry hippo even cooler. 

## Milestones

<img src="https://github.com/nikhilro/hungr.ai/blob/master/gif-1.gif?raw=true" width=500/>

<img src="https://github.com/nikhilro/hungr.ai/blob/master/gif-2.gif?raw=true" width=500/>

<img src="https://github.com/nikhilro/hungr.ai/blob/master/photo-1.jpg?raw=true" width=500/>

<img src="https://github.com/nikhilro/hungr.ai/blob/master/photo-2.jpg?raw=true" width=500/>

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
