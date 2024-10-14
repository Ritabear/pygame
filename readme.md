
# Flight War






## Installation for Ubuntu 20.04
To locate this file in your filesystem:
`find / -name libstdc++.so.6 2>/dev/null`
Then add the export LD_PRELOAD to the .bashrc file, e.g.:
`export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`

