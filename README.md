# Monopoly Simulator 

Probablity on a player landing on a property while playing Monopoly

## Getting Started

### Prerequisites

I used homebrew to install python3 on my OSX.
You can install it anyway you feel like.
```
brew install python3
```

Using pip to install other prerequisites
```
python3 -m pip install psd-tools numpy scipy pygame==2.0.0.dev6
```

### Installing

PyGame UI version
```
python3 Monopoly.py <turns_per_game>
```
For UI generation, tool parses through .psd file and generate Game UI directly. 
Read PSDReader.py for more info.


Keep UI.psd next to the py script. 

Layer named ScreenSize is required, PyGame uses this for Window initiation. 

Text elements are taken by name from PSD.


PyGame CMD Line version

```
python3 GameCode.py
```

## Built With

* [Python](https://www.python.org/)
* [PyGame](https://www.pygame.org/news)
* [Psd-tools](https://psd-tools.readthedocs.io/)

## Contributing

Mail me at sanchit.gulati@gmail.com

## Authors
* **Sanchit Gulati**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

[The Mathematics of Winning Monopoly](http://www.dropwizard.io/1.0.2/docs/)
