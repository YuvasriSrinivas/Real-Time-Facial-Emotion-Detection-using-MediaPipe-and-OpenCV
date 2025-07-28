# Real-Time-Facial-Emotion-Detection-using-MediaPipe-and-OpenCV
Developed a real-time facial emotion detection system using Python, OpenCV, and MediaPipe Face Mesh. Detects emotions like Happy, Sad, Angry, and Surprised by analyzing facial landmarks. Optimized for smooth webcam performance. Ideal for AI-driven human-computer interaction and emotion-aware applications.
Absolutely! Here's a **complete `README.md` file** for your **Real-Time Facial Emotion Detection** GitHub project — professional, informative, and includes an output preview section with instructions.

---

## 📘 `README.md`

```markdown
# 🎭 Real-Time Facial Emotion Detection using MediaPipe & OpenCV

This project is a real-time facial emotion recognition system built with **Python**, **OpenCV**, and **MediaPipe Face Mesh**. It detects and classifies human emotions like **Happy**, **Sad**, **Angry**, **Surprised**, and **Neutral** based on facial landmark analysis — all live from your webcam.

---

## 🚀 Features

- 🧠 Detects emotions using facial geometry (eyes, mouth, iris)
- 🎥 Real-time webcam capture with emotion overlay
- 🎯 Classifies: Happy, Sad, Angry, Surprised, Neutral
- ⚡ Optimized for smooth performance (30 FPS)
- 🔊 Optional voice feedback (disabled by default)

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** OpenCV, MediaPipe, NumPy
- **Optional:** pyttsx3 for text-to-speech (disabled in current version)

---

## 📷 Sample Output

| Emotion | Live Detection |
|--------|----------------|
| Happy 😊 | ![happy](https://i.imgur.com/5fKPXTN.png) |
| Sad 😢 | ![sad](https://i.imgur.com/2qHKkgP.png) |
| Angry 😠 | ![angry](https://i.imgur.com/xtN02E0.png) |

> *Note: Replace with your own screenshots if needed*

---

## 📁 Project Structure

```

emotion\_detector/
├── emotion\_detector.py
└── README.md

````

---

## 📦 Installation

1. **Clone this repository**
```bash
git clone https://github.com/YOUR_USERNAME/emotion-detector.git
cd emotion-detector
````

2. **Install dependencies**

```bash
pip install opencv-python mediapipe numpy
```

> *(Optional for voice)*

```bash
pip install pyttsx3 pywin32
```

3. **Run the application**

```bash
python emotion_detector.py
```

---

## 🧠 Emotion Detection Logic

| Emotion      | Landmark Conditions                   |
| ------------ | ------------------------------------- |
| 😲 Surprised | `mouth_open > 15` and `eye_open > 10` |
| 😠 Angry     | `eye_open < 5` and `mouth_open < 5`   |
| 😊 Happy     | `eye_open > 6` and `mouth_open > 10`  |
| 😢 Sad       | `iris-eye center distance > 12`       |
| 😐 Neutral   | None of the above                     |

---

## ⌨️ Controls

* **ESC** – Exit the webcam window

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Yuva Sri Srinivas**
📫 [LinkedIn](https://www.linkedin.com/in/yuvasrisrinivas)
🌐 [Portfolio](https://yuvasrisrinivas.github.io/yuvasrisrinivas-Portfolio/)

---

## ⭐ Star This Repository!

If you found this project useful, consider starring ⭐ the repo — it helps others find it too!

```
