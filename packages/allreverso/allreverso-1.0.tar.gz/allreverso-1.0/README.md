# python-reverso
A simple package to handle reverso.net services (translation, voice, dictionary etc.)

Run `pip install reverso` to install the package.

[Click here to see the documentation](https://github.com/PetitPotiron/python-reverso/)

Usage :

```python
import allreverso

client = allreverso.ReversoClient()
print(client.translate("en", "fr",
                       "Hello, this text has been translated by the allreverso package in python."))  # a simple translation example
print(client.define("en", "boat"))  # a simple definition example
print(client.synonymize("en", "boat"))  # a simple synonym example
client.speak_to_mp3("en", "Hello !")  # a simple voice example

```
