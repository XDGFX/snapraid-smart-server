# snapraid-smart-server
Displays the command `snapraid smart -v` as a webserver.

## Usage

### Option 1: Run Manually
0. Set desired update interval (default 12 hours)

    ```python
    interval = 60 * 60 * 12  # Run every 12 hours
    ```

1. Run as root

    ```shell
    sudo ./smartserver.py
    ```

2. Access through browser: 

    ```shell
    localhost:8888
    ```

### Option 2: Run With systemd
0. Clone into `/opt/snapraid-smart-server/`

1. Set desired update interval (default 12 hours)

    ```python
    interval = 60 * 60 * 12  # Run every 12 hours
    ```

2. Run installer script

    ```shell
    sudo ./install-service.sh
    ```