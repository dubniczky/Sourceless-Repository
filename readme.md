# Sourceless Website

This website displays text content, image and styling without containing any source code

If you open the page source `Ctrl + u`, it will be empty, also selecting the page components using developer tools will yield empty styling.

[[_TOC_]]

## Software Requirements

1. Python
1. Python Venv
1. Pip
1. Make

## Usage

### Automatic

1. Run `make`
1. Open browser: [http://127.0.0.1:8080](http://127.0.0.1:8080)

### Manual

1. `make venv` to create virtual environment.
1. `make install` install python dependencies to venv.
1. `make run` start the server.
1. Open browser: [http://127.0.0.1:8080](http://127.0.0.1:8080)

## Attributions

- Flower image: [pexels](https://www.pexels.com/photo/yellow-flower-on-white-surface-11431628/)

## Browser Compatibility

Loading sylesheets using the link tag is not an RFC standard.

|Browser|Version|Compatibility|
|---|---|---|
|Firefox|`99.0`|✅|
|Chrome|`101.0`|❌|
|Edge|`101.0`|❌|
|Brave|`1.38`|❌|
|Brave|`1.38`|❌|
|Safari|`15.4`|❌|
