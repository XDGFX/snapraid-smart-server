# snapraid-smart-server
Displays the command `snapraid smart -v` as a webserver.

## Usage

### Option 1: Run Manually
1. Set desired update interval (default 12 hours)

    ```python
    interval = 60 * 60 * 12  # Run every 12 hours
    ```

2. Run as root

    ```shell
    sudo ./smartserver.py
    ```

3. Access through browser: 

    ```shell
    localhost:8888
    ```

### Option 2: Run With systemd
1. Clone into `/opt/snapraid-smart-server/`

2. Set desired update interval (default 12 hours)

    ```python
    interval = 60 * 60 * 12  # Run every 12 hours
    ```

3. Run installer script

    ```shell
    sudo ./install-service.sh
    ```

4. Access through browser: 

    ```shell
    localhost:8888
    ```