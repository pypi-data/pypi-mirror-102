# webconnect

A simple python package and command line tool to publish static websites to RStudio Connect.

This package is not affiliated with RStudio.

## Command line tool

The primary way to use webconnect is via it's cli tiil, `webconnectcli`.

THe cli tool requires 5 parameters. 

* A path to a directory containing the static site to publish
* A unique name for the content on Connect - alphanumeric and underscores only
* A "pretty" name for the content that will be displayed in the Connect UI
* The URL for the Connect instance
* The Connect API key to use


```
usage: webconnectcli [-h] -d DIR -n NAME -p PRETTY -s SERVER -k KEY

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     name of the directory to publish
  -n NAME, --name NAME  name of the content - alphanumeric and underscores only
  -p PRETTY, --pretty PRETTY
                        pretty name
  -s SERVER, --server SERVER
                        RStudio Connect URL
  -k KEY, --key KEY     Connect API key
```

So a full example would look something like this:

```
webconnect \
  -d path/to/site/content \
  -n static_site \
  -p "Example.org main site" \
  -s https://connect.example.org \
  -k ${CONNECT_API_KEY}
```

This relies on the Connect API key being available in the `$CONNECT_API_KET` environment variable. 
You could use the key directly if you prefer.

## Package usage

```
import webconnect
webconnect.pub_rsconnect(
    "path/to/site/content,
    "static_site",
    "Example.org main site",
    "https://connect.example.org",
    "hgjhghgjguytuyt6876uytgfhg",
)
```
