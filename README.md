# snapraid-smart-server
Displays the command `snapraid smart -v` as a webserver.

## Usage
0. Set desired update interval (default 12 hours)

    ```python
    interval = 60 * 60 * 12  # Run every 12 hours
    ```

1. Run as root

    ```shell
    sudo python3 smartserver.py
    ```

2. Access through browser: 

    ```shell
    localhost:8888
    ```