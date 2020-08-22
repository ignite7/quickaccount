# Quickaccount 📨

If you want to make an random account easily this **CLI** it wiil be of great
help for you, as I said before if you want to make a quick account you can do it
with the option **_Fastmail_** that's simple email provider that allows you
create an account without captcha but if you want use others known providers
you can use **_Hotmail_** or **_Protonmail_** but you have to pass the
captcha but don't worry if you aren't a robot you can pass it.

## Setup 🧲

- It's **important** to know you need to have [**_chrome_**](https://www.google.com/chrome/) installed on your machine or get the [**_chromedriver stable release_**](https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/) 

```bash
git clone https://github.com/ignite7/quickaccount.git

cd quickaccount/

pip install .
```

## Usage ✔️

- The usage is so simple when you finish the setup you can run `quickaccount`
from your **_Terminal_**

    + You must choose a provider

    ```bash
    quickaccount fastmail
    ```

    + It's optional but you can choose an (username, password, domain)

    ```bash
    quickaccount hotmail -u pepe -p easypass -d hotmail.com
    ```

    + If you reach the limit of account created by your **_public IP_** you can
    use the flag ```--proxy || -P``` for using a **SSL** proxy

    ```bash
    quickaccount protonmail --proxy

    quickaccount protonmail -P
    ```

    + And last but not least you can always use ```--help``` for look all the
    options

    ```bash
    quickaccount --help
    ```

## To do 🔮

- Add more service providers
- Add more web browsers

## Thanks 👏🏻

> **_Made By:_** [Sergio van Berkel Acosta](https://www.sergiovanberkel.com/)
