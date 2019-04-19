# DMP Console

## How it works

The console will give you option(s)

> (1) Create and add a Weapon to a character
  * Console will ask user to provide a name, dice details, and description for the weapon, as will as which character to send the weapon to.
  * Console makes a POST request to add the weapon to the character.
> (2) View a Character
  * Console will ask for the character's id.
  * Returns the character's name, description, race, level, weapons, and skills.
> (3) Random Loot
  * This will hit the api to retrieve a random item.