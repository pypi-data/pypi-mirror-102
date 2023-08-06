# python-reverso
A simple package to handle reverso.net services (translation, voice, dictionary etc.)

Run `pip install allreverso` to install the package.

[Click here to see the documentation](https://petitpotiron.github.io/python-reverso/)

Example of usage :
```python
import allreverso

client = allreverso.ReversoClient()
print(client.translate("en", "fr",
                       "Hello, this text has been translated by the reverso package in python."))  # a simple translation example
print(client.define("en", "boat"))  # a simple definition example
print(client.synonymize("en", "boat"))  # a simple synonym example
client.speak_to_mp3("en", "Hello !")  # a simple voice example

```
Have troubles ? Check our [discord ![discord widget](https://discord.com/api/guilds/831480772455038996/widget.png)](https://discord.gg/v4yfnjWKvy)
