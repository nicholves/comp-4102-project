# Comp-4102-project - Nutrition Label Scanner (REST API and Client)

## Installation

To install the required Python libraries, run the following command from the root directory:
```bash
pip install -r .\requirements.txt
```
*You need to have pip installed to PATH*

To set up the git submodules run
```bash
git submodule update --init
```

To run OCR for this project, Tesseract OCR by Google is required. To install, follow the Instructions linked here [Tesseract OCR Install](https://tesseract-ocr.github.io/tessdoc/Installation.html)

To run flask server you can use, replace #.#.#.# with IPv4 Address of computer on your local network or 0.0.0.0 to run on all your computer networks
> You can find your local IPv4 Address using shell command
> `ipconfig` and local for the network your using. 

```bash
flask run --host=#.#.#.#.
```
*You need to have flask installed to path - [Flask Install](https://flask.palletsprojects.com/en/3.0.x/installation/)*

When the Server starts it will output a few lines and one of them will look something like this:
`* Running on http://172.17.50.161:5000`

Take that address and paste it as the value of the serverURL in the NutritionApp/config.json
```json
{
    "serverURL": "http://172.17.50.161:5000"
}
```

You need to download the Expo Go App to run a mobile app on your mobile device. This can be downloaded Here [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent&hl=en_CA&gl=US) or [Apple App Store](https://apps.apple.com/us/app/expo-go/id982107779)

To start expo client on mobile or add the `--android` flag to run locally on an Android emulator (*Requires Android Studio)
```bash
npx expo start
```
*You need to have npm and expo installed*

## Using the APP
The Nutrition App takes images from both uploads via the User's Camera Roll or Camera.
The user can get and save the Nutritional Facts for the image or clear and get the facts for a new Image.
The Data for the nutrition Label is stored with the Date and can be accessed by clicking the History Button
