
<h1 align="center">Autoclicker_online_game_pokeclicker</h1>


<p>
    Python auto clicker to automatize repetitive tasks in the online game pokéclicker
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">TO DO</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
---
## About the project 

This project is an auto clicker initially developed to help with repetitive tasks in the online game PokeClicker such as: 
- clicking for attack
- doing a dungeon 

### Built with

* Pynput to control and monitor the mouse and keyboard
* PIL to take a screenshot and analyze its content
* threading to launch multiple threads (one for clicking or dungeons and another to monitor the keyboard input)

---
## Getting started

To start using the auto clicker, you only need to download the repository, have a Python environment installed, and change variables in the Autoclicker_pokeclicker_online.py to fit your computer set up for the dungeon.


### Prerequisites
You need a Python environment installed to run the code and install the library needed ( the command can change in function of your environment): 

- Pynput: pip install pynput
- PIL: pip install Pillow
- Threading: pip install threading


### Installation

1. Download or clone the repository 
2. Use the readandpixel.py file to find the right constant for dungeons
3. Change the constant value in the Autoclicker_pokeclicker_online.py file
4. run the Python code

Details of the constant search for our screen setup:
1. Run the readandpixel.py file
2. Go to your Pokéclicker page and select the wanted dungeon
3. click on the 's' on the keyboard:
   *your mouse will move to the location specified in _entrance_button_position_
   *Verify that is going on the dungeon start button if not retry other value



<img width="960" alt="2023-11-02 16_35_04-Greenshot" src="https://github.com/KmilleK/Autoclicker_online_game_pokeclicker/assets/57387482/24d19171-5a79-4764-859e-f36a86d4d602">

   
5. start the dungeon and go on the boss tile start screen 
6. click on the 't' on the keyboard:
   *a screenshot of the screen (the _screenshot_box_) will be shown with the position of a evaluate pixel _pos_
   *This pixel should be on the red button Start Bossfight
   *Copy the RGB value of the pixel that is returned in the Python console


![pixel_position](https://github.com/KmilleK/Autoclicker_online_game_pokeclicker/assets/57387482/89be8821-f65c-4de9-98d3-025591a5e5d2)


---
## Usage 

To use the autoclicker, you need to run the Python code and then it will wait for input of the keyboard to execute different tasks. The key list is: 

* m (start/stop): repetitively push the mouse left click at a defined rate
* l (start/stop): dungeon routine (start the dungeon, walk the dungeon until the boss is killed, repeat)
* e: stop the Python script exit immediately if any tasks started  

When the mouse is moved or the screen is scrolled the task is stopped ( not the auto clicker)

[Video 1: Autoclick attack](https://github.com/KmilleK/Autoclicker_online_game_pokeclicker/assets/57387482/e0dce7de-7fb5-4559-b14f-64b13e6f64e7
)


https://github.com/KmilleK/Autoclicker_online_game_pokeclicker/assets/57387482/f6b4c7bc-aae1-4e8d-a450-8c742323be0e


---
## TO DO

- [ ] exit keyword sometime bug when dungeon is start
- [ ] different dungeon size input by the user  



