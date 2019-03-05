#!/usr/bin/expect
spawn scp -r  /home/raghava/NCC2019/web ncc2019@ece.iisc.ernet.in:/home/users/ncc2019/
expect "password"
send "$@@!322\r"
interact
spawn scp -r  /home/raghava/NCC2019/web ncc2019@52.172.131.106:/home/ncc2019/
expect "password"
send "ncc2019@543@@\r"
interact


