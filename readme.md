## Zihan Guo 15-112 Term Project ReadMe

### Project Title: Café Poirot with Amuro Tooru
### Project Description
This project is inspired by *Detective Conan*, or 名探偵コナン , by Gosho Aoyama. Amuro Tooru, or 安室透, an important character in *Detective Conan* runs a cafe called Café Poirot, also known as "喫茶ポアロ". The project "Café Poirot with Amuro Tooru" is a simulation game, where the player will be helping Amuro Tooru to run Café Poirot. 

The player starts on a workday at Café Poirot. Throughout the workday, the player is able to move the character around, select ingredients, cook food, and serve dishes to customers by walking up to them. There will be four available seats in the Café. When there are empty seats, customers will enter the Café one by one to a randomly selected available seat, with a randomly selected time interval between two customers, following a randomly generated path. The customers will be randomly chosen from a list of characters, all of whom are from *Detective Conan*, and a certain customer will be ensured that they will not appear more than once at the same time in the cafe. The customer's orders will also be randomly selected from a list of available menu items. The customer will leave when they finish eating their food. The player will work for five minutes, where their score is based on the number of dishes and number of customers served. A highest score will be saved globally even after the player closes the application.

Have fun! ☕️

### Run Instructions

The project uses libraries `cmu_graphics`, `PIL`, `random`, `os`, and `pathlib`.

`cmu_graphics` can be installed via [https://academy.cs.cmu.edu/desktop](https://academy.cs.cmu.edu/desktop). 

`PIL` can be installed by following the instructions via [this link](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html).


After the user has installed `cmu_graphics` and `PIL`, there are two ways to run the game.

####1
If the user currently has `src` folder, the user should download all of the files within the `src` folder to their local computer, and put `cmu_graphics` in `src`. The user should also download the music `gameStartMusic.mp3` and images `images` for this game via [this link](https://drive.google.com/drive/folders/1_v2HFEAg1NP9kINZ4GI792DNocJ6vqFE?usp=sharing). The file `gameStartMusic.mp3` and the folder `images` should be put inside `src` folder. Make sure that `cmu_graphics`, `gameStartMusic.mp3`, and `images` are at the same level as the Python files already in `src`.

####2
The user can also download a full version of the game via [this link](https://drive.google.com/drive/folders/1_v2HFEAg1NP9kINZ4GI792DNocJ6vqFE?usp=sharing). Make sure to also put `cmu_graphics` into this download folder.


The user should run `starter.py` to start the game.