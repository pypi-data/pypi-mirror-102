## Welcome to PygFW

PygFW stands for `Pygame Framework` and is a framework I create to be used in creating games with pygame. It has many builtins that help to eventually run your own game (hopefully with minimal effort!). In the docs you will find examples, usage and dev notes for everything within the framework. For starting out, we'll look at an example of creating a game with one scene and a controllable character: visit [here](). 

As a note, PygFW was built with the idea of using image sprites so to create entities using pygame shapes, (for the time being) we will have to take a look at building a custom class with different functions, we'll do this [here]() (It will be using inheritance so if this is too advanced for you, I recommend just using image sprites. 

I use two free platforms and would recommend them: [Piskell](https://piskellapp.com) and [Paint.Net](https://getpaint.net) for my sprites. The former of which has a better user interface in my opinion however the latter allows for inherent opacity changes.

To get started, you'll want to install the package using pip:

`python3 -m pip install PygFW`

If all runs smoothly, you should then have at PygFW installed and can import it to use in your game with. (I recommend also initialising pygame although it isn't currently required)

```py
import PygFW
pygame.init()
```

Now you can go on to make your game! Don't forget to check the docs if you don't know how something works or how to do something. Enjoy PygFW!
