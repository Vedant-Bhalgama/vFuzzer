# vFuzzer
vFuzzer is a tool developed for fuzzing buffer overflows, For now, It can be used for fuzzing plain vanilla stack based buffer overflows, The tool is still under development, More features will be added in the future! If you want to collaborate, feel free to do so! 

# Installation
- For using the tool, All you have to do is clone this repository locally, You should have Python3 installed on your machine in order to use it.
`git clone https://github.com/Vedant-Bhalgama/vFuzzer.git`
- After cloning it, Make sure to install `pyfiglet`
`pip3 install pyfiglet`

# Usage
- To get the help menu, Specify the `-h` flag, Here is a brief description of each flag and what it does.
- `-h, --help` : Shows the default help menu
- `-b, --buffer` : Specify the amount of buffer you want to send, If you want to send 100 bytes, Specify 100 over here, etc.
- `-d, --delay` : Specify the time delay before starting the loop again, If you want to wait for 1 second, Specify 1.
- `-t, --target` : Specify the target host which you want to fuzz
- `-p, --port`: Specify the target port which you want to fuzz
- `-nop, --noprefix` : If you don't want to set a prefix, Make sure to specify this flag.
- `-rf, --recvfirst` : Make sure to specify this flag and set the value to `1` if the server is sending data first, If the server is sending data first and you don't receive it, The progran will hang, If you don't want to receive first, set the value to `0`.
- `-s, --setprefix` : You need to specify this flag and a prefix to it if you are not using the `-nop` flag.

`Example (With Prefix) : python ./vfuzzer.py -b 1000 -d 2 -s 'administrator' -t 192.168.1.32, -p 9091 -rf 0`
`Example (Without Prefix) : python ./vfuzzer.py -nop -b 1000 -d 1 -t 192.168.1.32, -p 9091 -rf 1`


![image](https://user-images.githubusercontent.com/67494275/132438664-aa2e95c5-613a-4a8f-901a-5cd3587820e3.png)
