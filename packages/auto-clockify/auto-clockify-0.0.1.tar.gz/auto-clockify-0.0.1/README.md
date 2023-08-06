AutoClockify
============

This is a simple python command line utility with which you can automate calling the Clockify API to start and stop the timer.

Usage
-----

Start the timer:
> python main.py --config=/path/to/config.json start

Stop the timer:
> python main.py --config=/path/to/config.json stop


Configuration
--------------
The minimum configuration information you must supply in the JSON formatted configuration file is:

    {
      "base_url": "https://api.clockify.me/api/v1",
      "api_key": "_your_api_key",
      "user_id": "_your_user_id",
      "workspace_id": "_your_worspace_id"
    }

