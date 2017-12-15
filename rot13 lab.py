import time
import string
import codecs

# # Index	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# # English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# # ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
initial = input("Would you like to encrypt or decrypt?\n:")
user_in = input("Message to Encrypt:\n")
# # def rot13(user_er_in)times would you like to rotate the message?:\n"))
encryption_1 = codecs.encode(user_in, 'rot13')
print("ENCRYPTING")
time.sleep(3)
print(encryption_1)
