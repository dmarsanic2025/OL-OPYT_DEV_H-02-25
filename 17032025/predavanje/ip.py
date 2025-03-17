ip_oktet1, ip_oktet2, ip_oktet3, ip_oktet4 = 192, 168, 0, 184

print(ip_oktet1, ip_oktet2, ip_oktet3, ip_oktet4, sep=".")

print(
    bin(ip_oktet1)[2:],
    bin(ip_oktet2)[2:],
    bin(ip_oktet3)[2:],
    bin(ip_oktet4)[2:],
    sep=".",
)
print(
    oct(ip_oktet1)[2:],
    oct(ip_oktet2)[2:],
    oct(ip_oktet3)[2:],
    oct(ip_oktet4)[2:],
    sep=".",
)
print(
    hex(ip_oktet1)[2:],
    hex(ip_oktet2)[2:],
    hex(ip_oktet3)[2:],
    hex(ip_oktet4)[2:],
    sep=".",
)
