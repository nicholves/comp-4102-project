# Comp-4102-project - Nutrition Label Scanner (REST API and App)

## Installation

To install the required Python libraries, run the following command from the root directory:
```bash
pip install -r .\requirements.txt
```
*You need to have pip installed to PATH*

To setup some things either run the setup.ps1 script or setup.sh
```bash
./setup.ps1
```

To run flask server you can use, replace #.#.#.# with IPv4 Address of computer on your local network or 0.0.0.0 to run on all your computer networks
> You can find your local IPv4 Address using shell command
> `ipconfig` and local for the network your using. 

```bash
flask run --host=#.#.#.#.
```
*You need to have flask installed to path*

When the Server starts it will output a few lines and one of them will look something like:
`* Running on http://172.17.50.161:5000`

Take that address and paste it as the value of the serverURL in the NutritionApp/config.json
```json
{
    "serverURL": "http://172.17.50.161:5000"
}
```

To start expo client on mobile or add the `--web` flag to run locally on the web
```bash
npx expo start
```
*You need to have npm and expo installed*

## Using the APP
The Nutrition App takes images from both uploads via the User's Camera Roll or Camera.
The user can get and save the Nutritional Facts for the image or clear and get the facts for a new Image.
The Data for the nutrition Label is stored with the Date and can be accessed by clicking the History Button
