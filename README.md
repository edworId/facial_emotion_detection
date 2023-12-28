<h1 align="center"> Facial emotion detection using a shell GUI menu </h1>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=COMPLETO&color=GREEN&style=for-the-badge"/>
</p>

This project uses Python to detect faces and emotions with FER2013. Furthermore, it uses a Shell Script to develop a GUI menu to help the user use it.

Facial expression detection from a picture or a live camera stream implemented with convolutional neural networks in Keras and OpenCV.

The dialog command is a command-line tool used to create text-based user interfaces on Unix-like systems. It provides an interactive way to display dialog boxes, menus, and forms in the terminal.

## Basic Requirements

You will need to install **Dialog** package, run in your terminal:

```
sudo apt-get install dialog
```

You must give permissions to use this project, run in your terminal:

```
chmod a+x -v *.sh
```

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/edworId/facial_emotion_detection.git
    cd facial_emotion_detection
    ```

2. Run the main script:

    ```bash
    ./face.sh
    ```

3. Follow the instructions in the menu to choose the desired action.

  - **TAKE A PICTURE**: Capture an image and perform associated operations.
  - **DETECT EMOTION FROM IMAGE**: Detect emotions in an image.
  - **LIVE EMOTION DETECTION**: Perform real-time emotion detection.
  - **BACK TO MAIN MENU**: Return to the main menu.
  - **EXIT FROM PROGRAM**: Exit the program.

## DATASET

Dataset: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/overview

<h1 align="center">  </h1>
<p align="center">
<img width="900", img src="https://github.com/edworId/facial_emotion_detection/blob/main/menu.png"/>
</p>

<h6 align="center">This interface was built using Dialog, text based menu. </h6>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


<h2> Author </h2>

[<img src="https://avatars.githubusercontent.com/u/110691832?s=400&u=e671447386d38975c165bff78b715ea80549c069&v=4" width=115><br><sub>Edmundo Lopes Silva</sub>](https://github.com/edworId)  

<p align="center">
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Shell-Script-00000F?style=for-the-badge&logo=&logoColor=white"/>
</p>
