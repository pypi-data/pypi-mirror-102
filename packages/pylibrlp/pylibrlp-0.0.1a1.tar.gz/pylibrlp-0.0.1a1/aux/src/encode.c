#include <stdint.h>
#include <string.h>

#include "rlp.h"
#include "bits.h"
#include "endian.h"


int rlp_add(rlp_encoder_t *encoder, int len, const char *data) {
	char v;
	int lenlen;
	size_t r;

	r = (size_t)encoder->ptr;

	if (len == 0) {
		*(encoder->ptr) = 0x80;
		encoder->ptr++;
		encoder->size++;
	} else {
		v = (char)*data;
		if (len == 1 && v < 56) {
			*(encoder->ptr) = v;
			encoder->ptr++;
			encoder->size++;
		} else {
			v = (char)*data;
			if (len < 56) {
				*(encoder->ptr) = len + 0x80;
				encoder->ptr++;
				memcpy(encoder->ptr, data, len);
				encoder->ptr += len;
				encoder->size++;
			} else {
				lenlen = intbytes_le(sizeof(int), (char*)&len);
				*(encoder->ptr) = lenlen + 0xb7;
				encoder->ptr++;
				to_endian(CONVERT_BIGENDIAN, lenlen, &len);
				memcpy(encoder->ptr, &len, lenlen);
				to_endian(CONVERT_PLATFORM, lenlen, &len);
				encoder->ptr += lenlen;
				memcpy(encoder->ptr, data, len); 
				encoder->ptr += len;
				encoder->size += 1 + lenlen;
			}
		}
	}

	encoder->size += len;
	
	return (int)(r - (size_t)encoder->ptr);
}

int rlp_descend(rlp_encoder_t *encoder) {
	encoder->depth++;
	encoder->list_ptr[encoder->depth] = encoder->ptr;
	return encoder->depth;
}

int rlp_ascend(rlp_encoder_t *encoder) {
	size_t len;
	char *ptr;
	int lenlen;

	ptr = encoder->list_ptr[encoder->depth];
	len = encoder->ptr - ptr;
	if (len < 56) {
		memcpy(ptr + 1, ptr, len);
		*(ptr) = 0xc0 + len;
		encoder->ptr++;
		encoder->size++;
	} else {
		lenlen = intbytes_le(sizeof(size_t), (char*)&len);
		memcpy(ptr + 1 + lenlen, ptr, len);
		*ptr = lenlen + 0xf7;
		to_endian(CONVERT_BIGENDIAN, lenlen, &len);
		memcpy(ptr+1, &len, lenlen);
		to_endian(CONVERT_PLATFORM, lenlen, &len);
		encoder->ptr += (lenlen + 1);
		encoder->size + 1 + lenlen;
	}
	encoder->depth--;

	return encoder->depth;
}
