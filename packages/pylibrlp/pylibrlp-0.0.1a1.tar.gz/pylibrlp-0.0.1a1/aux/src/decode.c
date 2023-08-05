#include <string.h>

#include "endian.h"
#include "rlp.h"

static int process_state_token(rlp_encoder_t *encoder) {
	int len = 0;
	int lenlen = 0;
	unsigned char token;

	token = *encoder->ptr;

	if (encoder->ptr == encoder->list_ptr[encoder->depth]) {
		encoder->depth--;
		encoder->state = RLP_LIST_ASCEND;
		len = 0;

	} else if (token >= 0xf7) {
		lenlen = token - 0xf7;
		encoder->ptr++;
		len = 0;
		memcpy(&len, encoder->ptr, lenlen);
		if (lenlen > 1 && is_le()) {
			to_endian(CONVERT_LITTLEENDIAN, lenlen, &len);
		}
		encoder->depth++;
		encoder->ptr += lenlen;
		encoder->buf = encoder->ptr;
		encoder->list_ptr[encoder->depth] = encoder->buf + len;

		encoder->state = RLP_LIST_DESCEND;

	} else if (token >= 0xc0) {
		len = token - 0xc0;
		if (is_le()) {
			to_endian(CONVERT_LITTLEENDIAN, sizeof(len), &len);
		}
		encoder->depth++;
		encoder->ptr++;
		encoder->buf = encoder->ptr;
		encoder->list_ptr[encoder->depth] = encoder->buf + len;

		encoder->state = RLP_LIST_DESCEND;

	} else if (token >= 0xb7) {
		lenlen = token - 0xb7;
		encoder->ptr++;
		len = 0;
		memcpy(&len, encoder->ptr, lenlen);
		if (lenlen > 1 && is_le()) {
			to_endian(CONVERT_LITTLEENDIAN, lenlen, &len);
		}
		encoder->ptr += lenlen;
		
		encoder->buf = encoder->ptr;
		encoder->ptr += len;
		encoder->state = RLP_STRING;

	} else if (token >= 0x80) {
		len = token - 0x80;
		encoder->ptr++;

		encoder->buf = encoder->ptr;
		encoder->ptr += len;
		encoder->state = RLP_STRING;

	} else {
		encoder->list_ptr[encoder->depth] = encoder->ptr;
		encoder->buf = encoder->ptr;
		encoder->ptr++;
		len = 1;
		encoder->state = RLP_STRING;
	}
	
	return len;
}

int rlp_next(rlp_encoder_t *encoder, int *zlen, char **zdest) {
	int r;
	
	if (encoder->list_ptr[0] == encoder->ptr) {
		encoder->state = RLP_END;
		return -1;
	}

	*zlen = process_state_token(encoder);
	*zdest = encoder->buf;

	return 0;
}
