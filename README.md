# PianoTilesBot
 
This project is a bot designed to automatically play the game Piano Tiles 2. Piano Tiles 2 is a popular mobile game where players need to tap on piano tiles that appear on the screen in sync with the music. The bot utilizes computer vision and automation to detect and tap the tiles, ensuring accuracy and high-speed gameplay.

Project Features:
	Tile Detection: The bot employs computer vision using the OpenCV library to process screen captures and identify the locations of active piano tiles.
	Action Automation: After detecting the tiles, the bot uses the PyAutoGUI library to automatically move and click the mouse to tap the tiles at the right moments.
	Multithreading: The bot utilizes multithreading for parallel execution of tile detection and automated tapping, enabling fast response times and near real-time gameplay.
	Game Area Customization: Users can configure the coordinates and size of the game area where the piano tiles are located to ensure accurate tile recognition and tapping.
	Flexibility and Extensibility: The project provides a flexible architecture that allows for easy modifications and expansion of the bot's functionality.

Technologies and Tools Used:

	Python: The programming language used to implement the bot.
	OpenCV: The computer vision library used for tile detection on the screen.
	PyAutoGUI: The library used for mouse and keyboard automation.
	Multi-threading: Multithreading for parallel execution of tile detection and automated tapping.
	GitHub: The platform used for storing and managing the project's source code.
	Installation and Usage instructions can be found in README

Installation and Usage Instructions:

	Clone the Repository:
		git clone <https://github.com/VisageDvachevsky/PianoTilesBot>

	Install Dependencies:
		pip install opencv-python pyautogui

	Open website with Piano Tiles 2:
		https://yandex.ru/games/app/166004

	Run the Bot:
		Open a terminal or command prompt.
		Navigate to the project directory.
		Execute the following command:
			python bot.py
		The bot will start running and automatically play Piano Tiles 2.
		Note: Make sure to have Piano Tiles 2 running and visible on your screen before running the bot.

		Caution: The bot will control your mouse and perform automated actions. Avoid interacting with your computer while the bot is running to prevent interference.

		Enjoy watching the bot play Piano Tiles 2 with precision and speed!

		If you encounter any issues or have any questions, please refer to the project repository for further information and support.