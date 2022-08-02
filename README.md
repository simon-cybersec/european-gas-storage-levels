# European gas storage levels
A tool to get the current gas storage levels of the european countries.

Currently (July 2022) the gas levels in the european storage facilities are of huge interest. With this tool you can easily inspect them on your own.

# Before starting...
The data is released by the "Gas Infrastructure Europe" (GIE) which offers an API service for the public free of charge. To get access to the API you have to create an account [on their website](https://agsi.gie.eu/account). After sign up you get your personal API key.  

Clone this repository and create a file '.env' inside of which you specify you API key:  

        API_KEY=<your api key>

Hint: if you publish own code never include the API key. Make sure to add '.env' to your .gitignore file.
