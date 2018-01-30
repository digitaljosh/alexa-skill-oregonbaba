# Alexa Recipe Skill - *Baba G DIY Candy Kit*

*Developed with Python and Flask-Ask framework.*
***

Testing tools:

- ngrok: command-line program that opens a secure tunnel to localhost and exposes that tunnel behind an HTTPS endpoint.

- EchoSim.io: in-browser "virtual" Alexa testing tool

Personal testing plan:
1. Open Anaconda prompt and cd into project directory
2. type "python baba_recipe.py" in the command line
3. open up new Anaconda prompt and cd into joshu/devtools and type "ngrok.exe http 5000"
4. copy the last https endpoint
5. login to Amazon developer console and locate 'Baba G Recipe' skill
6. In the 'configuration' tab select 'HTTPS' radio button and paste the ngrok endpoint in the 'default' text box and 'save'
7. navigate browser to 'echosim.io'
8. start skill by saying invocation name 'start baba g recipe'

:)
