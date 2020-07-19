# ocr-copy
> a hiGhLy aDVaNceD ProGRam eMPlOyInG OpTiCal cHaRAcTeR RecOgnItiOn AnD MACHinE LEArNiNG tO InTellIgeNTly iDeNtiFy, ReaD anD CoPY TEXt

This Python program brings up a selector on screen that you can use to create a box around text you want to copy. The program will then take that part of your screen, feed it into Tesseract's OCR engine and automatically copy the output to the clipboard.

Ok, so for the most part **this program is a joke**. It's intended to be a mockery of the over-use of 'machine learning' and 'artificial intelligence' as a marketing ploy by recreating the copy text function in a painfully unnecessary and convoluted way.

That said, it *could* be taken and used in a direction that gives it some semblance of a practical application. Other than that, it's a joke I wasted too much of my time on.

**Currently only supported for macOS**

## Installing

### Dependencies
This program is dependency hell. It requires the following:

* python 3
* pyglet==1.3.0 *(the only feature used is deprecated in newer versions)*
* pynput
* pyscreenshot
* pytesseract
* pyperclip
* numpy
* Pillow

### Setting up Tesseract
The core of the program requires the Tesseract OCR Engine to be installed. Detailed installation instructions can be found in the Tesseract docs ([https://tesseract-ocr.github.io/tessdoc/Home.html](https://tesseract-ocr.github.io/tessdoc/Home.html)).


**TL;DR for macOS users**
```
brew install tesseract
```

Additional language and script data can be installed as well to extend this program's functionality beyond just English. These have to be separately installed. Details are on the docs above. Data files are also available [here](https://github.com/tesseract-ocr/tessdata).

More info about languages later.

### User installation
ocr-copy is available as a PyPI package so you can install this monstrosity with minimal effort.

```
$ pip install ocr-copy
```

## Usage
If you've made it this far, I commend your persistence. Lucky for you, ocr-copy can be started straight from the command line.

**Important:** depending on your OS, screen and input monitoring may be disabled. On macOS, for this program to work properly, you need to enable these permissions for the app you will run it from. The permissions are at `System Preferences > Security & Privacy > Privacy` on the left pane under `Input Monitoring` and `Screen Recording` respectively.

To run the program such that it only detects English:
```
$ python -m ocrcopy
```
*More about languages under the **Languages** section*

Once the program is running, follow these steps in order to copy text:
1. Hit the hotkey `Command + Shift + 6` to activate the selection mode
2. Use your cursor to make a box around text you want to copy as if you were taking a screenshot and let go
3. ???
4. Profit

### Languages
Is English too lame for you? Well, Tesseract has trained data for dozens of other languages and scripts to fit your fancy. As long as you have them installed, you can use them with ocr-copy

For a more robust coverage of different languages and scripts, activate ocr-copy using
```
$ python -m ocrcopy -l
```
*This covers English, Arabic, Simplified Chinese, Russian, Greek, Japanese and Hindi.*

For a more custom experience, you can add a string afterwards of the language(s) you want to be included using the code assigned by Tesseract and separated by `+`. For example:

* Russian: `$ python -m ocrcopy -l rus`
* English & French: `$ python -m ocrcopy -l eng+fra`
* Simplified Chinese & Japanese: `$ python -m ocrcopy -l chi-sim+jpn`

You can string as many languages together as you'd like, but too many will slow down the time to copy.

A full list of supported languages, scripts and their codes are available [here](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc). I'll list some of the more common/interesting ones in this handy table:

| Language              | Code      |
|-----------------------|-----------|
| Afrikaans             | `afr`     |
| Arabic                | `ara`     |
| Bengali               | `ben`     |
| Czech                 | `ces`     |
| Chinese (simplified)  | `chi-sim` |
| Chinese (traditional) | `chi-tra` |
| German                | `deu`     |
| Greek                 | `ell`     |
| English               | `eng`     |
| Maths notation        | `equ`     |
| French                | `fra`     |
| Hindi                 | `hin`     |
| Italian               | `ita`     |
| Japanese              | `jpn`     |
| Korean                | `kor`     |
| Dutch                 | `nld`     |
| Punjabi               | `pan`     |
| Polish                | `pol`     |
| Portugese             | `por`     |
| Russian               | `rus`     |
| Spanish               | `spa`     |
| Thai                  | `tha`     |
| Vietnamese            | `vie`     |