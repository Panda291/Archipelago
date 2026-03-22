# Setup Guide for Ratchet & Clank Archipelago

This guide is meant to help you get up and running with Ratchet & Clank in your Archipelago run.

## Requirements

The following are required in order to play Ratchet & Clank in Archipelago

- Installed the latest version of [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases).
- The latest version of the [Ratchet & Clank apworld](https://github.com/Panda291/Archipelago/releases).
- A device to play on:
  - [RPCS3 Emulator](https://rpcs3.net/download).
  - A Homebrew enabled PS3 (easiest is PS3 HEN).
- A Ratchet & Clank PAL ISO (`NPEA00385`)
- The latest version of the [Ratchet & Clank Multiplayer Client](https://github.com/bordplate/rac1-multiplayer/releases).
- (optional) The latest version of the [Ratchet & Clank Multiplayer Server](https://github.com/bordplate/Lawrence/releases).

## AP World Installation

1. Download the Ratchet & Clank apworld file from the [GitHub Releases Page](https://github.com/Panda291/Archipelago/releases)
2. Double-click the `rac1.apworld` to install it to your local Archipelago instance
3. Restart the Archipelago Launcher

## RPCS3 Settings
- Make sure you enable networking:
    - Configuration -> System -> Network (in the top bar) -> Network Status to 'Connected'

## Installing the Ratchet & Clank Multiplayer Mod
To install the Ratchet & Clank Multiplayer Mod, it would be best to follow its [installation guide](https://github.com/bordplate/rac1-multiplayer/blob/main/README.md).
A short TL;DR:
- Have NPEA00385 installed to either your emulator or PS3 .\
    **Note**: **For PS3 only** a Ratchet & Clank PAL Trilogy (`BCES01503`) disk should also work.
- Get the latest release of the [mod](https://github.com/bordplate/rac1-multiplayer/releases)
- **For Emulator:** Go to Files --> Install Packages/Raps/Edats --> select the downloaded mod from the step before. \
Then you can launch `Ratchet Multiplayer` from the games list.
- **For PS3:** This requires a modded PS3, I will not be going into the details here. Look up PS3 HEN if you don't know where to start

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a YAML file?
- In the Archipelago Launcher use the "Generate Template Options" feature if you prefer editing your YAML in a text editor.
  - In your `Archipelago\Players\Templates`folder look for `Ratchet & Clank.yaml` 
- Alternatively, you can use the "Options Creator" (a GUI tool in the Archipelago Launcher) to customize your options and export your YAML file.

### Hosting your MultiWorld

This section is for players who want to host a solo or multiplayer game.

1. Collect YAML files from all participating players.
    - In the Archipelago Launcher, select "Browse Files" and open the `Players` folder.
    - Place each player's YAML file into the `Players` folder.

2. In the Archipelago Launcher, select "Generate" to create your multiworld.
    - The generated zip file will appear in the `output` folder.

3. To host online, upload the zip file from the `output` folder to the [Archipelago Website](https://archipelago.gg/uploads).

4. To host locally, select "Host" in the Archipelago Launcher and choose the zip file from the `output` folder.

### Connect to the MultiWorld

1. **If you host the multiworld on the website**, you can use the public multiplayer server to join it.
  - Simply start the Ratchet & Clank Multiplayer Client and select the 'Randomizer' Server from the public servers.
  - Here you can either press Circle to create your own lobby, or join one made by another player who will be playing on the same multiworld slot
  - The host of the lobby must fill in the multiworld room details to connect

2. **If you host the multiworld on your own machine**, you must also host a [Ratchet & Clank Multiplayer Server](https://github.com/bordplate/Lawrence/releases). in order to join it.
  - Hosting the server locally is as simple as running "Lawrence.exe" and selecting to host "rando" in the configurator.
  - The IP does not matter if you are not planning to port forward your server
  - Connecting to the local server can be done from the main menu of the Client by pressing Circle to 'Direct connect' to your machine, the IP for localhost is '127.0.0.1'
  - When you make a lobby, make sure to set the address to '127.0.0.1' or 'localhost' for your local multiworld room.


## Troubleshooting

If you need further help:
- Join the [Archipelago Discord](https://discord.gg/archipelago) and visit the `[PS3] Ratchet and Clank` thread in the `future-game-design` forum channel (located at the bottom).
- Check out the [Official Ratchet & Clank Multiplayer website](https://boltcrate.space).