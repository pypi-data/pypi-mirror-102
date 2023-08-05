
int intbits_le(int len, char *n) {
	char ri = 0;
	char ry = 0;
	char i = 0;
	
	if (len == 0) {
		return 0;
	}

	for (int b = 0; b < len; b++) {
		for (i = 0; i < 8; i++) {
			if (((1 << i) & *(n + b)) > 0) {
				ri = i + 1;
				ry = b;
			}			 
		}
	}

	if (ri == 0 && ry == 0) {
		ri = 1;
	}

	return ri + (ry * 8);
}

int intbytes_le(int len, char *n) {
	int r = intbits_le(len, n);
	return (r - 1) / 8 + 1;
}
